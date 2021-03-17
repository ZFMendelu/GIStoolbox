import arcpy


class surface_analysis:

    def __init__(self, parameters):
        self.mask = parameters["mask"]
        self.out_name = parameters["out_name"]
        self.out_folder = parameters["out_folder"]
        self.check_type(parameters)


    def check_type(self, parameters):
        if len(parameters["in_raster_wms_str"]) > 0:
            self.in_raster = parameters["in_raster_wms"]
            self.in_raster_text = parameters["in_raster_wms_str"]
            self.type = "wms"
        else:
            self.in_raster = parameters["in_raster_local"]
            self.in_raster_text = parameters["in_raster_local_str"]
            self.type = "local"


    def extract_raster_by_mask (self):
        if self.type == "wms":
            arcpy.AddMessage("Creating raster: " + self.out_folder + "\\" + self.out_name)
            self.out_extract_by_mask = arcpy.sa.ExtractByMask(self.in_raster, self.mask)
            self.out_extract_by_mask.save(self.out_folder + "\\" + self.out_name)
        else:
            arcpy.AddMessage("Using raster: " + self.in_raster_text)
            self.out_extract_by_mask = self.in_raster

    def slope(self):
        arcpy.AddMessage("Creating slope: " + self.out_folder + "\\" + self.out_name + "_s")
        out_slope = arcpy.sa.Slope(self.out_extract_by_mask, "DEGREE")
        out_slope.save(self.out_folder + "\\"+ self.out_name + "_s")

    def hillshade(self):
        arcpy.AddMessage("Creating hillshade: " + self.out_folder + "\\" + self.out_name + "_h")
        out_hillshade = arcpy.sa.Hillshade(self.out_extract_by_mask)
        out_hillshade.save(self.out_folder + "\\"+ self.out_name + "_h")

    def aspect(self):
        arcpy.AddMessage("Creating aspect: " + self.out_folder + "\\" + self.out_name + "_a")
        out_aspect = arcpy.sa.Aspect(self.out_extract_by_mask)
        out_aspect.save(self.out_folder + "\\"+ self.out_name + "_a")

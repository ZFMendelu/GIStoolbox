import arcpy
from surface_analysis_class import surface_analysis

#Get parameters from ArcGIS
parameters = {
    "in_raster_wms": arcpy.GetParameter(0),
    "in_raster_wms_str": arcpy.GetParameterAsText(0),
    "in_raster_local": arcpy.GetParameter(1),
    "in_raster_local_str": arcpy.GetParameterAsText(1),
    "mask": arcpy.GetParameter(2),
    "out_name": arcpy.GetParameter(3),
    "out_folder": arcpy.GetParameterAsText(4)
}


sa = surface_analysis(parameters)


sa.extract_raster_by_mask()
sa.slope()
sa.hillshade()
sa.aspect()
arcpy.AddMessage("Thx, bro/sis.  XOXO")


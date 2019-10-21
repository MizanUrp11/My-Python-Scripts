import arcpy, os,sys
arcpy.env.workspace = "C:/Users/mizan_admin/SHAREit/Pictures"
rasters = arcpy.ListRasters("*","jpg")
pt = arcpy.Point()
for Images in rasters:
    names= Images.split("__")
    names1 = names[-2]
    composite = names1.split("_")
    lon = composite[-1]
    lat = composite[-2]
    print lat +", "+ lon
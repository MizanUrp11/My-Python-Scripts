import arcpy
arcpy.env.workspace = r'C:\Users\mizan_admin\Desktop\for kauser vai\from\Faridpur_Kawsar\All_GDB_Faridpur\Physical_Feature_Faridpur.gdb'
for f in arcpy.ListFeatureClasses():
    featureclass = f
    fieldnames = [f.name for f in arcpy.ListFields(featureclass)]
    print featureclass
    print fieldnames
    print ""

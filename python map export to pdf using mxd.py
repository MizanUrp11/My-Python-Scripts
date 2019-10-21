import arcpy, os
folderPath = r"C:\Users\mizan_admin\Desktop\Ramu\Ramu_Misty\MXD"
print "The path is:----"+ folderPath
for filename in os.listdir(folderPath):
##    print filename
    fullPath = os.path.join(folderPath,filename)
##    print fullPath
    if os.path.isfile(fullPath):
        basename, extention = os.path.splitext(fullPath)
        print extention
##        if extention.lower() == ".mxd":
##            mxd = arcpy.mapping.MapDocument(fullPath)
##            arcpy.mapping.ExportToPDF(mxd,basename + ".pdf")
import arcpy
from arcpy import env
env.workspace = r"C:\Users\mizan_admin\SHAREit"
arcpy.CreatePersonalGDB_management(r"C:\Users\mizan_admin\SHAREit\Pictures","photo.mdb", "9.2")
#set local variables
inFolder = "Pictures"
outFeatures = r"C:\Users\mizan_admin\SHAREit\Pictures\photo.mdb\photos"
badPhotosList = r"C:\Users\mizan_admin\SHAREit\Pictures\photo.mdb\photos_noGPS"
photoOption = "ONLY_GEOTAGGED"
attachmentsOption = "ADD_ATTACHMENTS"
arcpy.GeoTaggedPhotosToPoints_management(inFolder, outFeatures, badPhotosList, photoOption, attachmentsOption)



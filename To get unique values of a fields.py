import arcpy
table= 'Pourashava_Structure'
field = 'Str_Type'
with arcpy.da.SearchCursor(table,[field]) as cursor:
    myValues = sorted({row[0] for row in cursor})
    
print myValues
for x in myValues:
    print x
    


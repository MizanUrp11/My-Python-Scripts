fc = 'Union_Structure'
listfields = arcpy.ListFields("Union_Structure")
for x in listfields:
    print "Name:" + str(x.name) + " Type: " + str(x.type) + " Length: " + str(x.length)
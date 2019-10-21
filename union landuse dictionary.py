def classfromName(field):
    dictionary = {'Hospital':'Health Facilities',
    'Hostel':'Residential',
    'House':'Residential',
    'Industrial':'Industrial',
    'Market':'Commercial',
    'Miscellaneous':'Miscellaneous',
    'Mixed Use':'Mixed Use',
    'Monument':'Miscellaneous',
    'Office':'Non-Government Office',
    'Others':'Miscellaneous',
    'Religious':'Religious',
    'Shop':'Commercial',
    'Under Construction':'Miscellaneous'}
    return dictionary.get(field,'undefined')
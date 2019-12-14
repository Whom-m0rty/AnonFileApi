# AnonFileApi
Library for AnonFile API

for upload file to anonfile:

anonfile.upload_file(file)

exapmle: 

import anonfile

api = anonfile.upload_file('123.txt') #returns JSON dict
print(api)


for get info file:

info = anonfile.get_file_info(id)

example:

import anonfile

id = 'Lb4f83F9na'

info = anonfile.get_file_info(id) #returns JSON dict
print(info)


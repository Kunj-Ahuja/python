from mongo_setup import collection as  col

for i in col.find().sort('name',-1):
    print(i['name'])
#1 -> ascending, -1 -> desecending
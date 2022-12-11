from mongo_setup import collection as  col

x = col.find_one({'name' : 'Kunj'})
print(x['name'])

y = col.find() 
for i in y:
    print(i['name'])

z = col.find({'name' : { '$regex' : 'R'}}) #$regex -> startswith
for i in z:
    print(i['name'])

a = col.find().limit(1) #limits the result
for i in a:
    print(i['name'])
from mongo_setup import collection 

singleData = {
    'name' : 'Kunj'
}
manyData = [
    {
        'name' : 'Kunj'
    },{
        'name' : 'Rahul'
    }
]

# collection.insert_one(singleData)
# collection.insert_many(manyData)
from mongo_setup import collection as  col

col.delete_one({ 'name' : 'Kunj'})
col.delete_many({ 'name' : {'$gt' : 'A'}}) 

#$gt -> greater than 
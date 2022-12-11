import pymongo
url = 'mongodb+srv://kunj:kunj29@cluster0.yrlml0x.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(url)
db = client['DATABASE']
collection = db['COLLECTION']


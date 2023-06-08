import pymongo

client = pymongo.MongoClient("mongodb+srv://akritisingh:akritisingh@cluster0.jfytf1r.mongodb.net/")
db = client.test
print(db)

d = {
    "name": "akriti",
    "email" : "akriti@gmail.com",
    "surname" : "singh"
}
db1 = client['mongodbimport']
coll = db1['test']
coll.insert_one(d)
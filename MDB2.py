import pymongo

client = pymongo.MongoClient("mongodb+srv://akritisingh:akritisingh@cluster0.8d5kqsv.mongodb.net/")
db = client.test

database = client["myinfo"]
collection = database["Akki"]

"""record = collection.find()
for i in record:
    print(i)"""

# Query to find some data
#data = collection.find({"companyName" : 'iNeuron'})
data = collection.find({"courseOffered" : {"$gt": "E"}})
for i in data:
    print(i)

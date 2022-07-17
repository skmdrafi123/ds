import pymongo


client = pymongo.MongoClient("mongodb+srv://<smrafi2>:<BCvRym2NxKRKVGJt>@cluster0.1vcbf.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
d = {
    "name":"rafi",
    "email" : "test@gmail.com",
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
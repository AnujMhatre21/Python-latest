import pymongo 

# create a mongobd client 
# conn_str = ""
client = pymongo.MongoClient()


# create a db 
mydb = client["pymongo_demo"]

# create a collection means tables 
myCollection = mydb["demo_collecrtion"]


# create a document 
# myDoc = {
#     "name":"Anuj",
#     "Course": "Core Java"
# }

# insert a document
# in return we will get the inserted id
# res = myCollection.insert_one(myDoc)
# print(res.inserted_id)

# Reading the Document
record = myCollection.find_one()
print(record)
# print(client.list_database_names())


# Updating the record
query = {
    "Course": "Addvance Java"
}

new_value = {
    "$set": {
        "message": "Course Updated"
    }
}

new_record = myCollection.update_one(query,new_value)
print(new_record)
record = myCollection.find_one()
print(record)
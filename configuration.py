from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://<user>:<password>@fastapi-tutorial.aootn.mongodb.net/?retryWrites=true&w=majority&appName=fastapi-tutorial"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Create a database
db = client.bookstore

# Create a collection
collection = db.get_collection("books")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

from pymongo import MongoClient

MONGO_URI = "mongodb+srv://tadipadhma36_db_user:Padhu_123@cluster0.ruuu7jn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["primetrade"]

users = db["users"]
tasks = db["tasks"]
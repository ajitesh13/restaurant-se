# dbusername = ajitesh
# dbpassword = 1234

from pymongo import MongoClient

try:
    client = MongoClient(
        "mongodb+srv://ajitesh:1234@cluster0.tprp0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    database = client.test
    print("MongoDB Connected\n")
except:
    print("MongoDB Connection Error\n")

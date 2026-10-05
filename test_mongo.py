from pymongo import MongoClient
uri = "mongodb+srv://<username>:<password>@cluster0.mekubbb.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
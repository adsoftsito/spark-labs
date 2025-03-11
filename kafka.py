from kafka import KafkaConsumer
#from pymongo import MongoClient
#from pymongo.server_api import ServerApi
import json
#import subprocess



# replace here with your mongodb url 
#uri = "mongodb+srv://adsoft:Adsoft321@cluster0.kzghgph.mongodb.net/?retryWrites=true&w=majority"


# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

#try:
#    client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
#    print(e)

# Connect to MongoDB and pizza_data database

#try:
#    client = MongoClient(uri, server_api=ServerApi('1'))
#    client.admin.command('ping')
#    print("Pinged your deployment. You successfully connected to MongoDB!")

#    db = client.memes
#    print("MongoDB Connected successfully!")
#except:
#    print("Could not connect to MongoDB")

consumer = KafkaConsumer('test',bootstrap_servers=[
     'localhost:9092'
     ])
# Parse received data from Kafka
for msg in consumer:
    record = json.loads(msg.value)
    print(record)

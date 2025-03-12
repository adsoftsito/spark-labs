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

consumer = KafkaConsumer(
    bootstrap_servers=["https://jubilant-meme-q77q57jr4x9347w-9092.app.github.dev:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="people.grp-0",
    key_deserializer=lambda x: json.loads(x.decode("utf-8")),
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)
consumer.subscribe(["people"])
for message in consumer:
    print('Message received: ', message.value)

#consumer = KafkaConsumer(
#     'test', 
#     bootstrap_servers=['localhost:9092']
#                        )
# Parse received data from Kafka
#for msg in consumer:
#    record = json.loads(msg.value)
#    print(record)

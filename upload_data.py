

from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url information
uri="mongodb+srv://shivani:alonerider983@cluster0.gsc4n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# create a new client and connect to server
client=MongoClient(uri)

# create database and collection name
DATABASE_NAME='shivani'
COLLECTION_NAME='sensorfault'

df=pd.read_csv('C:\Users\viran\OneDrive\sensor fault detection\notebooks\wafer_23012020_041211.csv')

df=df.drop('Unnamed: 0',axis=1)

# convertin to json file
json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
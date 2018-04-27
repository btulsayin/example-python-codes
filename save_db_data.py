# -*- coding: utf-8 -*-
#read txt file and save data to MongoDB
from pymongo import MongoClient

client = MongoClient()
db = client.test_db
collection = db.data  

filepath = 'C:/Users/lenovo/Downloads/sample.txt'  
with open(filepath) as fp:  
   line = fp.readline()
   count = 1
   while line:
       print("Line {}: {}".format(count, line.strip()))
       doc = {"id": count, "commend" : line.strip() }
       collection.insert_one(doc)
       line = fp.readline()
       count += 1

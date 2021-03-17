#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

class Mongo:
    
    def __init__(self, dbName, collectionName):
        self.dbName = dbName
        self.collectionName = collectionName

        self.connectDB()
        self.selectDB()
        self.selectCollection()

    def connectDB(self):
        self.connection = MongoClient("mongodb:///localhost:27017")
        print("Connect: OK")

    def selectDB(self):
        self.db = self.connection[self.dbName]
        print("Selected DB: {}".format(self.dbName))

    def selectCollection(self):
        self.collection = self.db[self.collectionName]
        print("Selected Collection: {}".format(self.collectionName))

    def getListDatabaseNames(self):
        return  self.connection.list_database_names()
    
    def showListDatabaseNames(self):
        print(self.getListDatabaseNames())

    def getListCollectionNames(self):
        return  self.db.list_collection_names()
    
    def showListCollectionNames(self):
        print(self.getListCollectionNames())

    def insertOne(self, data):
        return self.collection.insert_one(data)

    def insertMany(self, arrData):
        return self.collection.insert_many(arrData)

    def findAll(self):
        return self.collection.find()
    
    def findAllByLimit(self, limit):
        return self.collection.find().limit(limit)

    def findByWhere(self, query):
        return self.collection.find(query)

    def findOne(self):
        return self.collection.find_one()

    def upsert(self, query, data):
        # data = { "$set": { "name": "Big Data e Analytics" } }
        return self.collection.update_one(query, data)

    def deleteOne(self, query):
        return self.collection.delete_one(query)

    def deleteMany(self):
        return self.collection.delete_many({})

    def deleteCollection(self):
        return self.collection.drop()
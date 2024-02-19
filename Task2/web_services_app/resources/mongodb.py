import os
from datetime import datetime

from bson.objectid import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

from interfaces.databases import Database

load_dotenv()

user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
passwd = os.getenv("MONGO_INITDB_ROOT_PASSWORD")


class MongoDB(Database):

    @classmethod
    def conn(self) -> MongoClient:
        conn_uri = f'mongodb://{user}:{passwd}@mongo:27017/'
        client = MongoClient(conn_uri)

        return client

    def insert(self, collection, doc, many=False):

        if many:
            return collection.insert_many(
                [
                    post.update(
                        {"date_posted": datetime.now()}
                    ) for post in doc
                ]
            )

        dict_doc = doc[0]
        dict_doc.update({"date_posted": datetime.now()})

        return collection.insert_one(dict_doc)

    def select(self, collection):
        if collection is not None:
            try:

                return [post for post in collection.find()]
            except Exception as e:
                raise e
        raise ValueError

    def delete(self, collection, post_id):
        post = collection.find_one({"_id": ObjectId(post_id)})

        if post:
            return collection.delete_one(post)

        return None


mongo = MongoDB()

client = mongo.conn()

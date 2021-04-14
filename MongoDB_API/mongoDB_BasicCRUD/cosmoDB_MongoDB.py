'''
 @Author: Ritika Patidar
 @Date: 2021-04-09 09:07:00
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-04-09 09:07:00  
 @Title : perform CRUD operation on mongoDB 
'''
import sys
import os
sys.path.insert(0, os.path.relpath('LogFile'))
import loggerfile 
import pymongo
import json
from decouple import config

class mongoDB:
    """
        Description:
            this class define for CRUD operation implementation
    """
    def __init__(self):
        uri = config('mdb_uri')
        self.client = pymongo.MongoClient(uri)
        self.database=self.client["database_addressbook"]
        self.collection=self.database["collection_Addressbook"]
    
    def insert_data(self):
        """
            Description:
                this function is define for insert data into mongodb
            Parameter:
                None
            Return:
                None
        """
        try:
            with open('/home/patidar/Desktop/AddressBook.json') as file:
                file_data = json.load(file)
            if isinstance(file_data, list):
                insert_value=self.collection.insert_many(file_data)  
            else:
                insert_value=self.collection.insert_one(file_data)
            print(insert_value.inserted_ids) 
            loggerfile.Logger("info","insert data successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

    def update_data(self):
        """
            Description:
                this function is define for update data into mongodb
            Parameter:
                None
            Return:
                None
        """
        try:
            myquery = {"first_name": "gopal"}
            newvalues = { "$set": {"first_name": "ramesh"}}
            updated_value=self.collection.update_many(myquery, newvalues)
            print(updated_value.modified_count, "documents updated.") 
            loggerfile.Logger("info","update data successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

    def find_data(self):
        """
            Description:
                this function is define for find all data into mongodb
            Parameter:
                None
            Return:
                None
        """
        try:
            data = self.collection.find().limit(5)
            for data_value in data:
                print(data_value)
            loggerfile.Logger("info","find data successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))
    
    def delete_document(self):
        """
            Description:
                this function is define for delete data into mongodb
            Parameter:
                None
            Return:
                None
        """
        try:
            myquery = { "city": "indore" }
            deleted_value=self.collection.delete_one(myquery)
            print(deleted_value.deleted_count, "deleted document successfull")
            loggerfile.Logger("info","delete document successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))

    def drop_collection(self):
        """
            Description:
                this function is define for drop collection
            Parameter:
                None
            Return:
                None
        """
        try:
            self.collection.drop() 
            loggerfile.Logger("info","drop collection successfully")
        except Exception as error:
            loggerfile.Logger("error","{0} error occured".format(error))



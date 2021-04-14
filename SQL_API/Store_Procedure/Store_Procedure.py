'''
 @Author: Ritika Patidar
 @Date: 2021-04-10 8:15:10
 @Last Modified by: Ritika Patidar
 @Last Modified time: 2021-04-10 8:15:38  
 @Title : To Write Stored Procedure In Javascript For SQL Api And Run It Using Python 
'''

import uuid
import azure.cosmos.cosmos_client as cosmos_client
from decouple import config

url = config('SQL_url')
key = config('SQL_key')
database_name = config('SQL_database_name')
container_name = config('SQL_container_name')

with open('spCreateToDoItems.js') as file:
    file_contents = file.read()

sproc = {
    'id': 'spCreateToDoItem1',
    'serverScript': file_contents,
}
client = cosmos_client.CosmosClient(url, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
created_sproc = container.scripts.create_stored_procedure(body=sproc)

new_id= str(uuid.uuid4())
# Creating a document for a container with "id" as a partition key.
new_item =   {
      "id": new_id, 
      "genre":"Mystery",
      "name":"Agatha Christie",
      "isComplete":False
   }
result = container.scripts.execute_stored_procedure(sproc=created_sproc,params=[[new_item]], partition_key=new_id)



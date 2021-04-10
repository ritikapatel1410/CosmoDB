import azure.cosmos.cosmos_client as cosmos_client
from decouple import config

url = config('SQL_url')
key = config('SQL_key')
database_name = config('SQL_database_name')
container_name = config('SQL_container_name')

with open('udfPrice.js') as file:
    file_contents = file.read()
udf_definition = {
    'id': 'Tax',
    'serverScript': file_contents,
}
client = cosmos_client.CosmosClient(url, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
udf = container.scripts.create_user_defined_function(udf_definition)

import json
for item in container.query_items(
    query='SELECT * FROM novels n WHERE udf.Tax(n.price) > 150',
    enable_cross_partition_query=True):    
      print(json.dumps(item, indent=True))
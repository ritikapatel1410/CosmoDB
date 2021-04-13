# CosmoDB SQL API 

* Prerequisites

 * Azure subscription
 * Azure Cosmo db Account
 * Azure Blob Storage
 * Azure Data factory

* create store procedure into cosmodb

  * In the Azure Cosmos DB blade, locate and select the Data Explorer link on the left side of the blade.
  * In the Data Explorer section, expand the your database node and then expand the your container node.
  * Within the your container node, select the Items link.
  * Select the New Stored Procedure button (two gears icon) at the top of the Data Explorer section.
  * run Store_Procedure code

* create UDFs into cosmodb

  * In the Azure Cosmos DB blade, locate and select the Data Explorer link on the left side of the blade.
  * In the Data Explorer section, expand the your database node and then expand the your container node.
  * Within the your container node, select the Items link.
  * Select the New user defined functions button (two gears icon) at the top of the Data Explorer section.
  * run User_defined_function code 

* cosmo db import

  * In Azure blob storage import json which you want to import into cosmodb
  * In data factory Select the Author & Monitor tile to start the Azure Data Factory user interface (UI) application on a separate tab.
  * Start the Copy Data tool
    * On the Let's get started page, select the Copy Data tile to start the Copy Data tool.
    * On the Properties page of the Copy Data tool, you can specify a name for the pipeline and its description, then select Next.
    * On the Source data store page, complete the following steps:
      * Click + Create new connection to add a connection.
      * Select the linked service type that you want to create for the source connection then select Continue.
      * On the New Linked Service (Azure Blob Storage) page, specify a name for your linked service. Select your storage account from the Storage account name list, test connection, and then select Create.
      * Select the newly created linked service as source, and then click Next.
  * On the Choose the input file or folder page, complete the following steps:
    * Click Browse to navigate to the your input folder, select the json file, and then click Choose.
    * Select the Binary copy checkbox to copy file as-is, and then select Next.
    * On the Destination data store page, select the Azure Blob Storage linked service you created, and then select Next.
    * For the Destination data store add the Cosmos DB target data store by selecting Create new connection and selecting Azure Cosmos DB (SQL API).
    * Name the linked service and select your Azure subscription and Cosmos DB account. You should also select the your Cosmos DB database that you created earlier.
    * Select your newly created connection as the Destination date store.
    * Select your container from the drop-down menu. You will map your Blob storage file to the correct Cosmos DB container. Select Next to continue
    * Select through the Table mapping screen.
    * There is no need to change any Settings. Select next.
    * Select Next to begin deployment After deployment is complete, select Monitor.
    * After a few minutes, refresh the page and the status for the ImportNutrition pipeline should be listed as Succeeded.
    * Once the import process has completed, close the ADF. You will now proceed to validate your imported data.
  * Validate Imported Data
    * Return to the Azure Portal (http://portal.azure.com).
    * On the left side of the portal, select the Resource groups link.
    * In the Resource groups blade, locate and select your resource group which linked with cosmo db account.
    * In the resource group blade, select the Azure Cosmos DB account you recently created.
      * In the Azure Cosmos DB blade, locate and select the Data Explorer link on the left side of the blade.
      * In the Data Explorer section, expand the your database node which mentioned as destination during data copy in data factory and then expand the container node.
      * Within the cointainer node, select the Items link to view a subset of the various documents in the container. Select a few of the documents and observe the properties and structure of the document

* cosmo db export

  * Start the Copy Data tool
    * On the Let's get started page, select the Copy Data tile to start the Copy Data tool.
    * On the Properties page of the Copy Data tool, you can specify a name for the pipeline and its description, then select Next.
    * On the Source data store page, complete the following steps:
      * Click + Create new connection to add a connection.
      * Select the linked service type that you want to create for the source connection. 
      * On the New Linked Service (Cosmo db Storage) page, specify a name for your linked service. Select your Cosmo db Storage account from the Cosmo db Storage account name list, test connection, and then select Create.
      * Select the newly created linked service as source, and then click Next.
      
        * On the Choose the input file or folder page, complete the following steps:
    * Click Browse to navigate to the your database, select cointainer and then click Choose.
    * Select the Binary copy checkbox to copy file as-is, and then select Next.
    * On the Destination data store page, select the Cosmo db Storage linked service you created, and then select Next.
    * For the Destination data store add the blob storage target data store by selecting Create new connection and selecting Azure blob storage.
    * Name the linked service and select your Azure subscription and blobe storage account. You should also select the your cointainer that ouput folder.
    * Select your newly created connection as the Destination date store.
    * Select your container from the drop-down menu. You will map your Cosmos DB container to the correct Blob storage file. Select Next to continue
    * Select through the Table mapping screen.
    * There is no need to change any Settings. Select next.
    * Select Next to begin deployment After deployment is complete, select Monitor.
    * After a few minutes, refresh the page and the status for the ImportNutrition pipeline should be listed as Succeeded.
    * Once the import process has completed, close the ADF. You will now proceed to validate your imported data.
  * Validate Imported Data
    * Return to the Azure Portal (http://portal.azure.com).
    * On the left side of the portal, select the Resource groups link.
    * In the Resource groups blade, locate and select your resource group which linked with azure storage account.
    * In the resource group blade, select the azure storage account you recently created.
      * In the azure blob storage blade, locate and select the cointainer and output folder.
      * In this you will see export json file.

Reference:

* https://docs.microsoft.com/en-us/cli/azure/cosmosdb/sql/user-defined-function?view=azure-cli-latest
* https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-write-stored-procedures-triggers-udfs
* https://cosmosdb.github.io/labs/dotnet/labs/02-load_data_with_adf.html
* https://docs.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory-copy-data-tool
  

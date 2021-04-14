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

* Create a function in Azure with Python using Visual Studio Code
  * Configure your environment
    * Before you get started, make sure you have the following requirements in place:
      * An Azure account with an active subscription. Create an account for free.
      * The Azure Functions Core Tools version 3.x.
      * Python versions that are supported by Azure Functions
      * Visual Studio Code on one of the supported platforms.
      * The Python extension for Visual Studio Code.
      * The Azure Functions extension for Visual Studio Code.
  * Create your local project
    * Choose the Azure icon in the Activity bar, then in the Azure: Functions area, select the Create new project... icon.
    * Choose a directory location for your project workspace and choose Select.
    * Provide the following information at the prompts:
    * Select a language for your function project: Choose Python.
    * Select a Python alias to create a virtual environment: Choose the location of your Python interpreter.If the location isn't shown, type in the full path to your Python binary.
    * Select a template for your project's first function: Choose Azure Cosmo DB  trigger.
    * Provide a function name: Type CosmoDBTrigger.
    * select Create new local app setting
    * select a database account
    * type name of the Cosmo DB database that includes the collection to be monitored
    * type name of collection to be monitored
    * type name of the collection to store the leases then select true
    * select open in new window
  * Run the function locally
    * To call your function, press F5 to start the function app project. Output from Core Tools is displayed in the Terminal panel. Your app starts in the Terminal panel. You can see the URL endpoint of your CosmoDBTrigger function running locally
    * With Core Tools running, go to the Azure: Functions area. Under Functions, expand Local Project > Functions. Right-click (Windows) or Ctrl - click (macOS) the CosmoDBTrigger function and choose Execute Function Now.
    * In Enter request body you see the request message body value of { "name": "Azure" }. Press Enter to send this request message to your function.
* Sign in to Azure
* Publish the project to Azure
  * Choose the Azure icon in the Activity bar, then in the Azure: Functions area, choose the Deploy to function app... button.
  * Provide the following information at the prompts:
    * Select folder: Choose a folder from your workspace or browse to one that contains your function app.You won't see this if you already have a valid function app opened.
    * Select subscription: Choose the subscription to use.You won't see this if you only have one subscription.
    * Select Function App in Azure: Choose + Create new Function App.
    * Enter a globally unique name for the function app: Type a name that is valid in a URL path. The name you type is validated to make sure that it's unique in Azure Functions.
    * Select a runtime: Choose the version of Python you've been running on locally. You can use the python --version command to check your version.
    * Select a location for new resources: For better performance, choose a region near you.
    * The extension shows the status of individual resources as they are being created in Azure in the notification area.
* When completed, the following Azure resources are created in your subscription, using names based on your function app name:
  * A resource group, which is a logical container for related resources.
  * A standard Azure Storage account, which maintains state and other information about your projects.
  * A consumption plan, which defines the underlying host for your serverless function app.
  * A function app, which provides the environment for executing your function code. A function app lets you group functions as a logical unit for easier management, deployment, and sharing of resources within the same hosting plan.
  * An Application Insights instance connected to the function app, which tracks usage of your serverless function
* Select View Output in this notification to view the creation and deployment results, including the Azure resources that you created. If you miss the notification, select the bell icon in the lower right corner to see it again.
* Run the function in Azure
  * Back in the Azure: Functions area in the side bar, expand your subscription, your new function app, and Functions. Right-click (Windows) or Ctrl - click (macOS) the CosmoDBTrigger function and choose Execute Function Now.... 
  * In Enter request body you see the request message body value of { "name": "Azure" }. Press Enter to send this request message to your function
  * When the function executes in Azure and returns a response, a notification is raised in Visual Studio Code.





Reference:

* https://docs.microsoft.com/en-us/cli/azure/cosmosdb/sql/user-defined-function?view=azure-cli-latest
* https://docs.microsoft.com/en-us/azure/cosmos-db/how-to-write-stored-procedures-triggers-udfs
* https://cosmosdb.github.io/labs/dotnet/labs/02-load_data_with_adf.html
* https://docs.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory-copy-data-tool
* https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python


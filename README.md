## Setting up and Testing Flask Endpoint

First, I navigated to the template app_basic.py code that we used as a class demo to use. From here, I modified parts of the code, such as the app.routes and putting emphasis on the middle name as the endpoint. This was my basic code as well that I used to deploy to Azure. My endpoint functionality screenshots are visible in the 'API Endpoints' folder of this repo-examples include: '/hello?name', '/hello?name=XXXmiddlename=XXX' and more. I also returned the names, capitalized with 'nameCapital'. It is important that the responses were in JSON format and the code also handled GET *and* POST requests. To view what is returned in the app depending on the request, I modified the end of the website to the route I included in my code. Also, the '?' sepates path and query parameters.

## Azure API Deployment + Management Integration 

To avoid the error of 'Unable to connect to Azure. Make sure you have the 'az' CLI...' (Screenshot documented in 'Errors' folder) later on when publishing the function app-

### Install Azure CLI 

To deploy, install Azure CLI using **'curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash'** This is not a one-time installment! This is done in one command or can be done step-by step following the [instructions](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt). Following that, we want to test that it installed with **'az'**. Following would be **'az login --use-device-code'**, which would prompt a code to be copied and pasted in the Microsoft login pop-up.

Follwing Installing Azure CLI, these steps can be followed: [instructions](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=macos%2Cbash%2Cazure-cli&pivots=python-mode-decorators). (Alternative Instructions)-include installing Azure Functions Core Tools with 'sudo apt-get install azure-functions-core-tools-4', then creating an Azure Functions Project func init YourFunctionProjectName --python', then cd into the function project 'cd YourFunctionProjectName', create the function 'func new --name HttpExample --template "HTTP trigger"', finally deploying 'func azure functionapp publish YourFunctionAppName' When following these alt. instructions I chose 'Python' and 'Anonymous' when promoted selections for purpose and access. Here creating a Functions App on Azure Portal directly was needed *before* deploying and publishing the function app (last step and also documented in 'Errors' folder) I successfully deployed my function app, invoking the URLs (Screenshot in 'Errors' folder as well) 

## Open API Specification

I updated my app_basic.py with app_updatedflasgger.py and I included docstring documentatation style for each endpoint, using the class demo as a template + guide. When I shifted the end of the site to '/apidocs', Swagger API appeared listing the GET and POST requests of my code. I noticed that Swagger documented these requests and also allows you to 'try it out' to determine what responses would appear along with CURL. Here I had a GET / Home endpoint, GET /hello Hello endpoint, and POST /hello Hello endpoint. This documentation provides an interactive way for users to test out the API endpoints along with related parameters

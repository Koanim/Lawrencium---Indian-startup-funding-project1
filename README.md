# Lawrencium---Indian-startup-funding-project1
## Accessing the data from the database
- Please follow the steps in this notebook to have access to the dataset. 

### Steps to take to use environment variables as opposed to credentials literals
1. Install pyodbc  - a package for creating connection strings to your remote database server
2. Install python-dotenv - a package for creating environment variables that will help you hide sensitve configuration informantion such as database credentials and API keys
3. Import all the necessary libraies
   1. pyodbc (for creating a connection)
   2. python-dotenv (loading environment variables)
   3. os (for accessing the environement variables using the load_env function. This is not needed if you use the dotenv_values function instead)
4. Now create a file called .env in the root of your project folder (Note, the file name begins with a dot)
5. In the .env file, put all your sensitive information like server name, database name, username, and password
6. Next create a .gitignore file (a new file with the name `.gitignore`. Note that gitignore file names begin with a dot)
7. Open the .gitignore file and type in the name of the .env file we just created like this "/.env". This will prevent git from tracking that file. Essesntially any file name in the gitignore file will be ignored by git and won't be checked into the repository
8. Create a connection by accessing your connection string with your defined environment variables

- Next, get data from other sources and concatenate (Depends on the project) to perform your analysis
- Extract and store key-value pairs from the .env file in a structured dictionary format for easy access to configuration settings.
- Retrieve specific credential information like database connection parameters (username, password, server address, etc.) from the structured dictionary.
- Formulate a connection string using the retrieved credential values, which is necessary for establishing a database connection.
- Leverage the pyodbc library's connect method by providing the connection string as an argument to initiate a connection to the server.
- Successfully establish a connection with the database server
- Transform and export the data retrieved from the SQL query into a CSV file format for each set of extracted data.
- Download the CSV file(s) from GitHub to a OneDrive account, facilitating file sharing and storage in the cloud.
- Add a new column to each dataframe to record the year of funding
























## Understanding the Business

-Venturing into the Indian start-ups ecosystem
-To investigate the ecosystem and propose the best course of action

-We will analyze funding recieved by start-ups in India from 2018 to 2021.

-We will seek to ask the following questions to help us propose the best cousrse of action.

##### 1) what is the average number of start-ups registered in Indian each year

##### 2) what is the average amount of funding recieved by a start-up per year

##### 3) Which industry do these start-ups belong

##### 4) How much funding in total is alocated to the industries

##### 5) Which start-ups recieved most funding and the industries they belong

##### 6) which start-ups survived after their first year of operation and the industry they belong

##### 7) which start-ups survived after the second year of operation and the industry they belong

##### 8) Which industries have the most successful start-ups

##### 9) What the loccations of the industrie that recieve most funding

##### 10) What is the Location of Industries that  

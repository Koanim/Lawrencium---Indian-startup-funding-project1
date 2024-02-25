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
- Add a new column to each dataframe to record the year of funding.
- We thoroughly clean the data to ensure its accuracy, consistency, and readiness for analysis.

 #### Few observations were made from the data cleaning
1. Rename 'Company Name' in df_fund2018, 'Company/Brand' in df_fund2019, and 'Company_Brand' in df_fund2020 and df_fund2021 to 'Company_Brand' for consistency.
2. Add the 'Founded' column to df_fund2018 to align with other dataframes.
3. Rename 'Industry' in df_fund2018 to 'Sector' to match the terminology used in other dataframes.
4. Replace 'Headquarter' with 'Location' in all dataframes except df_fund2018, which already uses 'Location'.
5. Change 'Round/Series' in df_fund2018 to 'stage' to harmonize column names across all dataframes.
6. Convert 'Amount($)' in df_fund2019 to 'Amount' for uniformity.
7. Standardize the description column to 'About Company' across all dataframes, removing underscores and aligning naming conventions.
8. Insert 'Founders' and 'Investors' columns into df_fund2018 to ensure all dataframes contain these fields.
9. Remove 'Column10' from df_fund2020 due to its null values to clean up the dataset.

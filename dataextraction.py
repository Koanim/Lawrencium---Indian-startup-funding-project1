import pandas as pd
from dotenv import dotenv_values
from sqlalchemy import create_engine
import pyodbc

# Load environment variables from .env file
environment_variables = dotenv_values('.env')
database = environment_variables.get("DATABASE")
server = environment_variables.get("SERVER")
username = environment_variables.get('USERNAME')
password = environment_variables.get("PASSWORD")

# Create the connection string for sqlalchemy
connection_string = f"DRIVER={{SQL SERVER}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Create the sqlalchemy engine
connection = pyodbc.connect(connection_string)

# Define your SQL query
query = "SELECT * FROM dbo.LP1_startup_funding2020"
query2 = "SELECT * FROM dbo.LP1_startup_funding2021"
# Fetch the data into a pandas DataFrame
data = pd.read_sql(query, connection)
data2 = pd.read_sql(query2, connection)


# Print the first few rows of the DataFrame
print(data2.head())
#converting the sql extracted data to csv respectively
data.to_csv("LP1_startup_funding2020.csv", index=False)
data2.to_csv("LP1_startup_funding2021.csv", index=False)
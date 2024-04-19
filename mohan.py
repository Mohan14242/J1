import pandas as pd
import mysql.connector

# Database credentials
host = 'database-1.cl844y0iiy16.us-east-1.rds.amazonaws.com'
user = 'admin'
password = 'Amohan9676$'
database = 'admin'

# Establish a connection to the database
connection = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Write your SQL query
sql_query = 'SELECT * FROM employees'

# Use pandas to execute the SQL query and load data into a DataFrame
df = pd.read_sql_query(sql_query, connection)

# Close the database connection
connection.close()

# Display the DataFrame
print(df)

import pyodbc
import pandas as pd
connection_string = ("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=localhost;"
                      "Database=AdventureWorks2022;"
                      "Trusted_Connection=yes;")

connection = pyodbc.connect(connection_string)    
print("Connection is established")
print(connection)

csr = connection.cursor()

# To insert multiple rows we can create list of multiple students
#insert_data_query = """INSERT INTO Student (ID, NAME, MAJOR, AGE)
#VALUES(?, ?, ?, ?)
#"""
#data_to_insert = [(153342, 'Tehmas', 'BSCS', 25), (153323, 'Ali', 'BBA', 22)]
#csr.execute(data_to_insert)

#csr.executemany(insert_data_query, data_to_insert)

#csr.execute(query)

query = "DELETE FROM Student WHERE ID = 153308"
csr.execute(query)

#To view table record in dataframe
query_to_display = "SELECT * FROM Student"
df = pd.read_sql_query(query_to_display, connection)
print(df)

connection.commit()
csr.close()
connection.close()

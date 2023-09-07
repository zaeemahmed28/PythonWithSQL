from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd

#engine = create_engine('mssql+pyodbc://localhost/AdventureWorks2022?driver=SQL Server?Trusted_Connection=yes')

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'Test_Employee'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __init__(self, Id, Name, Age):
        self.id = Id
        self.name = Name
        self.age = Age

    def __repr__(self):
        return f"{self.id} {self.name} {self.age}"

Server = 'localhost'
Database = 'AdventureWorks2022'
Driver = 'ODBC Driver 17 for SQL Server'
conn_string = f'mssql://@{Server}/{Database}?driver={Driver}'
engine = create_engine(conn_string)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

#Adding three employees in the table
emp = Employee(Id=313, Name="Ali", Age=22)
session.add(emp)

emp2 = Employee(323, "Bilal", 25)
emp3 = Employee(328, "Fawad", 30)

session.add_all([emp2, emp3])

employ = session.query(Employee)

#loop to print all rows in database
for e in employ:
    print(e.id, e.name, e.age)

#delete row
#result = session.query(Employee).filter(Employee.name=='Fawad').first()
#session.delete(result)
#session.commit()
#print(result)

#update row
#result = session.query(Employee).filter(Employee.name=='Ali').first()
#result.age = 24
#session.commit()
#print(result)

df = pd.DataFrame([(e.id, e.name, e.age) for e in employ], columns=['ID', 'Name', 'Age'])
df.index = df.index + 1    # To start index from 1 instead of 0
print(df)

session.commit()

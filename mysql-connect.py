from ShowData import ShowData
from Database import Database

try:
    Database.getObject().getData("select * from table1", ShowData())

except Exception as e:
    print(str(e))
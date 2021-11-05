import pymysql

db_pass = ""
db_user = "root"
db_host = "localhost"
db = "dbLibrary"

con = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db)

cur = con.cursor()
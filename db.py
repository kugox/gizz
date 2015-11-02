__author__ = 'WangChunQian'
import MySQLdb
db = MySQLdb.connect("localhost","root","050920","python")
cursor = db.cursor()
cursor.execute("SELECT uname from table1")
data = cursor.fetchone()
print "Database version : %s " % data
db.close()
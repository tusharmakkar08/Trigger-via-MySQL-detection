
import redis
import MySQLdb as mdb
import sys
import time

con=None

try:

    con=mdb.connect('localhost', 'testuser','test623', 'tio')		
    # Connecting to database
    cur=con.cursor()
    cur.execute("select * from student")
    # Executing Mysql command
    data=cur.fetchall()
    # Fetching the answer
    r_server = redis.Redis("localhost")
    # Connecting to localhost
    k=len(data)
    # Number of data entries in table
    for i in xrange(k):
        r_server.rpush("students",data[i])
		# Pushing in students list
    print r_server.lrange("students",0,-1)
    
    # Printing from starting to end
    r_server.delete("students")
    # Deleting the Reddis list 
    
except mdb.Error,e:
    
    print "Error %d: %s" % (e.args[0],e.args[1])
    # Printing Errors
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()
		# Closing connection


import redis
import MySQLdb as mdb
import sys
import time
import random



flag=0
# Variable for checking insert 

def trigger(no_trigger):
	""" 
	:param no_trigger: Number of triggers
	"""
	n=no_trigger
	for i in xrange(n):
		
		time.sleep(1)
		
		# Causing Delays
		
		l=random.randint(1,4)
		# Random Roll no. generation
		
		l4=random.randint(0,4)
		# Randomizing the triggers
		
		cur.execute("select * from student")
		data=cur.fetchall()
		k1=len(data)
		
		if l4<2:
			print "Inserted Checking"
		    # For  checking whether the trigger should be activated or not
			if l==1:
				cur.execute("insert into student (id,name,subject,marks) values ( 321,'Tushar Makkar','Information Technology' ,10 )")
			 # Inserting into table
			if l==2:
				cur.execute("insert into student (id,name,subject,marks) values ( 412, 'Tim Poston' , 'Object technology' , 9)")
			 # Inserting into table
			if l==3:
				cur.execute("insert into student (id,name,subject,marks) values ( 341, 'John Huffington' , 'Humanities' , 7)")
			 # Inserting into table 
			if l==4:
				cur.execute("insert into student (id,name,subject,marks) values ( 314, 'Koyal Malhotra' , 'Law and Economics' , 8)")
			 # Inserting into table
		else:
			print "No Insertion"	 
		cur.execute("select * from student")
		data=cur.fetchall()
		k=len(data)
		
		""" Checking whether the size of database is increased or not """
		
		if k!=k1:
			r_server.rpush("students",data[k-1])
		
		print r_server.lrange("students",0,-1)

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
    
    print "Initial Queue"
    print r_server.lrange("students",0,-1)
    # Printing from starting to end

    
    no_trigger=input("Enter number of triggers you want to have ?")
    
    trigger(no_trigger)
    # Calling trigger function
    
    
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

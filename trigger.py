
import redis
import MySQLdb as mdb
import sys
import time
import random
import sptrial


namelist=["Tushar Makkar","Tim Poston","Robert Frost","John \
Kimberly","Jim Mathews","Henry Jacobson","Mark Salvador"]
# Namelist of Students

subjectlist=["Data Structures and programming","Unix Programming\
","Microprocessors and Interfacing","Theory of Automation","Artificial\
 Intelligence","Object Technology","Computer Networks"]
# Names Of Subjects

flag=0
# Variable for checking insert 

def trigger(no_trigger):
	""" 
	:param no_trigger: Number of triggers
	"""
	n=no_trigger
	for i in xrange(n):
		time.sleep(1)
		
		sptrial.flag=0
		
		# Causing Delays
		
		l=random.randint(1,500)
		# Random Roll no. generation
		
		l1=random.randint(0,6)
		# Random Name Generation
		
		l2=random.randint(0,6)
		# Random Subject Generation
		
		l3=random.randint(1,10)
		# Random Grade Generation
		
		l4=random.randint(0,1)
		# Randomizing the triggers
		
		if l4==1:
			print "Inserted Checking"
		  # For  checking whether the trigger should be activated or not
			
			cur.execute("insert into student (id,name,subject,marks)\
			 values (.l. , '.namelist[l1].' , '.subjectlist[l2].' , .l3.)")
			 # Inserting into table
		
		cur.execute("DELIMITER $$\
		CREATE TRIGGER inserting_trigger\
		AFTER student INSERT \
		sys_exec('python /home/ai/trigger/sptrial.py');$$\
		DELIMITER;")
		
		if sptrial.flag==1:
			cur.execute("select * from student")
			data=cur.fetchall()
			k=len(data)
			r_server.rpush("students",data[k-1])
			print data[k-1]
			sptrial.flag=0

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
    
    no_trigger=input("Enter number of triggers you want to have ?")
    
    trigger(no_trigger)
    # Calling trigger function
    
    print r_server.lrange("students",0,-1)
    
except mdb.Error,e:
    
    print "Error %d: %s" % (e.args[0],e.args[1])
    # Printing Errors
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()
		# Closing connection

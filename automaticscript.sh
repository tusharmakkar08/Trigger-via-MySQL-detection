mysql -u root -p'ai' -Bse 'drop database if exists tio ;\
CREATE DATABASE tio;\
FLUSH PRIVILEGES;\
GRANT ALL PRIVILEGES ON tio.* To "testuser"@"localhost" IDENTIFIED BY "test623";\
use tio;\
source try.sql;\
insert into student (id,name,subject,marks) values \
(213,"Tushar Makkar","Data Structures",10),\
(214,"John Kimberly","Unix Programming",9),\
(213,"Tushar Makkar","Microprocessor Programming",9),\
(215,"Tim Berkeley","Data Structures",8)'
 # Creating database ,  new username and Password and  Inserting Entries into the table

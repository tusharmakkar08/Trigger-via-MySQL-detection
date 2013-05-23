drop table if exists student;
CREATE TABLE student
(
  id              int unsigned NOT NULL , 				# ID of the student
  name           varchar(255) NOT NULL,                # Name of the student
  subject          varchar(255) NOT NULL,                # Subject name
  marks           decimal(10,2) NOT NULL               # The marks of student
)ENGINE=InnoDB;

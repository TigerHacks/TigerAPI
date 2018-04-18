CREATE TABLE Users (
	id int NOT NULL AUTO_INCREMENT,
	first_name varchar(31) NOT NULL,
	last_name varchar(31) NOT NULL,
	email varchar(31) NOT NULL,
	phone_number varchar(15) NOT NULL,
	participants_id int,
	mentors_id int,
	administrator bool,
	PRIMARY KEY (id)
);

ALTER TABLE Users ADD CONSTRAINT Users_fk0 FOREIGN KEY (participants_id) REFERENCES Participants(id) 
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE Users ADD CONSTRAINT Users_fk1 FOREIGN KEY (mentors_id) REFERENCES Mentors(id) 
	ON UPDATE CASCADE
	ON DELETE CASCADE;
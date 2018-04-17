CREATE TABLE Mentors (
	id int NOT NULL AUTO_INCREMENT,
	company varchar(31) NOT NULL,
	job_title varchar(63) NOT NULL,
	current_location varchar(63) NOT NULL,
	skills varchar(255) NOT NULL,
	food_allergies varchar(255),
	gender varchar(15) NOT NULL,
	linkedin varchar(63) NOT NULL,
	github varchar(63) NOT NULL,
	approved bool NOT NULL,
	shirt_size varchar(3),
	PRIMARY KEY (id)
);
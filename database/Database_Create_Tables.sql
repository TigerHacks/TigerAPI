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

CREATE TABLE Participants (
	id int NOT NULL AUTO_INCREMENT,
	school varchar(31) NOT NULL,
	grade varchar(15) NOT NULL,
	age int NOT NULL,
	major varchar(31) NOT NULL,
	current_location varchar(63) NOT NULL,
	working_place varchar(255),
	title varchar(255),
	skills varchar(255) NOT NULL,
	food_allergies varchar(255),
	gender varchar(15),
	linkedin varchar(63),
	github varchar(63),
	shirt_size varchar(3) NOT NULL,
	transportation varchar(15) NOT NULL,
	lightning_interest bool(15) NOT NULL,
	professional_interest varchar(15) NOT NULL,
	PRIMARY KEY (id)
);

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

CREATE TABLE Sponsors (
	id int NOT NULL AUTO_INCREMENT,
	company_name varchar(63) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Authentication (
	username varchar(63) NOT NULL,
	password varchar(63) NOT NULL,
	user_id int NOT NULL,
	PRIMARY KEY (username)
);

CREATE TABLE Applications (
	id int NOT NULL AUTO_INCREMENT,
	resume blob NOT NULL,
	need_reinbursement bool NOT NULL,
	approved bool NOT NULL,
	reinbursement_request varchar(255) NOT NULL,
	rsvp_sent bool NOT NULL,
	attending bool NOT NULL,
	checked_in bool NOT NULL,
	participants_id int NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Prizes (
	id bigint NOT NULL AUTO_INCREMENT,
	prize_description varchar(255) NOT NULL,
	description_to_win varchar(255) NOT NULL,
	number_of_prizes int NOT NULL,
	sponsor_id int NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Participants_Prizes (
	id int NOT NULL AUTO_INCREMENT,
	participant_id int NOT NULL,
	prize_id int NOT NULL,
	PRIMARY KEY (id)
);

ALTER TABLE Users ADD CONSTRAINT Users_fk0 FOREIGN KEY (participants_id) REFERENCES Participants(id) 
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE Users ADD CONSTRAINT Users_fk1 FOREIGN KEY (mentors_id) REFERENCES Mentors(id) 
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE Authentication ADD CONSTRAINT Authentication_fk0 FOREIGN KEY (user_id) REFERENCES Users(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE Applications ADD CONSTRAINT Applications_fk0 FOREIGN KEY (participants_id) REFERENCES Participants(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE Prizes ADD CONSTRAINT Prizes_fk0 FOREIGN KEY (sponsor_id) REFERENCES Sponsors(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE Participants_Prizes ADD CONSTRAINT Participants_Prizes_fk0 FOREIGN KEY (participant_id) REFERENCES Participants(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE Participants_Prizes ADD CONSTRAINT Participants_Prizes_fk1 FOREIGN KEY (prize_id) REFERENCES Prizes(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;


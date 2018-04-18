CREATE TABLE Prizes (
	id bigint NOT NULL AUTO_INCREMENT,
	prize_description varchar(255) NOT NULL,
	description_to_win varchar(255) NOT NULL,
	number_of_prizes int NOT NULL,
	sponsor_id int NOT NULL,
	PRIMARY KEY (id)
);

ALTER TABLE Prizes ADD CONSTRAINT Prizes_fk0 FOREIGN KEY (sponsor_id) REFERENCES Sponsors(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

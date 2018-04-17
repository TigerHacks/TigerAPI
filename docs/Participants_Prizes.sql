CREATE TABLE Participants_Prizes (
	id int NOT NULL AUTO_INCREMENT,
	participant_id int NOT NULL,
	prize_id int NOT NULL,
	PRIMARY KEY (id)
);

ALTER TABLE Participants_Prizes ADD CONSTRAINT Participants_Prizes_fk0 FOREIGN KEY (participant_id) REFERENCES Participants(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;

ALTER TABLE Participants_Prizes ADD CONSTRAINT Participants_Prizes_fk1 FOREIGN KEY (prize_id) REFERENCES Prizes(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;
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

ALTER TABLE Applications ADD CONSTRAINT Applications_fk0 FOREIGN KEY (participants_id) REFERENCES Participants(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;
CREATE TABLE Authentication (
	username varchar(63) NOT NULL,
	password varchar(63) NOT NULL,
	user_id int NOT NULL,
	PRIMARY KEY (username)
);

ALTER TABLE Authentication ADD CONSTRAINT Authentication_fk0 FOREIGN KEY (user_id) REFERENCES Users(id)
	ON UPDATE CASCADE
	ON DELETE CASCADE;
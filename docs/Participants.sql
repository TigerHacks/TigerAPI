CREATE TABLE Participants(
	id INT,
	firstName VARCHAR(31),
	lastName VARCHAR(31),
	school VARCHAR(31), --should we have a table for schools???
	grade VARCHAR(15),
	email VARCHAR(31), --we might want to make this bigger to accommodate bigger email addresses?
	phoneNumber INT, --we might want to change this to VARCHAR
	currentLocation VARCHAR(63),
	workingPlace VARCHAR(255),
	title VARCHAR(255),
	skills VARCHAR(255),
	foodAllergies VARCHAR(255),
	socialMedia varchar(255), --we might want to change this to include separate twitter, instagram, and facebook fields
	gender VARCHAR(15), --modified to specify character amount
	
	PRIMARY KEY(id)
);
CREATE TABLE Prizes(
	id INT,
	prizeDescription VARCHAR(255),
	descriptionToWin VARCHAR(255),
	numPrizes INT,
	sponsor INT --FOREIGN KEY TO SPONSORS TABLE

	PRIMARY KEY(id)
);

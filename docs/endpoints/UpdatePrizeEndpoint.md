**PUT /update-prize** <br />
Updates an existing prize

URL Parameters <br />
None

Request Parameters <br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `id` | the ID of the prize | Yes |
| `prizeDescription` | a string of length up to 255 characters | Yes |
| `descriptionToWin` | a string of length up to 255 characters | Yes |
| `numberOfPrizes` | an int for the number of prizes to be given | Yes |
| `typeOfPrize` | 'money' or 'item' | Yes |
| `sponsorName` |  a string of length up to 255 characters | Yes |

Request
```
{
	"prizeDescription": "Google Home",
	"descriptionToWin": "Name entered in raffle",
 	"numberOfPrizes": 3,
  	"typeOfPrize": "item",
	"sponsorName": "Google"
}
```

Response
```
{
	"data": {
		"id": 1
		"prizeDescription": "Google Home",
		"descriptionToWin": "Name entered in raffle",
	  	"numberOfPrizes": 3,
	  	"typeOfPrize": "item",
		"sponsorName": "Google",
	}
}
```

Errors: <br>

| Error        | Source | Cause  |
| ------------ | ------ | ------ |
| NotFoundError | `id` | prize with the requested ID does not exist |

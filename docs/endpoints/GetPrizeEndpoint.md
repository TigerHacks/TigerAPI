**GET /get-prize** <br />
Gets a prize with specified ID

URL Parameters <br />
None

Request Parameters <br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `id` | the ID of the prize  | Yes |

Request
```
{
	"id": "1",
}
```

Response
```
{
	"data": {
		"id": 1,
		"prizeDescription": "Google Home",
		"descriptionToWin": "Name entered in raffle",
	  "numberOfPrizes": 3,
	  "typeOfPrize": "item",
		"sponsorName": "Google"
	}
}
```

Errors: <br>

| Error        | Source | Cause  |
| ------------ | ------ | ------ |
| NotFoundError | `id` | prize with the requested ID does not exist |

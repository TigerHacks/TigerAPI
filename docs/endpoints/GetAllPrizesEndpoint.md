**GET /get-all-prizes** <br />
Gets all prizes

URL Parameters <br />
None

Request Parameters <br />
None

Response
```
{
	"data": {
    "prizes": [
      {
        "id": 1
        "prizeDescription": "Google Home",
        "descriptionToWin": "Name entered in raffle",
        "numberOfPrizes": 3,
        "typeOfPrize": "item",
        "sponsorName": "Google",
      },{
        "id": 2
        "prizeDescription": "Google Home Mini",
        "descriptionToWin": "Name entered in raffle",
        "numberOfPrizes": 5,
        "typeOfPrize": "item",
        "sponsorName": "Google",
      },{
        "id": 3
        "prizeDescription": "iPhone",
        "descriptionToWin": "Name entered in raffle",
        "numberOfPrizes": 1,
        "typeOfPrize": "item",
        "sponsorName": "Apple",
      }
    ]
	}
}
```

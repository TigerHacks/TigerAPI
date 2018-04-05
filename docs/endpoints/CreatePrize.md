
**POST /create-prize** <br />
Creates a new prize

URL Parameters <br />
None

Request Parameters <br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
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
    "prizeDescription": "Google Home",
    "descriptionToWin": "Name entered in raffle",
    "numberOfPrizes": 3,
    "typeOfPrize": "item",
    "sponsorName": "Google",
    "id": 1
  }
}
```


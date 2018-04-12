**DELETE /delete-prize** <br />
Deletes a prize

URL Parameters <br />
None

Request Parameters <br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `id` | the ID of the prize | Yes |


Request
```
{
	"id": 1,
}
```

Response
```
{
	"data": {}
}
```

Errors: <br>

| Error        | Source | Cause  |
| ------------ | ------ | ------ |
| NotFoundError | `id` | prize with the requested ID does not exist |

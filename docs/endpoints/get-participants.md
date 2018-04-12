**GET participant/id** <br />
Allow the request get the information of the participant.

Headers <br />

| Header        | Description           | Required  |
| ------------- | --------------------- | --------- |
| `Authorization` | a valid authentication token | Yes |

URL Parameters <br />
| Parameter        | Description           | Required  |
| ------------- | --------------------- | --------- |
| `id` | the id of the user | Yes |

Response
```
{
    "firstName": "Joe",
    "lastName": "Smith",
    "school": "University of Missouri-Columbia",
    "level": "Senior",
    "email": "jsmith@mail.missouri.edu",
    "phoneNumber": 5733333333,
    "currentLocation": "Columbia",
    "workingPlace": "Columbia",
    "title": "student",
    "skills": ["Java", "C#", "Python"],
    "foodAllergies": "none",
    "socialMedia": "linktosocialmedia",
    "gender": "MALE"
}
```

Errors: <br>

| Error        | Source | Cause  |
| ------------ | ------ | ------ |
| InvalidHeaderError | `Authorization` | the authentication token was invalid or absent |
| NotFoundError | N/A | an attendee registration doesn't exist for the user |

---

[README.md](../README.md)

**POST /v1/registration/participant**<br />
Creates a new participant registration.

Headers

| Header        | Description           | Required  |
| ------------- | --------------------- | --------- |
| `Authorization` | a valid authentication token | Yes |

URL Parameters<br />
None

Request Parameters<br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `participant` | a JSON object containing the Participant Parameters below | Yes |
| `extraInfo` | an array of JSON objects of length at most two, each containing the ExtraInfo parameters below | No |
| `collaborators` | an array of JSON objects of length at most eight, each containing the RequestedCollaborator parameters below | No |
| `longForm` | an array of JSON objects of length at most two, each containing the LongForm parameters below | No |
| `osContributors` | an array of JSON objects of length at most eight, each containing the OSContributor parameters below | Yes |

Participant Parameters<br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `firstName` | the user's first name of length 31 or less | Yes |
| `lastName` | the user's last name of length 31 or less | Yes |
| `E-mail` | less than 31 characters | Yes |
| `age` | a number between 13 and 115 | No |
| `username` | less than 15 characters | Yes |
| `password` | less than 15 characters | Yes |
| `school` | the user's school of length 255 or less | Yes |
| `grade/level` | less than 15 characters | Yes |
| `major` | the user's major of length 63 or less | Yes |
| `phoneNumber` | the user's phone number, formatted as a string of length 15 or less | No |
| `transportation` | a string from the following options: ['NOT_NEEDED', 'BUS_REQUESTED', 'IN_STATE', 'OUT_OF_STATE'| Yes |
| `shirtSize` | a string of length 1 from the following options: ['S', 'M', 'L', 'XL'] | Yes |
| `diet` | a string from the following options: ['NONE', 'VEGETARIAN', 'VEGAN', 'GLUTEN_FREE'] | Yes |
| `gender` | a string from the following options: ['MALE', 'FEMALE', 'NON_BINARY', 'OTHER'] | Yes |
| `professionalInterest` | a string from the following options: ['NONE', 'INTERNORPARTTIME', 'FULLTIME', 'BOTH'] | Yes |
| `github` | the user's GitHub handle of length 50 or less | Yes |
| `linkedin` | the user's LinkedIn handle of length 50 or less | Yes |
| `hasLightningInterest` | a boolean indicating whether the user is interested in giving a short talk | No |


ExtraInfo Parameters<br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `info` | the extra user info length 16383 or less | Yes |



RequestedCollaborator Parameters<br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `collaborator` | the requested collaborator's email of length 255 or less | Yes |

LongForm Parameters<br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `info` | the response string to the given prompt of length 1023 or less | Yes |

OSContributor Parameters <br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `osContributor` | the requested contributor's contact info of length 255 or less | Yes |

Request
```
{
    "participant": {
                "firstName": "John",
                "lastName": "Doe",
                "E-mail": "abc56@mail.missouri.edu",
                "age": 19,
                "username": "",
                "password": "",
                "school": "University of Missouri - Columbia",
                "grade/level": "junior",
                "major": "Computer Science",
                "phoneNumber": "12345678910"
                "transportation": "NOT_NEEDED",
                "shirtSize": "M",
                "diet": "NONE",
                "gender": "MALE",
                "professionalInterest": "BOTH",
                "github": "JDoe1234",
                "linkedin": "JDoe5678",
                "hasLightningInterest": false,
    },
    "collaborators": [
        {
                    "collaborator": "collaborator@tigerhack.org"
        }
    ],
    "longForm": [
        {
                    "info": "One of the projects I'm really proud of is my HelloWorld Machine. It says 'Hello World' in ten different languages!"
        }
    ],
    "extraInfo": [
        {
                    "website": "mywebsite.com"
        }
    ],
    "osContributors": [
        {
                    "osContributor": "os contributors"
        }
    ]
}
```

Response
```
{
    "meta": null,
    "data": {
        "firstName": "John",
        "lastName": "Doe",
        "E-mail": "abc56@mail.missouri.edu",
        "age": 19,
        "username": "",
        "password": "",
        "school": "University of Missouri - Columbia",
        "grade/level": "junior",
        "major": "Computer Science",
        "phoneNumber": "12345678910"
        "transportation": "NOT_NEEDED",
        "shirtSize": "M",
        "diet": "NONE",
        "gender": "MALE",
        "professionalInterest": "BOTH",
        "github": "JDoe1234",
        "linkedin": "JDoe5678",
        "hasLightningInterest": false,
        "userId": 1,
        "id": 16,
        "osContributors": [
            {
                "osContributor": "os contributors",
                "participantId": 16,
                "id": 7
            }
        ],
        "longForm": [
            {
                "info": "One of the projects I'm really proud of is my HelloWorld Machine. It says 'Hello World' in ten different languages!",
                "participantId": 16,
                "id": 3
            }
        ],
        "extraInfo": [
            {
                "website": "mywebsite.com",
                "participantId": 16,
                "id": 2
            }
        ],
        "collaborators": [
            {
                "collaborator": "collaborator@tigerhack.org",
                "participantId": 16,
                "id": 16
            }
        ]
    }
}
```

Errors:<br />

| Error        | Source | Cause  |
| ------------ | ------ | ------ |
| InvalidParameterError | `User` | a Participant for the requested user already exists |
| InvalidHeaderError | `Authorization` | the authentication token was invalid or absent |
---

**GET /v1/registration/participant**<br />
Allows requester to retrieve information about their participant registration. Requires requester to have a participant registration.

Headers <br />

| Header        | Description           | Required  |
| ------------- | --------------------- | --------- |
| `Authorization` | a valid authentication token | Yes |

URL Parameters <br />
None

Response
```
{
    "meta": null,
    "data": {
        "firstName": "John",
        "lastName": "Doe",
        "E-mail": "abc56@mail.missouri.edu",
        "age": 19,
        "username": "",
        "password": "",
        "school": "University of Missouri - Columbia",
        "grade/level": "junior",
        "major": "Computer Science",
        "phoneNumber": "12345678910"
        "transportation": "NOT_NEEDED",
        "shirtSize": "M",
        "diet": "NONE",
        "gender": "MALE",
        "professionalInterest": "BOTH",
        "github": "JDoe1234",
        "linkedin": "JDoe5678",
        "hasLightningInterest": false,
        "userId": 1,
        "id": 16,
        "osContributors": [
            {
                "osContributor": "os contributors",
                "participantId": 16,
                "id": 7
            }
        ],
        "longForm": [
            {
                "info": "One of the projects I'm really proud of is my HelloWorld Machine. It says 'Hello World' in ten different languages!",
                "participantId": 16,
                "id": 3
            }
        ],
        "extraInfo": [
            {
                "website": "mywebsite.com",
                "participantId": 16,
                "id": 2
            }
        ],
        "collaborators": [
            {
                "collaborator": "collaborator@tigerhack.org",
                "participantId": 16,
                "id": 16
            }
        ]
    }
}
```

Errors: <br />

| Error        | Source | Cause  |
| ------------ | ------ | ------ |
| InvalidHeaderError | `Authorization` | the authentication token was invalid or absent |
| NotFoundError | N/A | an participant registration doesn't exist for the user |

---

**GET /v1/registration/participant/{:id}**<br />
Retrieves information about an participant. Requires requester to have either the `ADMIN`
or `STAFF` permission. Identical to `GET /v1/registration/participant`.

---

**GET /v1/registration/participant/user{:id}**<br />
Retrieves information about an participant. Requires requester to have a `host` role.

Headers<br />

| Header        | Description           | Required  |
| ------------- | --------------------- | --------- |
| `Authorization` | a valid authentication token | Yes |


URL Parameters<br />

| Parameter        | Description           | Required  |
| ------------- | --------------------- | --------- |
| `id` | the id of the user whose participant information the volunteer wants | Yes |

Response
```
{
  "meta": null,
  "data": {
    "firstName": "John",
    "lastName": "Doe",
    "shirtSize": "M",
    "diet": "NONE"
  }
}
```

Errors:<br />

| Error        | Source | Cause  |
| ------------ | ------ | ------ |
| InvalidHeaderError | `Authorization` | the authentication token was invalid or absent |
| NotFoundError | N/A | an participant registration doesn't exist for the user |

---

**PUT /v1/registration/participant**<br />
Updates an participant registration.

Headers<br />

| Header        | Description           | Required  |
| ------------- | --------------------- | --------- |
| `Authorization` | a valid authentication token | Yes |

URL Parameters<br />
None

Request Parameters<br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `participant` | a JSON object containing the participant Parameters below | Yes |
| `extraInfo` | an array of JSON objects of length at most two, each containing the ExtraInfo parameters below | No |
| `collaborators` | an array of JSON objects of length at most eight, each containing the RequestedCollaborator parameters below | No |

Participant Parameters<br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `firstName` | the user's first name of length 31 or less | Yes |
| `lastName` | the user's last name of length 31 or less | Yes |
| `E-mail` | less than 31 characters | Yes |
| `age` | a number between 13 and 115 | No |
| `username` | less than 15 characters | Yes |
| `password` | less than 15 characters | Yes |
| `school` | the user's school of length 255 or less | Yes |
| `grade/level` | less than 15 characters | Yes |
| `major` | the user's major of length 63 or less | Yes |
| `phoneNumber` | the user's phone number, formatted as a string of length 15 or less | No |
| `transportation` | a string from the following options: ['NOT_NEEDED', 'BUS_REQUESTED', 'IN_STATE', 'OUT_OF_STATE'| Yes |
| `shirtSize` | a string of length 1 from the following options: ['S', 'M', 'L', 'XL'] | Yes |
| `diet` | a string from the following options: ['NONE', 'VEGETARIAN', 'VEGAN', 'GLUTEN_FREE'] | Yes |
| `gender` | a string from the following options: ['MALE', 'FEMALE', 'NON_BINARY', 'OTHER'] | Yes |
| `professionalInterest` | a string from the following options: ['NONE', 'INTERNORPARTTIME', 'FULLTIME', 'BOTH'] | Yes |
| `github` | the user's GitHub handle of length 50 or less | Yes |
| `linkedin` | the user's LinkedIn handle of length 50 or less | Yes |
| `hasLightningInterest` | a boolean indicating whether the user is interested in giving a short talk | No |


ExtraInfo Parameters<br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `website` | the website urls provided by the user of length 255 or less | Yes |
| `id` | the preexisting id of an ExtraInfo to be updated | No|


RequestedCollaborator Parameters<br />

| Parameter        | Description           | Required  |
| ---------------- | --------------------- | --------- |
| `collaborator` | the requested collaborator's email of length 255 or less | Yes |
| `id` | the preexisting id of a collaborator to be updated | No|

Request
```
{
    "participant": {
                "firstName": "John",
                "lastName": "Doe",
                "E-mail": "abc56@mail.missouri.edu",
                "age": 19,
                "username": "",
                "password": "",
                "school": "University of Missouri - Columbia",
                "grade/level": "junior",
                "major": "Computer Science",
                "phoneNumber": "12345678910"
                "transportation": "NOT_NEEDED",
                "shirtSize": "M",
                "diet": "NONE",
                "gender": "MALE",
                "professionalInterest": "BOTH",
                "github": "JDoe1234",
                "linkedin": "JDoe5678",
                "hasLightningInterest": false,
    },
    "collaborators": [
        {
                    "collaborator": "collaborator@tigerhack.org"
        }
    ],
    "longForm": [
        {
                    "info": "One of the projects I'm really proud of is my HelloWorld Machine. It says 'Hello World' in ten different languages!"
        }
    ],
    "extraInfo": [
        {
                    "website": "mywebsite.com"
        }
    ],
    "osContributors": [
        {
                    "osContributor": "os contributors"
        }
    ]
}
```

Response
```
{
    "meta": null,
    "data": {
        "firstName": "John",
        "lastName": "Doe",
        "E-mail": "abc56@mail.missouri.edu",
        "age": 19,
        "username": "",
        "password": "",
        "school": "University of Missouri - Columbia",
        "grade/level": "junior",
        "major": "Computer Science",
        "phoneNumber": "12345678910"
        "transportation": "NOT_NEEDED",
        "shirtSize": "M",
        "diet": "NONE",
        "gender": "MALE",
        "professionalInterest": "BOTH",
        "github": "JDoe1234",
        "linkedin": "JDoe5678",
        "hasLightningInterest": false,
        "userId": 1,
        "id": 16,
        "osContributors": [
            {
                "osContributor": "os contributors",
                "participantId": 16,
                "id": 7
            }
        ],
        "longForm": [
            {
                "info": "One of the projects I'm really proud of is my HelloWorld Machine. It says 'Hello World' in ten different languages!",
                "participantId": 16,
                "id": 3
            }
        ],
        "extraInfo": [
            {
                "website": "mywebsite.com",
                "participantId": 16,
                "id": 2
            }
        ],
        "collaborators": [
            {
                "collaborator": "collaborator@tigerhack.org",
                "participantId": 16,
                "id": 16
            }
        ]
    }
}
```

Errors:<br />

| Error        | Source | Cause  |
| ------------ | ------ | ------ |
| NotFoundError | `id` | an id for a given related object was not found |
| InvalidHeaderError | `Authorization` | the authentication token was invalid or absent |

---

**PUT /v1/registration/participant/{:id}** <br />
Updates an participant registration. Requires requester to have either the ADMIN or STAFF permission. Identical to
`PUT /v1/registration/participant`.

**DELETE /v1/registration/participant**<br />
Delete an participant registration.

**DELETE /v1/registration/participant/{:id}** <br />
Delete an participant registration. Requires requester to have either the ADMIN or STAFF permission. Identical to
`DELETE /v1/registration/participant`.


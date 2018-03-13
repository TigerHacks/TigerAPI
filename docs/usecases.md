# Use Cases

## Rough use cases

* Authentication
* Administration management
* Registration/Applications
* Check in
* Participant/meal tracking
* Schedule/Events
* Notifications
* Sponsors
* Mailing list
* Travel reimbursement
* Prizes

## Functional Use Cases

### Authentication

* Administrators and participants should be able to authenticate with an email
  and password
* Participants should be able to authenticate with GitHub OAuth

## Administration management

* Administrators should be able to add new administrators
* Administrators should be able to remove other administrators
* Administrators should be able to fetch a list of all administrators

### Registration/Applications

* Participants should be able to apply
* Participants should be able to update/modify applications
* Participants should be able to check application status
* Participants should be able to RSVP
* Administrators should be able to fetch all applications
* Administrators should be able to approve/decline applications
* System should be able to verify account/email
* Sponsors/Mentors should be able to register the mentors they intend to send
  with email

### Check-in

* Administrators should be able to check participants in
* Administrators should be able to check sponsor mentors in
* Administrators should be able to check who is checked in

### Participant/meal tracking

* Administrators should be able to get participant statistics
* Administrators should be able to track meals

### Schedule/Events

* Participants should be able to check schedule
* Administrators should be able to add events and modify schedule

### Announcements/Notifications
* Participants should be able to fetch announcements
* Admins should be able to create/modify/delete announcements

### Sponsors

* Sponsors/Mentors should be able to register with name, skills, a form of
  contact (slack), and availability on campus
* Sponsors should be able to add a website link to their company's website, API,
  or a link to internship opportunities - just one link option

### Mailing List

* Administrators should be able to send mass emails to certain participants,
  e.g. only approved applicants
* System should be able to mail participants, e.g. application approval, account
  verification
* System should be able to mail administrators on specified admin changes
* Send mail to sponsor or mentor contacts with updates

### Travel Reimbursement

* Participants should be able to register for travel reimbursement
* Administrators should be able to fetch all travel reimbursement forms
* Administrators should be able to approve/decline travel reimbursement

### Prizes

* Administrators can add prizes and a description of how to obtain prize
* Administrators can manage by add/edit/delete Prizes
* Administrators can set Prizes to beginner or standard

## Nonfunctional Use Cases

* Should be secure (HTTPS)
* Should be cross-platform (Web, iOS, Android)
* Should be easy to maintain, extend, and deploy
* Should be well documented

## Story/Epic Ideas

* Create a use-case diagram
* Write use case descriptions
* Write README.md
* Design the application
* Design the REST API endpoints (Epic)
* Design a normalized database schema (Epic)
  * Design a table for participants
  * Design a table for administrators
  * Design a table for applications
  * Design a table for sponsor info
  * Design a table for authorization/api keys(?)
  * Design a table for notifications
  * Design a table for the schedule
  * Design a table for mentors
* Implement REST API (Epic)

## Other Notes

Implementation details that are probably important.

* The [HackIllinois] api is a really good resource for ideas.
* Because of CORS, we shouldn't/can't use cookies for authorization. We will
  probably need to use some kind of authorization/api key.

[HackIllinois]: https://github.com/HackIllinois/api

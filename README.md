# radius

## Github open issues basic web app.

## Input  
Github repo URL

Example - https://github.com/Exiv2/exiv2

## Output 
[1] Total open issues count

[2] Open issues created in last 24 hours

[3] Open issues created before 24 hours and less than 7 days

[4] Open issues created before 7 days

Sample output
![alt text](https://github.com/maheshmhegade/radius/blob/master/demo.png)

## Tech
### Front end - Basic Html page hosted on apache2 server
### Backend - Python flask framework for rest interface

## Design
- Html makes async call to flask rest api, provides github repo url in the request body.
- Backend python flask, makes 3 github API calls
	- To get all open issues count
	- To get open issues created in last 24 hours
	- To get open issues created in last 7 days
- These 3 are sufficient to get the required data.
- Flask service returns the response in json, html displays the data.


## Suggested improvements.
- UI could be improved a lot better, to handle error cases for invalid URLs etc
- Autocomplete could be implemented for all repos of particular github account.
- Request/response design of flask backend could be improved to handle additional type of queries.
- Appropriate error code should be returned in case of error/exception.
- Some data couild be cached, for example for given problem statement, open issues more than 7 days could be cached for another 7 days, which wont change.
- Links to the recent actual issues could be provided.

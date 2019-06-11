# radius

Github open issues basic web app.
Input - Github repo URL
Outut - 
[1] Total open issues count
[2] Open issues created in last 24 hours
[3] Open issues created before 24 hours and before 7 days

Front end- Basic Html page hosted on apache2 server
Backend - Python flask framework for rest interface

Design
- Html makes async call to flask rest api, provides github repo url in the request body.
- Backend python flask, makes 3 github API calls
	[1] To get all open issues count
	[2] To get open issues created in last 24 hours
	[3] To get open issues created in last 7 days
- These 3 are sufficient to get the required data.
- Flask service returns the response in json, html displays te data.
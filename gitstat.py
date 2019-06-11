# @author - mailto:maheshmhegade@gmail.com
from flask import Flask, jsonify
from flask import request
import requests
import json
from datetime import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)

## Enabled CORS, since i am running both flask and apache2 on same server
cors = CORS(app)

## Method to serve the request
def getIssuesCount(issuesRequest):

	## taking issue state also as input, so that we can extend the code for close request as well
	issuestatus = issuesRequest['status']
	
	repourl = issuesRequest['repourl']
	spliturl = repourl.split('/')
	org = spliturl[3]
	repo = spliturl[4] 

	url = 'https://api.github.com/search/issues?q=repo:' + org + '/' + repo + '+type:issue+state:' + issuestatus 
	
	## if since is not provided, it gets all open requests.
	if 'since' in issuesRequest:
		created = issuesRequest['since']
		url += ('+created:>' + created)
	## calls github API
	response = requests.get(url)
	return json.loads(response.content)['total_count']

@app.route('/issues/count', methods=['POST'])
def issues():
	inputRequest = json.loads(request.data)
	repourl = inputRequest['repourl']
	
	## Github API requires timestamp is a perticular format
	last24hourTimeStamp = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%dT%H:%M:%S')
	last7DaysTimeStamp = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S')
	issuesRequest = {'repourl': repourl, 'status': 'open'}
	totalIssuesCount = getIssuesCount(issuesRequest)

	issuesRequest['since'] = last24hourTimeStamp
	last24HourIssuesCount = getIssuesCount(issuesRequest)

	issuesRequest['since'] = last7DaysTimeStamp
	last7DaysIssuesCount = getIssuesCount(issuesRequest)

	return jsonify({'total': (totalIssuesCount), 'last24Hour' : int(last24HourIssuesCount), 'last7DaysExcludingLast24Hour': (int(last7DaysIssuesCount)-int(last24HourIssuesCount)), 'morethan7Days': (int(totalIssuesCount) - int(last7DaysIssuesCount)) })

if __name__ == '__main__':
	app.run(host='0.0.0.0')

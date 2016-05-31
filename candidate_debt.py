# Written by Jonathan Saewitz, released May 30th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import csv, plotly.plotly as plotly, plotly.graph_objs as go, requests
from bs4 import BeautifulSoup

candidates=[]

with open('presidential_candidates.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next() #skip the headers row
	c=0
	for row in reader: #loop through the candidates
		c+=1
		print c
		c_id=row[15] #row[15] is the candidate's FEC id
		html=requests.get('https://beta.fec.gov/data/candidate/' + c_id).text #get the candidate's FEC page
		b=BeautifulSoup(html, 'html.parser')
		if len(b.find_all(class_='t-big-data'))==0: #if this class isn't found on the candidate's FEC page,
													#the candidate raised $0
			debt=0.0
		else:
			debt=float(b.find_all(class_="t-big-data")[3].text.strip().replace("$", "").replace(",", ""))
			#class "t-big-data" contains the money data
			#the 3rd element contains the total debt
			#.text gets only the text (i.e. amount raised)
			#.strip() removes all whitespace
			#.replace("$", "") removes the dollar sign	
			#.replace(",", "") removes all commas
			#we should be left with the total amount raised in the form 0.00
			name=row[14] #row[14] is the candidate's name
			if debt>0:
				candidates.append({'name': name, 'amount': debt})

candidates=sorted(candidates, key=lambda k: k['amount']) #sort the candidates by amount raised	

trace=go.Bar(
	x=[candidate['name'] for candidate in candidates],
	y=[candidate['amount'] for candidate in candidates]
)

layout=go.Layout(
	title="US Presidential Candidates by Debt",
	xaxis=dict(
		title="Candidate",
	),
	yaxis=dict(
		title="Campaign debt ($)",
	)
)

data=[trace]
fig=dict(data=data, layout=layout)
plotly.plot(fig)
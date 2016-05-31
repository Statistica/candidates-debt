# Written by Jonathan Saewitz, released May 30th, 2016 for Statisti.ca
# Released under the MIT License (https://opensource.org/licenses/MIT)

import csv, numpy

amount=0
amounts=[]

with open('campaigns_and_debt.csv', 'r') as f:
	reader=csv.reader(f)
	reader.next() #skip the header row
	for row in reader: #loop through each row (candidate)
		amount+=float(row[1]) #row[1] is the current candidate's debt
		amounts.append(float(row[1]))

print "# of candidates:", "{:,}".format(len(amounts))
print "Total amount raised: $", "{:,}".format(amount)
print "Average amount raised: $", "{:,}".format(amount/len(amounts))

print "Median amount raised: $", "{:,}".format(numpy.median(amounts))

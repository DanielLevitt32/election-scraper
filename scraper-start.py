import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/PickaRace.aspx')

# Fill out the top form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
br.submit('ctl00$MainContent$btnElectionType')

# Fill out the bottom form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboRaces'] = ['750003269']
br.submit('ctl00$MainContent$btnCountyChange')

# Get HTML
html = br.response().read()

soup = BeautifulSoup(html, "html.parser")
table = soup.find('br', attrs ={'option value': '750003566', 'option value': '750003269'})

for row in table.find_all('tr'):
	for cell in row.find_all('tr'):
		list_of_cells.append(text)
		list_of_rows_append(list_of_cells)
		print cell.text
########## YOUR CODE HERE ##########
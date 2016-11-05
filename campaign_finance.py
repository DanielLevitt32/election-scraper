import json, requests

#PRO PUBLICA CAMPAIGN FINANCE API#
API_KEY = "P7kuyuM7XB37elOJ6da786cYoYjncGa98Mdod8QZ"

#THE URL OF THE API#

url = "https://api.propublica.org/campaign-finance/v1/2016/president/totals"
#https://api.propublica.org/campaign-finance/v1/2016/independent_expenditures.json&#039
r = requests.get(url, headers={'X-API-Key': API_KEY})

response_data = r.content

data = json.loads(response_data)

#print data

#digging into results, and then targeting the first item in the dictionary
print data['results'][0]['total_receipts']

#If we wanted to target a specific thing/string
#print data['cycle']

#python campaign_finance.py
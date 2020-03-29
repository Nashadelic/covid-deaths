import json
import requests


from matplotlib import pyplot

url = "https://pomber.github.io/covid19/timeseries.json"
r = requests.get(url=url)
data = r.json()

cleaned=[]
row=[]
counter=0
first_date = None

for country in data:
    row.append(country)
    for entry in data[country]:
        if entry["deaths"] > 5:
            row.append(entry['deaths'])
    else:
        if len(row) > 2:
            cleaned.append(row)
        row = []
                       
import csv
with open('death_rate.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["Country"] + [f"Day {n}" for n in range(90)])
    spamwriter.writerows(cleaned)



import json

cleaned=[]
row=[]

# Json file is from https://pomber.github.io/covid19/timeseries.json
with open('timeseries.json') as json_file:
    data = json.load(json_file)
    for country in data:
        row.append(country)
        for entry in data[country]:
            if entry["confirmed"] != 0:
                row.append(entry['deaths'])
        else:
            cleaned.append(row)
            row = []
                       
import csv
with open('death_rate.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["Country"] + [f"Day {n}" for n in range(90)])
    spamwriter.writerows(cleaned)



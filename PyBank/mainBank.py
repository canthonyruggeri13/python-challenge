import os, csv

# Read in budget_data.csv
data = []
csv_path = os.path.join(".", "budget_data.csv")
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None) #skip header
    for row in csv_reader:
        data.append({"Date": row[0], "Profit/Loss": float(row[1]), "PL Delta": 0.0})

# Add Profit/Loss Delta column
# (Assumes data was sorted by date in csv)
prev_profitloss = data[0]["Profit/Loss"]
for i in range(1, len(data)):
    profitloss = data[i]["Profit/Loss"]
    data[i]["PL Delta"] = profitloss - prev_profitloss
    prev_profitloss = profitloss


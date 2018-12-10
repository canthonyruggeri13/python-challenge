import os, csv

# Read in budget_data.csv
bankData = []
budgetCsv = os.path.join(".", "budget_data.csv")
with open(budgetCsv) as csvFile:
    impbudgCSV = csv.reader(csvFile, delimiter=",")
    next(impbudgCSV, None)
    for row in impbudgCSV:
        bankData.append({"Date": row[0], "Profit/Losses": float(row[1]), "Net Pr/Lo": 0.0})

# Add Profit/Losses column
pploss = bankData[0]["Profit/Losses"]
for i in range(1, len(bankData)):
    profLoss = bankData[i]["Profit/Losses"]
    bankData[i]["Net Pr/Lo"] = profLoss - pploss
    pploss = profLoss

# Generate summary statistics
count = len(bankData)
sumProfLoss = 0.0
sumNetPL = 0.0
mxC = {"Date": "", "Net Pr/Lo": 0.0}
MNc = {"Date": "", "Net Pr/Lo": 0.0}
for row in bankData:
    sumProfLoss += row["Profit/Losses"]
    sumNetPL += row["Net Pr/Lo"]
    if row["Net Pr/Lo"] > mxC["Net Pr/Lo"]:
        mxC["Date"] = row["Date"]
        mxC["Net Pr/Lo"] = row["Net Pr/Lo"]
    if row["Net Pr/Lo"] < MNc["Net Pr/Lo"]:
        MNc["Date"] = row["Date"]
        MNc["Net Pr/Lo"] = row["Net Pr/Lo"]
avNet = sumNetPL / (count-1)


# Print data summary
print("Financial Analysis:")
print("----------------------------")
print(f'Total Months: {count}')
print(f'Total: $ {sumProfLoss}')
print(f'Average Change: $ {avNet}')
print(f'Greatest Increase in Profits: {mxC["Date"]} ($ {mxC["Net Pr/L"]})')
print(f'Greatest Decrease in Profits: {MNc["Date"]} ($ {MNc["Net Pr/L"]})')

# Write data summary to file
file = open("output.txt", "w")
file.write("Financial Analysis:\n")
file.write("----------------------------\n")
file.write(f'Total Months: {count}\n')
file.write(f'Total: $ {sumProfLoss}\n')
file.write(f'Average Change: $ {avNet}\n')
file.write(f'Greatest Increase in Profits: {mxC["Date"]} ($ {mxC["Net Pr/L"]})\n')
file.write(f'Greatest Decrease in Profits: {MNc["Date"]} ($ {MNc["Net Pr/L"]})\n')
file.close()



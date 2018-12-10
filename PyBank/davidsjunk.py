davids junk     



# Generate summary statistics
count = len(data)
sum_profitloss = 0.0
sum_pldelta = 0.0
max_change = {"Date": "", "PL Delta": 0.0}
min_change = {"Date": "", "PL Delta": 0.0}
for row in data:
    sum_profitloss += row["Profit/Loss"]
    sum_pldelta += row["PL Delta"]
    if row["PL Delta"] > max_change["PL Delta"]:
        max_change["Date"] = row["Date"]
        max_change["PL Delta"] = row["PL Delta"]
    if row["PL Delta"] < min_change["PL Delta"]:
        min_change["Date"] = row["Date"]
        min_change["PL Delta"] = row["PL Delta"]
average_pldelta = sum_pldelta / (count-1) # There is one fewer delta than there are months
 
# Print data summary
print("Financial Analysis:")
print("----------------------------")
print(f'Total Months: {count}')
print(f'Total: $ {sum_profitloss}')
print(f'Average Change: $ {average_pldelta}')
print(f'Greatest Increase in Profits: {max_change["Date"]} ($ {max_change["PL Delta"]})')
print(f'Greatest Decrease in Profits: {min_change["Date"]} ($ {min_change["PL Delta"]})')

# Write data summary to file
file = open("output.txt", "w")
file.write("Financial Analysis:\n")
file.write("----------------------------\n")
file.write(f'Total Months: {count}\n')
file.write(f'Total: $ {sum_profitloss}\n')
file.write(f'Average Change: $ {average_pldelta}\n')
file.write(f'Greatest Increase in Profits: {max_change["Date"]} ($ {max_change["PL Delta"]})\n')
file.write(f'Greatest Decrease in Profits: {min_change["Date"]} ($ {min_change["PL Delta"]})\n')
file.close()





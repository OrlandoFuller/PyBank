#The total number of months included in the dataset.
#The net total amount of Profit/Losses over the entire period.
#The average of the changes in Profit/Losses over the entire period.
#The greatest increase in profits (date and amount) over the entire period.
#The greatest decrease in losses (date and amount) over the entire period.

#imports
import pandas as pd

# reading csv
bd = pd.read_csv('budget_data.csv')

# calculation
total_mths = bd['Profit/Losses'].count() # calculate total mths
total = bd['Profit/Losses'].sum() # calculate total pnl
avg_chng = round(bd['Profit/Losses'].diff().mean(),2) # calculate average change
greatest_increase = round(bd['Profit/Losses'].diff().max()) # calculate max increase
greatest_decrease = round(bd['Profit/Losses'].diff().min()) # calculate max decrease

# increase / decrease loop
diff_lst = bd['Profit/Losses'].diff()
f1 = diff_lst == greatest_increase
greatest_increase_index = bd[f1]['Date'].index
for i in greatest_increase_index:
    greatest_increase_date = bd[f1]['Date'][i]
diff_lst = bd['Profit/Losses'].diff()
f2 = diff_lst == greatest_decrease
greatest_decrease_index = bd[f2]['Date'].index
for i in greatest_decrease_index:
    greatest_decrease_date = bd[f2]['Date'][i]

# Print statments
print(f'Financial Analysis')
print(f'-'*30)
print(f'Total Months: {total_mths}')
print(f'Total: ${total}')
print(f'Average  Change: ${avg_chng}')
print(f'Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})')
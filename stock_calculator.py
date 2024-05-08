#Formatting values
dashes = '--------------------------------------------------'
asterisks = '**************************************************'

#Constants
COMMISSION_0 = 0
COMMISSION_50 = 50
COMMISSION_100 = 100
MIN_THRESHOLD = 1000
MAX_THRESHOLD = 2000

#Welcome message to user
print(dashes)
print('*** Welcome to Stock Value Calculator Program! ***')
print(dashes)

#Getting input values
stock_name = (input('Enter stock\'s name: '))

purchased_shares = int(input('Enter the total number of purchased shares: '))
if purchased_shares <= 0:
    print('Error: Number of purchased shares should be > 0')
    exit()

paid_per_purchase = float(input('Enter the dollar amount paid per a purchased share: '))
if paid_per_purchase <= 0:
    print('Error: the purchase amount should be > 0')
    exit() 

sold_shares = int(input('Enter the total number of sold shares: '))
if sold_shares <= 0 or sold_shares > purchased_shares:
    print ('Error: Number of sold shares should be > 0 and must be <= number of purchased shares')
    exit()

paid_per_sold_shares = float(input('Enter the dollar amount paid per a sold share: '))
if paid_per_sold_shares <= 0:
    print ('Error: The sold amount should be > 0 ')
    exit()

#Conditions - Commission
if purchased_shares < MIN_THRESHOLD:
    purchase_commission = COMMISSION_100
else:
    purchase_commission = COMMISSION_0

if sold_shares < MIN_THRESHOLD:
    sale_commission = COMMISSION_100
elif sold_shares < MAX_THRESHOLD:
    sale_commission = COMMISSION_50
else:
    sale_commission = COMMISSION_0

#Calculations for Total Purchase Amount & Total Sold Amount
purchase_amount = purchased_shares * paid_per_purchase
sold_amount = sold_shares * paid_per_sold_shares

#Condition for Profit
if sold_shares >= purchased_shares:
    profit = sold_amount - purchase_amount - purchase_commission - sale_commission
else:
    profit = sold_amount - (sold_shares * paid_per_purchase) - purchase_commission - sale_commission

#Results - Purchasing Report
print(asterisks)
print(f"{'Purchasing Report' : ^50}")
print(asterisks)
print('Stock Name: ', stock_name)
print(f'Total Purchase Amount: ${purchase_amount:.1f}')
print('Purchase Commission: $' + str(purchase_commission))

#Results - Selling Report
print(asterisks)
print(f"{'Selling Report' : ^50}")
print(asterisks)
print(f'Total Sold Amount: ${sold_amount:.1f}')
print('Sold Commission: $' + str(sale_commission))
print(asterisks)

#Decimal Formatting
format_profit = '{:.1f}'.format(profit)

#Results - Profit
if profit > 0:
    print('Congratulation, Total Profit: $' + format_profit)
elif profit == 0:
    print('No Profit or Loss, Total Profit: $' + format_profit)
else:
    print ('Good Luck Next Time, You Lost: $' + format_profit)
print(asterisks)

#End
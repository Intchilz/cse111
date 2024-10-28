#Import the date from the datetime module
import datetime

#Here I collect the date from the system
today = datetime.date.today()

#Save today's date in the variable week_day
week_day = today.weekday()

#Collect the subtotal from the user
subtotal = float(input('Please enter the subtotal: '))
sales_tax = 0.06 * subtotal
total = subtotal + sales_tax

if  week_day == 1 or week_day == 2 and subtotal >= 50:
    sub = subtotal * 0.10
    sub1 = subtotal - sub
    s_tax = sub1 * 0.06
    final = s_tax + sub1
    print(f'Discount amount: {round(sub, 2)}')
    print(f'Sales tax amount: {round(s_tax, 2)}')
    print(f'Total: {round(final, 2)}')

elif subtotal < 50:
    compute = 50 - subtotal
    print(f'Hey, you are only ${round(compute, 2)} away from a discount')
    print('keep shopping!')
    
else:  
    print(f'Sales tax amount: {round(sales_tax, 2)}')
    print(f'Total: {round(total, 2)}')
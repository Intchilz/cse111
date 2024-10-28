#Import the math and datetime module
import math
import datetime

#Collect input from the user: Width, Aspect Ratio and diameter of the tyre.
width = int(input('Enter width of tire in mm (ex 205): '))
aspect_ratio = int(input('Enter aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter diameter of the wheel in inches (ex 15): '))

#Perform calculations to determine the volume.
calc1 = width * aspect_ratio + 2540 * diameter
calc2 = math.pi * width**2 * aspect_ratio
calcln2 = calc1 * calc2
calculate = calcln2 / 10000000000
answer = round(calculate, 2)

#If statements to show prices for four different tyre sizes.
if width == 205 and aspect_ratio == 70 and diameter == 15:
    print('')
    print('Price for your desired tyre is $63.84')
    
elif width == 215 and aspect_ratio == 80 and diameter == 15:
    print('')
    print('Price for your desired tyre is $75.19')
    
elif width == 245 and aspect_ratio == 75 and diameter == 15:
    print('')
    print('Price for your desired tyre is $80.19')
    
elif width == 255 and aspect_ratio == 70 and diameter == 15:
    print('')
    print('Price for your desired tyre is $90.00')
    
#store the desired sizes and date in a file called volumes.txt
with open('volumes.txt', 'a') as volume:
    width = str(width)
    aspect_ratio = str(aspect_ratio)
    diameter = str(diameter)
    answer = str(answer)
    
    today = volume.write(datetime.date.today().strftime('%Y-%m-%d')+',')
    w = volume.write(' '+width+',')
    ar = volume.write(' '+aspect_ratio+',')
    d = volume.write(' '+diameter+',')
    v = volume.write(' '+answer+'\n')
    
#Display the calculated volume.       
print(f'\nThe approximate volume is {answer} liters')

#prompt the user to know if they'd like to buy the tyre with the entered dimensions.
buy_tyre = input('\nPurchase tyres with the dimensions entered(yes or no with small letters)? ' )

#If statements to perform a task depending on the choice of the user.
#Should the user choose to purchase, they share their number
#and it gets stored in a file called volumes.txt.
#If the user chooses not to buy, the message
#'Okay, bye' displays and the program stops running.
if buy_tyre == 'yes':
    number = input('Enter your phone number: ')
    print('')
    print('Contact received, we will be in touch shortly.')
    with open('volumes.txt', 'a') as volume:
        number = volume.write(number)
elif buy_tyre == 'no':
    print('Okay, bye!')
else:
    print('You can only answer yes or no with small letters')
# code is correct
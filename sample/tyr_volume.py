import math
import datetime

today = datetime.date.today()


width = int(input('Enter width of tire in mm (ex 205): '))
aspect_ratio = int(input('Enter aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter diameter of the wheel in inches (ex 15): '))

calc1 = width * aspect_ratio + 2540 * diameter
calc2 = math.pi * width**2 * aspect_ratio
calcln2 = calc1 * calc2
calculate = calcln2 / 10000000000
answer = round(calculate, 2)


print(f'The approximate volume is {answer} liters')
# code is correct
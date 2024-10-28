"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = float(input('Please enter your age: '))
subtract = 220 - age
percent1 = subtract * 0.65
percent2 = subtract * 0.85

convert1 = int(percent1)
convert2 = int(percent2)

print("When you exercise to strengthen your heart, you should")
print(f'keep your heart rate between {convert1} and {convert2} beats per minute.')
# Assignment is correct
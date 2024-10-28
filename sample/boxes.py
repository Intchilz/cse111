'''In our modern world economy, many items
   are manufactured in large factories, then packed
   in boxes and shipped to distribution centers
   and retail stores. A common question for
   employees who pack items is “How many
   boxes do we need?”'''

import math

items = int(input('Enter the number of items: '))
number = int(input('Enter the number of items per box: '))

calculate = math.ceil(items/number)

print(f"For {items} items, packing {number}"
      f" items in each box, you will need {calculate} boxes.")
#assignment is correct
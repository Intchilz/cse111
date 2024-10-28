def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
  fruit_list.reverse()
  print(f'Reversed: {fruit_list}')
  fruit_list.append('orange')
  print(fruit_list)
  fruit_list.insert(1, 'cherry')
  print(fruit_list)
  fruit_list.pop(3)
  print(fruit_list)
  popped = fruit_list.pop()
  print(popped)
  print(fruit_list)
  fruit_list.sort()
  sorted = []
  for fruit in fruit_list:
      sorted.append(fruit)
  print(f'Sorted: {sorted}')
  fruit_list.clear()
  print(fruit_list)
  
main()
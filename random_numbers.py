import random

def main():
    
    numbers = [16.2, 75.1, 52.3]
    
    print(f'Numbers {numbers}')
    
    append_random_numbers(numbers)
    
    print(f'Numbers {numbers}')
    
    append_random_numbers(numbers, 3)
    
    print(f'Numbers {numbers}')
    
    words= []
    
    append_random_words(words)
    print(f'Words {words}')
    
    append_random_words(words,5)
    print(f'Words {words}')
    
def append_random_numbers(numbers_list,quantity=1):
    
    for numbers in range(quantity):
        random_number = random.uniform(4.1, 67.2)
        numbers_list.append(round(random_number,1))
        
def append_random_words(words_list, quantity=1):
    
    random_words_list = ['boys', 'ladies', 'girls', 'men',
        'dog', 'cat', 'mouse', 'gorilla', 'lion', 'chipmunk',
        'chicken','beef', 'pork chops', 'fish fillets',
        'rice', 'pizza', 'burger', 'ohh am hungry now!'
    ]
    
    for _ in range(quantity):
        random_words = random.choice(random_words_list)
        words_list.append(random_words)  


if __name__ == "__main__":
    main()
    
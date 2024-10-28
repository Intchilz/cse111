
def main():
    
    added = add_to_list()
    specific = access_list_item()
    
    print("Here is the list of names you requested;")
    print(added)
    
    print(' ')
    print(f'The list item matching your index number is {specific}')
    
def actual_list():
    
    my_list = ['Louis Chilumba', 'Adams Kabosha', 'Joseph Nthani', 'Sarah Saidi']
    
    return my_list

def add_to_list():
    
    the_list = actual_list()
    
    user = input('Enter list item (Name): ')
    
    the_list.append(user)
    
    return the_list

def access_list_item():
    
    the_list = add_to_list()
    
    user_index = int(input("Enter index number, I will show you the list item (1-4): "))
    
    return the_list[user_index]

main()
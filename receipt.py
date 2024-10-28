'''
Most customers love to suggest services
/products to businesses. I added a two
functions (add_file and services).
The add_file function adds the desired
product the customer desires to our 
products.csv file. The services function
prompts the user if they'd like to 
suggest a product. It then calls the 
add_file function and passes in the 
products.csv file and the product
the customer entered. The name of the 
product is printed on the receipt 
so that the customer can remember 
to check in with our store when they 
wish to purchase that product.
'''


import csv
from datetime import datetime

products_file = 'products.csv'
SALES_TAX_RATE = 0.06

def main():
    
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    try:
        products_dict = read_dictionary(products_file, I_NUMBER_INDEX)
        print('All products')
        print(products_dict)
        
        subtotal = 0
    
        with open('request.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            # Skip the header line
            next(csv_reader)
        
            # Print the requested items
            print("\nInkom Emporium")
            for row in csv_reader:
                product_number = row[0]  # Product number in the first column
                requested_quantity = int(row[NAME_INDEX])  # Quantity in the second column
            
                # Check if the product number exists in the dictionary
                #product_number in products_dict:
                #if product_number in products_dict:
                product_name = products_dict[product_number][1]  # Product name
                product_price = products_dict[product_number][2]  # Product price
        
                # Print product details
                print(f"{product_name}: {requested_quantity} @ {product_price}")
                price = float(product_price)
                subtotal += requested_quantity * price 
                sales_tax = subtotal * SALES_TAX_RATE
                total = subtotal + sales_tax               
        sum_ordered_items('request.csv')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sales Tax: {sales_tax:.2f}')
        print(f'Total: {total:.2f}')
        print(f'Thank you for shopping at the Inkom Emporium.')
        get_date_time()
        services()
    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)
    except KeyError:
        print(f"Error: unknown product ID in the request.csv file\n'{product_number}'")
   
def read_dictionary(filename, key_column_index):
    
    """Read the contents of a CSV file into a compound
        dictionary and return the dictionary.
        Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
        to use as the keys in the dictionary.
        Return: a compound dictionary that contains
        the contents of the CSV file.
    """

  
    compound_dict = {}
    
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.

                key = row_list[key_column_index]
                # Store the data from the current
                # row into the dictionary.
                compound_dict[key] = row_list
    # Return the dictionary.
    return compound_dict

def get_date_time():
    
    current_date_and_time = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    
    print(current_date_and_time)
    

def sum_ordered_items(file_path):
    total_quantity = 0

    with open(file_path, mode='r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row if it exists
        
        for row in reader:
            if len(row) == 2:  # Ensure there are two columns
                try:
                    quantity = int(row[1])  # Convert quantity to integer
                    total_quantity += quantity
                except ValueError:
                    print(f"Invalid quantity: {row[1]} in row {row}")

    print(f'Number of items: {total_quantity}')
    
def add_file(file_name, service):
    # Create an empty list.
    service_list = []
    # Add the service to the empty list.
    service_list.append(service)
    # Open the csv file and add the item from the list at the 
    # end of the file.
    with open(file_name, 'at') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(service_list)
        
    return writer

def services():
    # Prompt the user if they wish to suggest more services.
    service = input('Would you like to suggest additional services? ')
    # Add conditionals to prompt the user for the product
    # they wish to add.
    if service == 'yes':
        product = input('What product would you like us to provide? ')
        add_file(products_file, product)
        print('')
        # Show the name of the product to the user.
        print(f'Thank you, we have added {product} on the list of products.')
    # Add an else statement to print when the user enters anything
    # other than yes.
    else:
        print('Thank you. Call again.')
    

if __name__ == '__main__':
    main()
import csv

def main():
    
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    
    products_dict = read_dictionary('products.csv', I_NUMBER_INDEX)
    print('All products')
    print(products_dict)
    
    with open('request.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        # Skip the header line
        next(csv_reader)
        
        # Print the requested items
        print("\nRequested Items")
        for row in csv_reader:
            product_number = row[0]  # Product number in the first column
            requested_quantity = int(row[NAME_INDEX])  # Quantity in the second column
            
            # Check if the product number exists in the dictionary
            if product_number in products_dict:
                product_name = products_dict[product_number][1]  # Product name
                product_price = products_dict[product_number][2]  # Product price
                
                # Print product details
                print(f"{product_name}: {requested_quantity} @ {product_price}")
    
    
    
    
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
  
  
    
    
if __name__ == '__main__':
    main()
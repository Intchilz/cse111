from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def make_periodic_table():
    """Create and return a dictionary representing the periodic table."""
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794],
        "C": ["Carbon", 12.0107],
        "O": ["Oxygen", 15.9994],
        "N": ["Nitrogen", 14.0067],
        "S": ["Sulfur", 32.065],
        "P": ["Phosphorus", 30.973761],
        "Cl": ["Chlorine", 35.453],
        "Ar": ["Argon", 39.948],
        "K": ["Potassium", 39.0983],
        "Ca": ["Calcium", 40.078],
        # Add more elements as needed
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the elements listed in symbol_quantity_list."""
    total_molar_mass = 0
    for symbol_quantity in symbol_quantity_list:
        symbol = symbol_quantity[SYMBOL_INDEX]
        quantity = symbol_quantity[QUANTITY_INDEX]
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass

def main():
    # Get a chemical formula for a molecule from the user.
    formula = input("Enter the molecular formula of the sample: ")
    # Get the mass of a chemical sample in grams from the user.
    sample_mass = float(input("Enter the mass in grams of the sample: "))
    # Call the make_periodic_table function and store the periodic table in a variable.
    periodic_table = make_periodic_table()
    # Call the parse_formula function to convert the chemical formula given by the user.
    symbol_quantity_list = parse_formula(formula, periodic_table)
    # Call the compute_molar_mass function to compute the molar mass of the molecule.
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
    # Compute the number of moles in the sample.
    number_of_moles = sample_mass / molar_mass
    # Print the molar mass and the number of moles.
    print(f"{molar_mass} grams/mole")
    print(f"{number_of_moles} moles")

if __name__ == "__main__":
    main()
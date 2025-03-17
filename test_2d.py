import galois

# Define GF(2^6) with power representation
GF = galois.GF(2**15, repr="power")

# Get the representation table as a string and save it to a file
repr_table = GF.repr_table(sort="power")
with open("GF_table.txt", "w") as f:
    f.write(repr_table)

print("GF(2^6) table saved as 'GF_table.txt'.")

# Read the table from the file
def read_gf_table():
    with open("GF_table.txt", "r") as f:
        lines = f.readlines()
    return lines

# Function to extract power exponent given an integer value
def get_power_by_integer(value, lines):
    for line in lines[3:]:  # Skip headers
        parts = line.strip().split()  # Split into columns
        if parts and parts[-1].isdigit():  # Ensure last column is an integer
            int_value = int(parts[-1])
            if int_value == value:
                return parts[0]  # Return the power representation
    return "Not found"  # If not found

# Load the table
lines = read_gf_table()

# Get user input for power values
power1 = int(input("Enter first power value (e.g., 9 for x^9): "))
power2 = int(input("Enter second power value (e.g., 7 for x^7): "))

# Get primitive element α
alpha = GF.primitive_element

# Convert power values to GF elements
elem1 = alpha ** power1
elem2 = alpha ** power2

# Perform GF computations
sum_result = elem1 + elem2  # GF(2^6) addition
product_result = elem1 * elem2  # GF(2^6) multiplication
inverse_elem1 = elem1 ** -1 if elem1 != 0 else "No inverse (zero element)"
inverse_elem2 = elem2 ** -1 if elem2 != 0 else "No inverse (zero element)"

# Convert sum and product results back to power representation
sum_power = get_power_by_integer(int(sum_result), lines)
product_power = get_power_by_integer(int(product_result), lines)

# Print results
print(f"\nSum (GF Computation): {sum_result} → Power: {sum_power}")
print(f"Product (GF Computation): {product_result} → Power: {product_power}")
print(f"Inverse of x^{power1}: {inverse_elem1}")
print(f"Inverse of x^{power2}: {inverse_elem2}")

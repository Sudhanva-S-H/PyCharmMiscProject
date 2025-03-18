import galois

# Define GF(2^m) with power representation
m = int(input("Enter the field exponent m (for GF(2^m)): "))
GF = galois.GF(2**m, repr="power")

# Get the representation table as a string and save it to a file
repr_table = GF.repr_table(sort="power")
with open("GF_table1.txt", "w") as f:
    f.write(repr_table)

print("✅ GF table saved as 'GF_table1.txt'.")


# Read the table from the file
def read_gf_table():
    with open("GF_table1.txt", "r") as f:
        lines = f.readlines()
    return lines


# Function to extract power & polynomial representation given an integer value
def get_power_and_polynomial_by_integer(value, lines):
    for line in lines[2:]:  # Skip headers
        parts = line.strip().split()  # Split into columns
        if len(parts) >= 3:
            power_repr = parts[0]  # Extract power representation (e.g., x^9)
            polynomial_repr = parts[1]  # Extract polynomial part
            int_value = int(parts[-1])  # Convert last column to integer
            if int_value == value:
                return power_repr, polynomial_repr
    return "Not found", "Not found"  # If not found


# Load the table
lines = read_gf_table()

# Get user input for power values
power1 = int(input("Enter initial power value (e.g., 9 for x^9): "))
power2 = int(input("Enter R power value (e.g., 7 for x^7): "))

# Get primitive element α
alpha = GF.primitive_element

# Convert power values to GF elements
Xn = alpha ** power1  # Initial value
R = alpha ** power2  # R value

# Perform 10 iterations of the equation: X(n+1) = X(n) * (R * (X(n) + 1))
print("\nIteration Results:")
print("-------------------------------------------------")
print("| Iter | Power Representation | Polynomial      |")
print("-------------------------------------------------")

for i in range(1, 11):  # 10 iterations
    Xn_plus_1 = Xn * (R * (Xn + GF(1)))

    # Get power and polynomial representation
    power_repr, poly_repr = get_power_and_polynomial_by_integer(int(Xn_plus_1), lines)

    # Display iteration results
    print(f"|  {i:2d}  | {power_repr:20s} | {poly_repr:20s} |")

    # Update Xn for the next iteration
    Xn = Xn_plus_1

print("-------------------------------------------------")

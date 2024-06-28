# multiplication_table.py

# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for i in range(1, 11):  # i ranges from 1 to 10
    result = number * i
    print(f"{number} * {i} = {result}")

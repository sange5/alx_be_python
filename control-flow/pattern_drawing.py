# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 1
while row <= size:
    # Print '*' for each column in the row
    for col in range(1, size + 1):
        print("*", end="")
    # Move to the next line after completing the row
    print()
    row += 1

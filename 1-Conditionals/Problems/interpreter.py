# Prompt the user for input as an arithmetic expression
expression = input("Enter an arithmetic expression: ")

# Split the expression into three parts
x, y, z = expression.split(" ")

# Convert x and z to integers
x = int(x)
z = int(z)

# Here to prevent "using an undefined variable"
result = "N/A"

# Perform calculations based on y
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# Print the results
if result != "N/A":
    print(f"{result:.1f}")
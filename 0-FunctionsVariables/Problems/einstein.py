# Prompts the user for mass in kilograms
m = int(input("Enter the mass in kilograms: "))

# Equation "F = mc²"
c = 300000000
F = m * c**2

print(f"The equivalent energy is {F} Joules.")
# Prompts the user for mass in kilograms
mass = int(input("Enter the mass in kilograms: "))
# Equation "F = mc²"
c = 300000000
energy = mass * c**2

print(f"The equivalent energy is {energy} Joules.")
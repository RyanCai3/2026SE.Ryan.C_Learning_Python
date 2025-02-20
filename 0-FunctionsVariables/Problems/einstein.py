# Prompts the user for mass in kilograms
mass = int(input("Enter the mass in kilograms: "))

# Equation "F = mc²"
speed_of_light = 300000000
energy = mass * speed_of_light**2

print(f"The equivalent energy is {energy} Joules.")
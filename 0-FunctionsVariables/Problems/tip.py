# Prompt user for input on meal price and percentage to tip
# Calculate the tip and return the results
def main():
    price = price_to_float(input("How much was the meal? "))
    percentage = percentage_to_float(input("What percentage would you like to tip? "))
    tip = price * percentage
    print(f"Leave ${tip:.2f}")

# Remove the dollar sign and convert the string to float
def price_to_float(input_string):
    return float(input_string.strip("$"))

# Remove the percentage sign and convert the string to float
def percentage_to_float(input_string):
    return float(input_string.strip("%")) / 100

main()
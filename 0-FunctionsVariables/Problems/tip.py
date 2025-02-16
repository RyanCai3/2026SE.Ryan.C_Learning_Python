def main():
    # Prompt user for input on meal price and percentage to tip
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
	#Calculate the tip and return the results
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
	# Remove the dollar sign and convert the string to float
	return float(d.strip("$"))

def percent_to_float(p):
	# Remove the percentage sign and convert the string to float
	return float(p.strip("%")) / 100

main()
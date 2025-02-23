# Prompt the user for input as a greeting
user_input = input("Greeting: ")

# Strip whitespace from input and convert to lowercase for standardisation
new_string = user_input.strip().lower()

# Check if the greeting starts with a "Hello" or an "H"
if new_string.startswith("hello"):
    print("$0")
elif new_string.startswith("h"):
    print("$20")
else:
    print("$100")
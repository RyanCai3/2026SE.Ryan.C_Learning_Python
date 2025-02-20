# Prompt the user for input as a greeting
user_input = input("Greeting: ")

# Check if the greeting starts with a "Hello" or an "H"
if user_input.startswith("Hello"):
    print("$0")
elif user_input.startswith("H"):
    print("$20")
else:
    print("$100")
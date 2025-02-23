# Prompt the user for input for the answer to the Great Question of Life, the Universe and Everything
user_input = input("What's the answer to the Great Question of Life, the Universe and Everything? ")

# Strip whitespace from input and convert to lowercase for standardisation
new_string = user_input.strip().lower()

# Return "yes" if the user typed in the correct answer, and "no" if they didn't
match new_string:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

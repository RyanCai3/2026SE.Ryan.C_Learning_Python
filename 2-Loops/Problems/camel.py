def convert(camel_case):
    snake_case = []

    # Add underscore before uppercase letter
    # Convert uppercase to lower case
    for characters in camel_case:
        if characters.isupper():
            snake_case.append("_")
            snake_case.append(characters.lower())
        else:
            snake_case.append(characters)

    return "".join(snake_case)

# Prompt user for input
camel_case = input("--> ")

# Convert to snake case and print the result
snake_case = convert(camel_case)
print(f"{snake_case}")
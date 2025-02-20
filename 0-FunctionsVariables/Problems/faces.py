# Prompts the user for input and print the converted results
def main():
    user_input = input("--> ")
    print(convert(user_input))

# Convert emoticons to emojis
def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

main()
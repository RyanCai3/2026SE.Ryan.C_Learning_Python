def main():
    # Prompts the user for input and print the converted results
    user_input = input("--> ")
    print(convert(user_input))

def convert(input_str):
    # Convert emoticons to emojis
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

main()
def main():
    user_input = input("--> ")
    print(convert(user_input))

def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

main()
# Prompts the user for input as emoticon and print the converted results
def main():
    emoticon = input("--> ")
    print(convert(emoticon))

# Convert input emoticons to emojis
def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

main()
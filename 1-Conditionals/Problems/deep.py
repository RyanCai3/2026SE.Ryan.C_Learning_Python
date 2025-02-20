#Prompt the user for input for the answer to the Great Question of Life, the Universe and Everything
user_input = input("What's the answer to the Great Question of Life, the Universe and Everything? ")

#Return "yes" if the user typed in the correct answer, and "no" if they didn't
match user_input:
    case "42" | "Forty-Two" | "Forty-two" |"forty-two" | "Forty Two" | "Forty two" | "forty two":
        print("Yes")
    case _:
        print("No")
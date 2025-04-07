letters = ["A", "B", "C", "D", "E"]
numbers = ["1", "2", "3", "4", "5"]

def print_table():
    print("Letters | Numbers")
    print("--------|--------")
    i = 0
    while i < len(letters):
        print(f"   {letters[i]}    |    {numbers[i]}   ")
        i += 1

user_input = input("What are you looking for? ")
match user_input:
    case "1" | "2" | "3" | "4" | "5" | "A" | "B" | "C" | "D" | "E":
        print_table()
    case _:
        print("Not in table")
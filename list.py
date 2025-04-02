letters = ["A", "B", "C", "D", "E"]
numbers = ["1", "2", "3", "4", "5"]

def main():
    dest = input("What are you looking for? ")
    match dest:
        case "1" | "2" | "3" | "4" | "5" | "A" | "B" | "C" | "D" | "E":
            table()
        case _: 
            print("N/A")

def table():
    print("Letters | Numbers")
    print("--------|--------")
    i = 0
    while i < len(letters):
        print(f"   {letters[i]}    |    {numbers[i]}   ")
        i += 1

main()
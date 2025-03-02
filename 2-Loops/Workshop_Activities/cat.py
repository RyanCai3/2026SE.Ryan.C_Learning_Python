def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        m = int(input("How many times does the cat meow? "))
        if m > 0:
            return m

def meow(n):
    for _ in range(n):
        print("meow")

main()
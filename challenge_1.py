x = int(input("What's x? "))
y = int(input("What's y? "))
operator = input("What's the operator? ")
output = "" 

if operator == "+":
    output = (x + y)
elif operator == "-":
    output = (x - y)
elif operator == "*":
    output = (x * y) 
elif operator == "/":
    output = (x / y)
else:
    output = ("Not a known operator")

print(output)
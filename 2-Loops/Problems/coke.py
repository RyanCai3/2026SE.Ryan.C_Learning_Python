# Begin with the original values
total = 0
price = 50

# Calculate and output the amount due
while total < price:
    print(f"Amount Due: {price - total}")
    coin = int(input("Insert Coin: "))

    # Check if coin is a valid denominator
    if coin in [5, 10, 25]:
        total += coin

# Calculate and return price
change = total - price
print(f"Change Owed: {change}")
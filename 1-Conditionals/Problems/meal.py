def main():
# Prompt the user for a time input in 24-hour time format and convert to hours
    time = input("What's the time? (HH:MM) ")
    new_time = convert(time)

# Check the time and print out what meal it is
    if 7 <= new_time <= 8:
        print("Breakfast time")
    elif 12 <= new_time <= 13:
        print("Lunch time")
    elif 18 <= new_time <= 19:
        print("Dinner time")

def convert(time):
# Split the input time into hours and minutes
    hours, minutes, = time.split(":")

# Convert hours and minutes into integers
    hours = int(hours)
    minutes = int(minutes)

# Convert minutes to a fraction of an hour
    return hours + minutes / 60

main()
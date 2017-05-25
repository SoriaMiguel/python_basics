number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

# the modulo operator divides two numbers but only returns the remainder, not the whole number itself

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

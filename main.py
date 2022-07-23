
number = int(input("Which number do you want to check?\n"))

result = number % 2

if number % 2 == 0:
    print("This is an even number - Modulo of 2 = 0")

else:
    print("This is an odd number and has a remainder of " + str(result))


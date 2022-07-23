# ModuloCalculator

This is a calculator that takes a user's input and applies % 2.

Then if the answer is even (modulo % 2 = 0 remainder) then the program prints "This is an even number - Modulo of 2 = 0".

If the answer has a remainder of anything other than 0, then this is an odd number and the program prints: "This is an odd number and has a remainder of" with the result.

```
number = int(input("Which number do you want to check?\n"))

result = number % 2

if number % 2 == 0:
    print("This is an even number - Modulo of 2 = 0")

else:
    print("This is an odd number and has a remainder of " + str(result))

```

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter second number: "))

minimum = number1


if number2 < minimum:
	minimum = number2
if number3 < minimum:
	minimum = number3
print("Minimum value is", minimum)


maximum = number1

if number2 > maximum:
	maximum = number2
if number3 > maximum:
	maximum = number3
print("Maximum value is", maximum)

if number1 != maximum and number1 != minimum:
	print("The middle number is ", number1)
if number2 != maximum and number2 != minimum:
	print("The middle number is ", number2)
if number3 != maximum and number3 != minimum:
	print("The middle number is ", number3)


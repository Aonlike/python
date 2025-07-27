number1 = int(input ("Enter first number: "))
number2 = int(input ("Enter second number: "))
number3 = int(input ("Enter third number: "))

sum = number1 + number2 + number3
print("The sum is of numbers is " + str(sum))

average = (number1 + number2 + number3)/3
print("The average of the numbers is " + str(average))

product = number1 * number2 * number3
print("The product of the numbers is " + str(product))




largest = number1
if number2 >= number1:
	largest = number2

if number3 >= largest:
	largest = number3

print("The largest number " + str(largest))

smallest = number1

if number2 <= smallest:
	smallest = number2

if number3 <= smallest:
	smallest = number3

print("The smallest number is " + str(smallest))
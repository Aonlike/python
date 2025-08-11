import random
numbers = [random.randint(1,50)for _ in range(10)]
print(numbers)

length = 0
for _ in numbers:
  length = length + 1
print("Length of list:",length)

odd_sum = sum(numbers[1::2])
print("The odd sum is :",odd_sum)

even_sum = sum(numbers[::2])
print("The even sum is :", even_sum)

product = 1
for number in range(2,len(numbers),3):
	product = product * numbers[number]
print("The product of the number at the third position is :", product)

average = sum(numbers) / len(numbers)
print("The average of all numbers in the list:", average)

largest_element = max(numbers)
print("The largest element is: ", largest_element)

smallest_element = min(numbers)
print("The smallest element is: ", smallest_element)
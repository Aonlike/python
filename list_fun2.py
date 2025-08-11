list_of_integers = list(range(1,16))
print(list_of_integers)

duplicate_list = [integer for integer in list_of_integers for _ in range(2)]
print(duplicate_list)


def add_third_element(list):
	return sum(list[integer] for integer in range(2, len(list), 3))

print("Sum of every third element :", add_third_element(list_of_integers))


def sum_numbers(list):
	first = list[0]
	last = list[-1]
	middle_index = len(list) // 2

	if len(list) % 2 == 0:
		middle = (list[middle_index - 1] + list[middle_index]) / 2
	else:
		middle = list[middle_index]
	return first + middle + last

	print("Sum of every third element :",sum_numbers(list_of_integers))	


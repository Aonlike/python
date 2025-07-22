days_of_the_week = """
		1. Monday
		2. Tuesday
		3. Wednesday
		4. Thursday
		5. Friday
		6. Saturday
		7. Sunday

		 """
print(days_of_the_week)
day = int(input("Enter a number: "))
match day:
	case 1:
		print("Monday")
	case 2:
		print("Tuesday")
	case 3:
		print("Wednesday")
	case 4:
		print("Thursday")
	case 5:
		print("Friday")
	case 6:
		print("Saturday")
	case 7:
		print("Sunday")
	
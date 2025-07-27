""" Target Heart-Rate Calculator """

current_age = int(input("Enter current age: "))

maximum_heart_rate = 220 - current_age

	print("The maximum heart rate is ",maximum_heart_rate)

# Using a target heartrate of 50 - 85%

target_heart_rate = (60/100) * maximum_heart_rate

	print("The target heart rate is ", target_heart_rate)

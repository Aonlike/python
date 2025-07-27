def get_score():
	while True:
			score = int(input("Enter score(1-100):  "))
			if score >= 0 or score <= 100:
				return score
			else:
				print("invalid input!Enter score(1-100")

def calculate_grade(score):	
	if score >= 80:
		return "A"
	elif score >= 70:
		return "B"
	elif score >= 60:
		return "C"
	elif score >= 50:
		return "D"
	elif score >= 40:
		return "E"
	else:
		return "F"

def get_feedback(grade):
	if grade == "A":
		return "Excellent performance"
	if grade == "B": 
		return "Good job, keep improving"
	if grade == "C":
		return "Fair effort, keep working on it"
	if grade == "D":
		return "You can do better,dont give up"
	if grade == "E":
		return "Needs improvement, Ask for help"
	if grade == "F"

def main():
	
	while True:

		score = get_score()
		grade = calculate_grade(score)
		feedback = get_feedback(grade)
		print(f"Score: {score}")
		print(f"Grade: {grade}")
		print(f"Feedback: {feedback}")
		
		try_again = input("Enter score(yes or no)?: ")
		if try_again != yes:
				break
main()
		
		 
	



		
		
	
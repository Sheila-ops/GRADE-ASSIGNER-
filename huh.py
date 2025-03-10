while True:
	grade = input("Please enter the mark (or type 'exit' to quit): ")
	
	if grade =="exit":
		print("Goodbye!")
		break
		
	try: 
		marks = int(grade)
		
		if marks < 0 or marks > 100:
			print("Invalid score! Please enter a value between 0 and 100.")
		else:
			if marks >= 90:
				grade = "A Grade"
			elif marks >= 80:
				grade = "B Grade"
			elif marks >= 70:
				grade = "C Grade"
			elif marks >= 60:
				grade = "D Grade"
			else:
				grade = "F Grade"
				
			print(f"Marks == {grade}")
			
	except:
		print("Invalid input. Please enter a number between 0 and 100 or type 'exit' to quit.")
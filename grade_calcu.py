marks = input("Enter ur marks: ")
marks = int(marks)

if marks >= 80:
	grade = "A+"
	print("Your grade: ", grade, "Awesome! Hold it also in future :)")
elif marks >= 70:
	grade = "A"
	print("Your grade: ", grade, "Well done! Try to study even better for next level grade in future. You are very close.")
elif marks >= 60:
	grade = "A-"
	print("Your grade: ", grade, "Hmm, good! Study hard to upgrade your grade. You can & you'll.")
elif marks >= 50:
	grade = "B+"
	print("Your grade: ", grade, "Not bad! Study hard, study hard. You can & you'll.")
else:
	grade = "F"
	print("Your grade: ", grade, "Don't be upset! You can & you'll. Please study hard with full passion. Better luck next time.")

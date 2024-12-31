def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
name = input("Enter students name : ")
score = float(input("Enter Students score : "))
grade = calculate_grade(score)
print(f"WOW {name}, your grade is {grade} !!!")
    

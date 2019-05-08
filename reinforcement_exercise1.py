print("Enter a percentage and I'll show you the equivalent letter grade!")
number_percentage = int(input())

def letter_grade_conversion(number_percentage):
    if number_percentage >=90 and number_percentage <=100:
        return ("A+")
    elif number_percentage >= 85 and number_percentage <=89:
        return ("A")
    elif number_percentage >= 80 and number_percentage <=4:
        return ("A-")
    elif number_percentage >= 77 and number_percentage <=79:
        return ("B+")
    elif number_percentage >= 73 and number_percentage <=76:
        return ("B")
    elif number_percentage >= 70 and number_percentage <=72:    
        return ("B-")   
    elif number_percentage >=67 and number_percentage <=69:
        return ("C+")
    elif number_percentage >=63 and number_percentage <=66:
        return ("C")
    elif number_percentage >=60 and number_percentage <=62:
        return ("C-")
    elif number_percentage >=57 and number_percentage <=59:
        return ("D+")
    elif number_percentage >=53 and number_percentage <=56:
        return ("D")
    elif number_percentage >=50 and number_percentage <=52:
        return ("D-")
    elif number_percentage <= 49:
        return ("F")
    
print(letter_grade_conversion(number_percentage))



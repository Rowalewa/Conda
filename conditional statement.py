age = int(input("Enter your age: "))
differ = int(18) - age
if age >= 18:
    print("You are eligible to apply for an Identification Card")
    name = input("Enter your full name: ")
    print("Hi " + name + ", your request is being processed by the government")
elif age < 18:
    print("You are not eligible to apply for an Identification Card")
    print("Wait for " + str(differ) + " years and try again")
points = int(input("Enter your points:  "))
if points >= 81:
    print("Grade: A")
elif points >= 74:
    print("Grade: A-")
elif points >= 65:
    print("Grade: B+")
elif points >= 60:
    print("Grade: B")
elif points >= 55:
    print("Grade: B-")
elif points >= 59:
    print("Grade: C+")
elif points >= 50:
    print("Grade: C")
elif points >= 45:
    print("Grade: C-")
elif points >= 40:
    print("Grade: D+")
elif points >= 35:
    print("Grade: D")
elif points >= 30:
    print("Grade: D-")
elif points >= 5:
    print("Grade:E")
elif points < 5:
    print("Grade: X")
    print("Results Nullified")


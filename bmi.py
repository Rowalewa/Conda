height = int(float(input("Enter your height in metres ")))
if height < 0:
    print("Invalid height.")
else:
    weight = int(float(input("Enter your weight IN KG ")))
    if weight < 0:
        print("Invalid weight.")
    else:
        BMI = weight/(height*2)
        if BMI > 0:
            print("You are underweight")
            print("Your BMI is", BMI)
        elif BMI >= 18.5:
            print("You are normal")
            print("Your BMI is", BMI)
        elif BMI >= 25.0:
            print("You are Overweight")
            print("Your BMI is", BMI)
        elif BMI > 30.0:
            print("Obesity")
            print("Your BMI is", BMI)
        else:
            print("BMI cannot be calculated")

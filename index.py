print("Hello World")
print("Welcome to eMobilis Institution")
print(800)
# Variables
first_name = input("What is your first name? ")
print(first_name)
last_name = input("What is your last name? ")
print(last_name)
print("Hello")
print(first_name + " " + last_name)
age = input("How old are you? ")
if int(age) < 18:
    print("You are a child")
elif int(age) > 18:
    print("You are an adult")
gender = input("What is your gender? ")
print("You are " + gender)
print("You are " + age + " years old")
# # # data types
# # # string
school = input("What is your school name? ")
print(school)
# integer
print(125)
num_1 = 154
print(num_1)
# # # boolean
greeting = input("What is your name? ")
if greeting == (first_name + " " + last_name):
    print("Hello " + greeting)
    # float
    print(10.25365747756)
    num_2 = 13.6746475765
    print(num_2)
else:
    print("No Cheating 😂")
# # list ordered
MyList = [100,200,300,400,500, "Leslie" + " " + "Wanjala"]
print(MyList)
# set unordered
MySet = {100,200,300,400,500}
print(MySet)
# dictionary
MyDictionary = {"name":"Leslie", "age":18, "gender":"male"}
print(MyDictionary["name"])
MyDictionary["age"] = "26"
# # tuple
MyTuple = (100, 200, 300, 400, 500)
print(MyTuple[3])
# mine
YearOfBirth = int(input("What is your Year of Birth? "))
print(YearOfBirth)
import datetime
today = datetime.date.today()
year = today.year
print(year)
print(today)
old = year - YearOfBirth
print("You are " + str(old) + " years old")
score1 = int(input("Enter your first score as Integer: "))
score2 = int(input("Enter your second score as Integer"))
sum = score1 + score2
average = sum / 2
print("Your final score is: ", sum)
print("Your average is: ", average)
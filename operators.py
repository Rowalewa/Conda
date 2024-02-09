# # arithmetic operators
# # +, *, /, %, **
a = int(5)
b = int(7)
total = a + b
print(total)
difference = b - a
print(difference)
multiply = a * b
print(multiply)
divide = b/a
print(divide)
rem = b % a
print(rem)
if divide == 0: print("divisible")
else:
    print("Not Divisible")

power = a ** b
# print(power)
# # # assignment operator
c = 10
c = c +5
print(c)
d = 7
d = d - 4 #d- =4
print(d)
e = 8
e = e * 3  # e*=3
print(e)
f = 225
f = f/15  # f/=15
print(f)
a = 81
b = 9
remainder = a % b
print(remainder)
if remainder == 0:
    print("a is divisible by b")
else:
    print("a is not divisible by b")
# comparison operators
# ==, !=, <=, >=, <, >
y = 30
z = 40
print(y == z)
print(y != z)
print(y > z)
print(y <= z)
print(y > z)
print(y <= z)
print(y >= z)
# logical operators
# and, or, is not= True, False, True
print((y > z) and (y < z))  # false
print((y < z) and (z > y))  # true
print((y < z) or (y > z))  # true
print((y == z) or (y > z))  # false
print((y > z) or (y == z))  # false
print((y < z) or (y == z))  # true
print(not ((y < z) and (z > y)))
# identity operators
# is, is not
m = 2
n = 5
print(m is n)
print(m is not n)
print(type(m) is type(n))
# membership operator
l = "Welcome to full stack development"
print("Welcome" in l)
print("stack" not in l)
p = int(input("Enter a number p: "))
q = int(input("Enter a number q: "))
if p > q:
    print("p is greater than q")
elif p < q:
    print("p is less than q")
else:
    print("p is equal to q")
MyList = [1, 2, 3, 4, 5, 6, 7, 9]
for i in MyList:
    print(i)
MySet = {1, 2, 3, 4, 5, 6, 7, 8}
for i in MySet:
    print(i)
MyTuple = {'Ben', 'Tom', 'Brian', 'John'}
for i in MyTuple:
    print(i)
char = 'Welcome'
for i in char:
    print(i,)
temperature = int(input('Enter temperature in Celsius: '))
if temperature < 20:
    print("Put on a Sweater")
elif temperature < 30:
    print("Put on shirt")
elif temperature < 40:
    print("Remove shirt")

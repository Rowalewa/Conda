MyTuple = (1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 2)
print(MyTuple)
print(MyTuple[1])
print(MyTuple[1:6])
print(len(MyTuple))
#  del MyTuple - deletes tuple
print(MyTuple.count(2))
print("Total:", sum(MyTuple))
print("Maximum:", max(MyTuple))
print("Minimum:", min(MyTuple))
print("Average:", sum(MyTuple)/len(MyTuple))
print(MyTuple.index(7))
num = int(input("Enter number to search for in tuple: "))
if num in MyTuple:
    print("The number is present in the tuple")
else:
    print("The number is not present in the tuple")
# a tuple cannot be modified ie
# MyTuple[1] = 89  error
# print(MyTuple)
# used for static data
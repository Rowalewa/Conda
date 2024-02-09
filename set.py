MySet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(MySet)
a = int(input("Enter a number, a: "))
if a in MySet:
    print(a, "is in MySet")
else:
    print("a is not in MySet")
# set has no index hence you have to assign a variable
b = 8
if b in MySet:
    print(b, "is in MySet")
else:
    print(b, "is not in MySet")
MySet.add(10)
print(MySet)
MySet.update([11, 12, 13, 14, 15, 16, 17, 18, 19])
print(MySet)
MySet2 = MySet.copy()
print(MySet2)
print(max(MySet))
print(min(MySet))
print(len(MySet))
MySet.discard(17)
print(MySet)
# MySet.clear()
# print(MySet)
# del MySet
# print(MySet)
if 2 in MySet:
    print(2, "is in MySet")
else:
    print(2, "is not in MySet")
# set cannot be modified

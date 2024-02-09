MyList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # square bracket
print(MyList)
print(len(MyList))
print(MyList[9])
print(MyList[0:5])  # Square bracket for range
MyList[0] = 11
print(MyList)
MyList[4] = 14
print(MyList)
MyList.append(17)
print(MyList)
MyList.insert(3, 19)
print(MyList)
MyList.insert(7, 414)
print(MyList)
MyList.extend([4000, 5000, 6000, 7000, 8000, 9000])
print(MyList)
MyList.remove(5)  # remove known element
print(MyList)
del MyList[0]  # remove unknown element identified by index
print(MyList)
MyList.clear()  # clear data in list
print(MyList)
del MyList
MyList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(MyList2))  # maximum
print(min(MyList2))  # minimum
print("Total: ", sum(MyList2))  # total
print("Average: ", sum(MyList2)/len(MyList2))  # average
if 90 in MyList2:
    print("Found 90!")
else:
    print("Error 404:")
    print("90 Not found!")
MyList3 = ["Tom", "John", "Smith", "Jane", "Sarah"]
SearchName = input("Enter search name: ")
if SearchName in MyList3:
    print("Found 😌😌😌😌😌")
else:
    print("Not found 😤😤😤😤😤")

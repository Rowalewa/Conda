MyDictionary = {
    "Name": "Leslie",
    "Gender": "Male",
    "Status": "alive"
}
print("Name: ", MyDictionary["Name"])
print(MyDictionary)
MyDictionary = dict(
    Name="Leslie",
    Gender="Male",
    Status="alive"
)
print(MyDictionary)         # print specific dictionary value
print(MyDictionary["Name"])     # print specific dictionary value
print(MyDictionary["Gender"])   # print specific dictionary value
print(MyDictionary["Status"])   # print specific dictionary value
print(MyDictionary.get('Gender'))   # print specific dictionary value
MyDictionary['Status'] = "Dead"  # changing the content of a title
print(MyDictionary.get('Status'))
MyDictionary['BirthDate'] = 2006
print("YOB: ", MyDictionary.get('BirthDate'))
MyDictionary['email'] = "lesliewanjala06@gmail.com"
print(MyDictionary.get('email'))
MyDictionary['Number'] = 13876
print(MyDictionary.get('Number'))
MyDictionary["Location"] = "Earth"
print(MyDictionary.get('Location'))
MyDictionary2 = MyDictionary.copy()
print(MyDictionary2)
print(len(MyDictionary2))
MyDictionary2.pop('Name')  # removes dictionary element
print(MyDictionary2)
del MyDictionary2['Gender']
print(MyDictionary2)
print(len(MyDictionary2))
MyDictionary2.clear()  # deletes dictionary data
print(MyDictionary2)
del MyDictionary2  # deletes the entire dictionary
if 'Name' in MyDictionary:
    print("Name present")
else:
    print("Error 404: Name not present")
if 'Gender' in MyDictionary:
    print("Gender present")
else:
    print("Error 404: Gender not found")
for name in MyDictionary:
    print(MyDictionary[name])

for key in MyDictionary:
    print(key)

for key, value in MyDictionary.items():
    print(key, value)

MyDictionary = dict(
    Pen=20,
    Pencil=10,
    Soap=50,
    Book=30,
    Water=70,
    Bag=1000,
    Strawberry=120,
    apple=90,
    banana=100,
    orange=50,
)
MyDictionary['Mango'] = 90
print(MyDictionary)
if 'Mango' in MyDictionary:
    print("Mango is in dictionary")
else:
    print("Mango is not in dictionary")
if 'Pear' in MyDictionary:
    print("Pear is in dictionary")
else:
    print("Pear is not in dictionary")
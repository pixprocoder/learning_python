"""
---------- Data Types in Python ---------------
1. Numeric Data
    > int
    > float
    > complex
2. Text Data
    > str (string)
3. Boolean Data
    > True Or False
4. Sequence Data
    > list
    > tuple
    > range
5. Mapped Data:
    > dict
6. Binary data:
    > bytes
    > bytearray
    > memoryview
"""
# a = 2
# b = 2
"""

"""

# Loop
alphavet = "ABCDEFGH"
# for i in alphavet:
#     print(i)

print(alphavet.lower())
print(alphavet.upper())

str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))



# lists
# friends_name = ["kobir", "oli", "samad"]
# for firned in friends_name:
    # print(firned)

# country = ("Spain", "Italy", "India", "England", "Germany")
# if "Germany" in country:
    # print("Germany is present.")
# else:
    # print("Germany is absent.")


info = {"name": "kobir", "age":12, "id": "Bangladesh"}
# print(info["name"])
# print(info.get("age"))
# print(info.values())
# print(info.keys())
# print(info.items())
info["selary"] = 1200
info.update({"age": 25})
# info.clear()
info.pop('age')
# print(info)


# If
# price1 = 1300
# price2 = 1300
# if (price1 > price2):
#     print("price1 is expencive")
# else:
#     print("price2 is expansive")

# num = 20
# if (num < 0):
#     print("Number is negative.")
# elif (num > 0):
#     if (num <= 10):
#         print("Number is between 1-10")
#     elif (num > 10 and num <= 20):
#         print("Number is between 11-20")
#     elif (num >20 and num <=100):
#         print("Number is between 20-100")
#     else:
#         print("Number is grater than 100")
# else:
#     print("Number is zero")


price = 20
if (price < 0):
    print("Price is Nagetive")
elif (price > 0):
    if (price <= 10):
        print("Price is between 1-10")
    elif (price > 10 and price <=20):
        print("Price is between 10-20")
    elif ( price >20 and price <=30):
        print("Price is between 20-30")
    else:
        print("The Price is grater than 30")
else:
    print("The Price is Zero")


# age = int(input("Input age :"))
# if age >= 18:
#     print("welcome")
# else:
#     print("you are not 18 age")
# age = int(input("Input age :"))
# if age > 18:
#     print("welcome")
# elif age == 18:
#     print("you may pass")
# else:
#      print("you are not 18 age")
#
#+, -, *, /
# num1 =  int(input("Num1 :"))
# num2 =  int(input("Num2 :"))
# operator  = input("Operator")
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)

###################################
# convrter F to C
# Temperature = float(input("Temperature: "))
# defind = input(" F or C: ")
# if defind.lower() == "f":
#     temp = (Temperature - 32) *(5/9)
#     print("Temperature in C ", temp)
# elif defind.lower() == "c":
#     temp = Temperature * (9/ 5) + 32
#     print("Temperature in F ", temp)
######################################
# year = int(input("Vvedite god :"))
#
# if year % 4 and year % 100 != 0:
#     print("Yes")
# elif year % 100 == 0 and year % 400 == 0:
#         print("Yes")
# else:
#         print("No")
#####################################
# list
#lists = [1, 2, 3, 4, 5]

#print(lists[1])
####################methots
# list1 = list()
# list1[3]
# list1.append("Hello")
# list1.append("Hel")
# list1.insert(1, "world!")
# print(len(list1))

# fruits = ["banana", "banana", "apple", "orange"]
# vegetables = ["potato", "cabage", "tomato"]
# fruits.extend(vegetables)
#print(fruits)
#print(fruits.count("banana"))
# print(fruits.index("banana",1))
# phone_number = ["9962389889", "9963434545435"]
# block_number = phone_number.pop(1)
# print(phone_number)
# print(block_number)
mega = []
o = []
beeline = []
phon_number1 = input("Vvedite number 1:")
phon_number2 = input("Vvedite number 2:")
phon_number3 = input("Vvedite number 3:")
if phon_number1.startswith("555"):
    mega.append(phon_number1)
elif phon_number1.startswith("700"):
    o.append(phon_number1)
elif phon_number1.startswith("777"):
    beeline.append(phon_number1)
print(mega)
print(o)
print(beeline)
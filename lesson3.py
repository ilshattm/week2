# number_fact = int(input())
# count = 1
# for i in range(1, number_fact + 1):
#     count = count * i
#
# print(count)

#number_fact = int(input())
# count = 0
# for i in range(21):
#     count = count + i
# else:
#     print("result", count)
# break continue
# for i in range(1, 100):
#     if i % 2 == 8:
#         continue
#     print(i)
# for i in range(1, 100):
#     if i % 2 == 0:
#         break
#     print(i)
# pis = []
# for i in range(1, 100):
#     if i % 3 != 0:
#         continue
#     pis.append(i)
# else:
#         print(pis)

####################################3
# i = 0
# while i <= 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
#

# while True:
#     print("Hi")

# number1 = int(input("num1: "))
# number2 = int(input("num2: "))
# operation = int(input("operation: "))
# if
user_log_passw = ['ilshat', 'ryuuu3']
i = 0
user_input = []
#login = ''
#passw = ''
i = 0
j = 0
while True:
    j = j + 1
    login = input("Login: ")
    print(login)
    #user_input.append(login)
    passw = input("Pasw: ")
    #user_input.append(passw)
    if user_log_passw[0] == login:
        print("yes")
        if user_log_passw[1] == passw:
            print("YesYes")
            i +=1
            break
    if j == 3:
        break
if i == 1:
    print("Your correct")


if j == 3:
    print("Your data will be delete")
    user_log_passw.clear()


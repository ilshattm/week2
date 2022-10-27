# my_list = [1, 2, 4]
# print(sum(my_list))
# if my_list:
#     result = sum(my_list) / len(my_list)
# print(round(result))
#
# if not my_list:
#     print("rejjjf")
# if 2 in my_list:
#     print("rejjjf")

# my_list = [1, 8, 4]
# my_list.reverse()
# #my_list.clear()
# #my_list.sort(reverse=True)
# print(my_list)
# my_str = input(" write sentens ")
# my_str1 = list(my_str)
# my_str2 = list(my_str)
# if my_str1 == my_str2.reverse():
#     print("Polindrom")
# else:
#     print("Not polindrom")

# my_list = [1, 2, 5]
# my_list.remove(3)
#my_list.pop(2)
# my_list2 = list(my_list)
# my_list2.append(3)
#
# print(id(my_list))
# print(id(my_list2))
#print(my_list)
# lists = [1, 4, 2, "Sweet", 2.3]
#  for i in lists:
#      print(i)
#w = input()
# word = list(range(1, 1000))
# texts = []
# numb = []
# for i in word:
#     #print(i)
#     print (int(i) % 2 == 0)
# a = int(input(" Vvedite chislo "))
# for i in range(1, 11):
#     print(f" {i} * {a}  = {i * a}")
# for i in range(1, 5):
#     if i == 1 or i == 4:
#         print(f"*****")
#     else: print("*   *")
# #total = total + price
# color = ''
# color.upper()
def get_current(amount):

    Cash = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
    L = []
    for i in Cash:
        print(i)
        while amount >= i:
            L.append(i)
            amount = amount - i
    return(L)
S = get_current(3)
print(S)


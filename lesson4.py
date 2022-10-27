#### tuple #################
# list()  []
# tuple()  ()
# set()   {}
# dict()  {k:v}
# tuples = ("Erj", [1, 2, 3], 6)
#tuples[1].append(5)
# tuples[0].append(5)
# tuples[1][0] = 6
# print(tuples[1])

# tuples = ([1, 2, 3], 4, 5)
# for i in tuples:
#     print(i)
# tuples = list(tuples)
# tuples.append("Nazgul")
# tuples = tuple(tuples)
# print(tuples)
# a = 8
# b =10
# a, b = b, a
# print(a)
# print(b)
# tuples = ([1, 2, 3], 4, 5, 6, 34, 45)
# lists, number, number2 = tuples
# print(lists)
# print(number)
# print(number2)
# lists, *number, number1 = tuples
# print(lists)
# print(number)
# print(number1)
# from math import *
# print(sqrt(4))
# names = ("Nurlan","Smanaly","Aman", "Aman")
# print(names[::2])
# print(names.count("Aman"))
# print(names.index("Nurlan"))
# tuples = ((), (), ('',), ('a', 'b'), 5, "asv", ('a', 'b', 'c'), ('d'), (3, 5, 4, 3))
# #lists = list(tuples)
# listst2 =[]
# for i in tuples:
#     print(i)
#     if type(i) == tuple and len(i) % 2 ==0 and i != ():
#         listst2.append(i)
#
#
# tuples = tuple(listst2)
# print(listst2)
# print(tuples)
# def get_dict(dict_one, dict_two, dict_three):
#     dictonary = (dict_three, dict_two, dict_one)
#
#     return( dictonary)
# d = get_dict({1, 3, 6,}, (1, 4, 8), [54, 23,56])
# print(d)
# district = "чон-арык"
# district == ("чон-арык", "байтик", "ортосай")
# filename = 'yuiewe.png'
# s = filename[-3::]
# n = filename[-4::]
# if  s in ['png', 'doc']:
#         print(f'Расширение файла - {s} ')
# elif n in ['jpeg', 'xlsx', 'html']:
#      print(f'Расширение файла - {n} ')
# else:
#     pass
# def get_extension(filename):
#     extensions = ['png', 'jpeg', 'html', 'doc',   'xlsx']
#
#
# print(get_extension('rerfferf.pptx'))
# def knight_beats(x1, x2, y1, y2):
#     if x1 + 1 == x2 and y1 + 2 == y2:
#         return (True)
#     elif x1 - 1 == x2 and y1 + 2 == y2:
#         return (True)
#     elif x1 + 2 == x2 and y1 + 1 == y2:
#         return (True)
#     elif x1 - 2 == x2 and y1 + 1 == y2:
#         return (True)
#     elif x1 - 2 == x2 and y1 - 1 == y2:
#         return (True)
#     elif x1 - 1 == x2 and y1 - 2 == y2:
#         return (True)
#     elif x1 + 2 == x2 and y1 - 1 == y2:
#         return (True)
#     elif x1 + 1 == x2 and y1 - 2 == y2:
#         return (True)
#     else:
#         return print(False)
# knight_beats(3, 5, 4, 3)
username = 'tttuuuppp'
entered_username = 'tttuuupp9p'
#for i in range(0, len(username)):
# if username == entered_username and len(username) == len(entered_username):
#     if username == entered_username and len(username) == len(entered_username):
#     print(True)
# else:
#     print(False)
def season(month):
    if month == 12 or month <= 2:
        return print('зима')
    elif month >=  3 and month <= 5:
        return print('весна')
    elif month >= 6 and month <= 8:
        return print('лето')
    elif month >= 9 and month <= 11:
        return print('осень')
    else:
        return print(False)
season(1)
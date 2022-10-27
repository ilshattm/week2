# for i in range(1, 11):
#     for j in range(1, 10):
#         result = i*j
#         print(f" {j} * {i} ={result}", end="\t\t\t\t")
#     print()
# a = [[3, 2, 1, 5, 9],
#      [2, 3, 3, 2, 4],
#      [5, 7, 9, 1, 7],
#      [23, 54, 6, 9, 3],
#      [2, 5, 6, 1, 5]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if i == j:
#             a[i][j] = a[i][j] * 2
#         elif i > j:
#             a[i][j] = 0
#         elif i < j:
#             a[i][j] = 1
#         print(a[i][j], end='  ')
#     print()
import random
cities = ['Neo', 'Lake', 'Base', 'Jorn']
city = random.choice(cities)
print(city)

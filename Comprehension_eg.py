# nums= [1,2,3,4,5,6,7,8,9,10]
#
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)
#
# # comprehension way
#
# my_list = [n for n in nums]
# print(my_list)

# ---------------------------------------------------

# nums= [1,2,3,4,5,6,7,8,9,10]
#
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)
#
# # comprehension way
#
# my_list =[n*n for n in nums]
# print(my_list)


# using a map + lambda

# my_list = map(lambda n: n*n, nums)
# print(my_list)

# ---------------------------------------------------
# nums= [1,2,3,4,5,6,7,8,9,10]

# my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)

# comprehension way

# my_list = [n for n in nums if n%2==0]
# print(my_list)

# filter + lambda

# my_list= filter(lambda n: n%2==0, nums)
# print(my_list)

# ---------------------------------------------------

# nums= [1,2,3,4,5,6,7,8,9,10]
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)

# comprehension way

# my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# ---------------------------------------------------

# Dictionary Comprehensions
# names = ['Bruce', 'Clark', 'Peter', 'Logan', "Wade"]
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#
# my_dict = {}
# for name, hero in zip(names,heros):
#     if name!= 'Peter':
#         my_dict[name] = hero
#
# # comprehension way
#
# my_dict = {name:hero for name,hero in zip(names,heros) if name != 'Peter'}
# print my_dict

# ---------------------------------------------------

# Set comprehensions

# nums= [1,1,2,2,6,7,5,5,4,8,9,2,3,4,5,6,7,8,9,10]
#
# my_set = set()
# for n in nums:
#     my_set.add(n)
#
# # comprehension way
#
# my_set = set(n for n in nums)
# my_set_02 = {n for n in nums}
# print my_set
# print my_set_02

# ---------------------------------------------------

# Generator Expressions

# nums= [1,2,3,4,5,6,7,8,9,10]
#
# def gen_func(nums):
#     for n in nums:
#         yield n*n
#
# my_gen = gen_func(nums)
#

# for i in my_gen:
#     print i
#
# # comprehension way
# my_gen = (n*n for n in nums)
#
# for i in my_gen:
#     print i

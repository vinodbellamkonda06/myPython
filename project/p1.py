# num_list = []
# '''This program gives the sum of numbers below 1000 divisible by 3 and 5'''
# for num in range(1, 1000):
#     if num % 3 == 0 or num % 5 == 0:
#         num_list.append(num)
#
#
# print(sum(num_list))

#num_list = sum([num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0])
print(sum([num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0]))

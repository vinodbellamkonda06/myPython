'''fib_list = [1, 2]
i = fib_list[-1]

while i < 4000000:
    for j in range(1, i):
        fib_list.append(fib_list[-1] + fib_list[-2])
        i = fib_list[-1]


print(sum([num for num in fib_list if num % 2 == 0 ]))
l = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]
sum_l = sum([num for num in l if num % 2 == 0])
print(sum_l)'''

def calcE():
	x = y = 1
	sum = 0
	while (sum < 1000000):
		sum += (x + y)
		x, y = x + 2 * y, 2 * x + 3 * y
	return sum
print(calcE())

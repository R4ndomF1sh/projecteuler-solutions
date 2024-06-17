list_ = list(range(1, 101))

sum_of_the_squares = 0
numbers_sum = 0
for i in list_:
	num = i * i
	sum_of_the_squares += num
	numbers_sum += i

square_of_the_sum = numbers_sum * numbers_sum

difference = square_of_the_sum - sum_of_the_squares

print(">>", difference)
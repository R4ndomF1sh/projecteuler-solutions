
def check_palindrome(number):
	num = str(number)
	return num == num[::-1]


def result():
	max_palindrome = 0
	for num1 in range(100, 1000):
 		for num2 in range(100, 1000):
 			product = num1 * num2
 			if check_palindrome(product):
 				if product > max_palindrome:
 					max_palindrome = product
	return max_palindrome


print("> ", result())
def test_inferiority(a, b, c):
	if a < b < c:
		return True
	return False

def test_sum(a, b, c):
	num = a + b + c
	if num == 1000:
		return True
	return False


for a in range(1000):
	for b in range(1000):
		square_a = a*a
		square_b = b*b
		square_c = square_a + square_b
		c = square_c**0.5
		if test_inferiority(a, b, c):
			if test_sum(a, b, c):
				print(f"a = {a}, b = {b}, c = {c}")
				abc = a*b*c
				print("product: ", abc)	

			
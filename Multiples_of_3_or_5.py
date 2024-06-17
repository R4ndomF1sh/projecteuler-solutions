numbers = range(1000)


totale_sum = 0

for i in numbers:
	if i % 3 == 0:
#		print("for_3: ", i)
		totale_sum += i
	elif i % 5 == 0:
#		print("for_5: ", i)
		totale_sum += i

print("totale: ", totale_sum)

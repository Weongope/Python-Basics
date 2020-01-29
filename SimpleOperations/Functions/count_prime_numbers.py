def count_prime(num):
	#Check if num is either 0 or 1
    if num < 2:
		return 0
	#Bigger than 2

	#Store primes
	primes = [2]
	#counter
	x = 3

	#x is going through every-number up to num
	while x <= num:
		#check if x is prime
		for i in primes:
			if x%i == 0:
				x +=2
				break
		else:
			primes.append(x)
			x += 2
	print(primes)
	return len(primes)

print(count_prime(100))

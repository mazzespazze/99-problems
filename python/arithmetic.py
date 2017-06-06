#31 determine whether a given integer number is prime
prime = lambda x: True not in [x % i == 0 for i in range(2,x)]

#32 determine the greatest common divisor of two positive integer numbers
gcd = lambda a,b: a if(b == 0) else gcd(b, b % a) 
if __name__ == '__main__':
	print("Is 7 prime ? {0}".format(prime(7)))
	print(prime(17))
	print(prime(8))
	print(gcd(36,63))
import math
#31 determine whether a given integer number is prime
prime = lambda x: True not in [x % i == 0 for i in range(2,x)]

#32 determine the greatest common divisor of two positive integer numbers
gcd = lambda m,n: m if(n == 0) else gcd(n, m % n)

#33 determine if two numbers are coprime: gcd must be 1 (using gcd)
coprime = lambda a,b: 1 == gcd(a,b)

#34 euler totient function: given m it calculates the NUMBERS of positive integers that are coprime
phi = lambda m: [coprime(x,m) for x in range(1,m+1)].count(True)

#35 Determine the prime factors of a given integers
#that's not algorithmical polynomial, I'm gonna implement the prime divisors with a square now
prime_factor = lambda x: [prime(n) for n in range(1,math.ceil(x/2+1))]
#36~38 boring, nothing new

#39 A list of prime number
primeN = lambda x: x if prime(x) else None
prime_list = lambda x: list(filter(lambda x: x != None, map(lambda a: primeN(a), range(2,x))))

#40 Goldbach conjecture
_goldbach = lambda a,b: [a,b] if prime(a) and prime(b) else _goldbach(a-1, b+1)
goldbach = lambda x: _goldbach(x//2, x//2) if x % 2 == 0 else _goldbach(x//2, x//2+1)
goldbach1 = lambda x: _goldbach(x-1, 1)

#41 Goldbahc conjecture with upper and lower bound
_goldbach_list = lambda u,i,s: s if u==i else _goldbach_list(u,i+1,s+"\n"+str(i)+" ~> "+str(goldbach1(i)))
goldbach_list = lambda l,u: _goldbach_list(u+1,l,"")  

if __name__ == '__main__':
	print("Is 7 prime?~> {0}".format(prime(7)))
	print("Is 8 prime?~> {0}".format(prime(8)))
	print("Great common divisor between 36 and 63 ~> {0}".format(gcd(36,63)))
	print("Coprime 35 and 64?~> {0}".format(coprime(35,64)))
	print("Coprime 36 and 63?~> {0}".format(coprime(36,63)))
	print("phi(10) ~> {0}".format(phi(10)))
	print(prime_factor(10))
	print(prime_list(10))
	print(goldbach(28))
	print(goldbach1(28))
	print("Goldbach list\n" + goldbach_list(9,20))
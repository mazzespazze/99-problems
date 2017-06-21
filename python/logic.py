#46 logical equivalences
_and = lambda a,b: bool(a) and bool(b)
_or = lambda a,b: bool(a) or bool(b)
_xor = lambda a,b: bool(a) != bool(b)
_nand = lambda a,b: not _and(a,b)
_nor = lambda a,b: not _or(a,b)
_equ = lambda a,b: a == b

#table are boring, I go with the GrayCode
#49
gray = lambda n: n and[x+y for x in '01' for y in gray(n-1)[::1-2*int(x)]] or ['']
#Apllying a binary function to the gray code
#printer = lambda x,func: print("{0} ~> {1}".format(x, func(*x)))
#converter = lambda s:[int(x) for x in list(s)]
#pretty = lambda n,func: list(map(lambda x: printer(converter(x),func), gray(n)))

#50 Huffman code
if __name__ == '__main__':
	print(_and(1,0))
		print(_or(1,0))
		print(_xor(1,0))
	print(_nand(1,0))
	print(_nor(1,0))
	print(_equ(1,1))
	print(gray(2))
	#f0 = lambda x: 1-x
	#f1 = lambda x,y: x&y
	#f2 = lambda x,y,z: x&y|z
	#pretty(1,f0)
	#pretty(2,f1) 
	#pretty(3,f2)
	
#1 return the last element of a list (it does not change the list: use pop() for REMOVE)
_last = lambda l: l[-1]

#2 return the last but one element
_last_but_one = lambda l: l[-2]

#3 find the k-th element of a list
k_th = lambda l,k: l[k]

#4 find the number of elements of a list
num_list = lambda l: len(l)

#5 reverse a list
rev = lambda l: l[::-1]

#6 find out if a list is palindrome
palindrome = lambda l: l == l[::-1]

#7 flatten a nested list structure
flatten = lambda *l: (x for a in l for x in (flatten(*a) if isinstance(a,list) else(a,)))

#8 eliminate consecutive duplicates of list elements
compress = lambda l: list(set(l))

#9 pack consecutive duplicates of list elements into sublists (without collections module)
duplicate = lambda l: list(zip(list(map(lambda x: l.count(x), list(set(l)))),list(set(l))))

#10 is related to #9

#11 modified run-length: only elements with more of one occurrence must be printed as run-length
def modify(l):
	for x in l:
		if(x[0]==1)

if __name__ == '__main__':
	l = [1,2,3,4,5,6]
	print(_last(l))
	print(_last_but_one(l))
	print(k_th(l,3))
	print(num_list(l))
	print(rev(l))
	r = [1,2, [3,4]]
	print(list(flatten(r)))
	r = ['a','a','a','b','b','c','c','c','d']
	print(compress(r))
	print(duplicate(r))
##WORKING WITH THE LISTS##
import random
import itertools
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
modify = lambda l: list(map(lambda x: x[1] if x[0]==1 else x, l)) 

#12 decode a run length encoding
decode = lambda l: list(flatten(list(map(lambda x: [x[1]]*x[0], l))))

#13 it's the 9 since we didn't use callback methods

#14 duplicate elements of a list: if the order is not important it is enough "list * 2". 
#So here we consider the order as a matter of importance
no_order_double_it = lambda l: l*2
ordered_double_it = lambda l: list(flatten(list(map(lambda x: [x]*2, l))))

#15 duplicate a number n of times
duplicate_n = lambda l,n: list(flatten(list(map(lambda x: [x]*n, l))))

#16 drop every n-th element of a list
drop = lambda l,n: l[n-1::n] #it does not work ~> Invalid syntax. Anonymous clash?
def _drop(l,n):
	del(l[n-1::n])
	return l

#17 split a list into two parts
split = lambda l: [l[:int(len(l)/2)]]+[l[int(len(l)/2):]]

#18 extract a slice from a list
extract = lambda l,s,e: l[s:e]

#19 rotate a list n places to the left: so the head becomes the new tail
rotate = lambda l,n: l if n == 0 else rotate(l[1:]+[l[0]], n-1)

#20 remove the k-th element of a list, and return the list and the element removed in a tuple: oss tuples do not change
remove = lambda l,k: (l.pop(k),l)[::-1]

#21 insert an element into a given position in a list
insert = lambda l,k,el: l[0:k]+[el]+l[k:]

#22 creating a list containing all integers within a given range
_range = lambda a,b: list(range(a,b+1)) #list(map(lamda x: x, range(a,b+1)))

#23 extract a given number of randomly selected elements from a list (so n is the number of random elements that we have to pick up)
#HINT: I have imported random ~> import random
#Osservation: My list does not change, otherwise we just need to save the random index and delete the value also from the list
_select = lambda l,n,b: b if n == 0 else _select(l, n-1, b+[l.pop(random.randint(0,len(l)-1))])

#24 draw n different random numbers from the set 1..m
#HINT: let's use the #23!
draw = lambda r,n: _select(list(range(1,r+1)),n,[])

#25 Generate a random permutation of the elements of a list
#HINT: we can use the rotation: number #19!
permute = lambda l: rotate(l, random.randint(1,len(l)-1))

#26 Generate the combinations of K distinct objects chosen from the N elements of a list.
#In how many ways can a committee of 3 be chosen from a group of 12 people? We all know that there are C(12,3) = 220 possibilities
#(C(N,K) denotes the well-known binomial coefficient). For pure mathematicians, this result may be great. 
#But we want to really generate all the possibilities.
#HINT: itertools
permute_all = lambda l, n: list(itertools.permutations(l,n))

#27 Group the elements of a set into disjoint subsets.
#a) In how many ways can a group of 9 people work in 3 disjoint subgroups of 2, 3 and 4 persons? 
#We are gonna write a function that generates all the possibilities.
#d = 9, a = 2, b = 3, c = 4

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
	print(modify(duplicate(r)))
	print(decode(duplicate(r)))
	print(no_order_double_it(l))
	print(ordered_double_it(l))
	print(duplicate_n(l,4))
	print(_drop(l,3))
	l = [1,2,3,4,5,6,7]
	print(split(l))
	print(rotate(l,3))
	print(remove(l,6))
	print(insert(l,3,42))
	print(_range(3,10))
	print(_select(l,2,[]))
	print(draw(49,6))
	l = [1,2,3,4,5,6]
	print("Permutation {0} and then {1}".format(l, permute(l)))
	print("Permute_all starting from {0} with {1} of range: {2}".format(l,3,permute_all(l,3)))


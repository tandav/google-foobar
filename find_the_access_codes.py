
# import math
# def nCr(n,r):
#     f = math.factorial
#     return f(n) / f(r) / f(n-r)

# TRY TO USE SLICES WHEN MVP WILL WORKS ===============================

# def answer(l): 
# 	l.sort() # try pass tests w/o this line
# 	used = [] # used elements of l, now it's indexes 
# 	n = len(l) # make back substitution before submiting
# 	codes = 0 # numper of lucky triples
	
	# for i in xrange(len(l) - 2):
	# 	pass

	# for i in xrange(n - 2): # mb start w/ len(l)
	# 	if i not in used:
	# 		temp_list = []
	# 		for x in xrange(i, len(l)):
	# 			if l[x] % l[i] == 0:
	# 				temp_list.append(x)
	# 				used.append(x)
	# 		print(temp_list)
	# 		if len(temp_list) > 2:
	# 			codes += nCr(len(temp_list), 3)


		# if l[i] not in used:
		# 	print([el for el in l[i:] if el % l[i] == 0])
		# 	codes += nCr(len([el for el in l[i:] if el % l[i] == 0]), 3)
		# 	used.append(l[i])
		# for j in xrange(i + 1, n - 1):
		# 	if l[j] % l[i] == 0:
		# 		for k in xrange(j + 1, n):
		# 			if l[k] % l[j] == 0:
		# 				codes += 1
		# 				print(l[i], l[j], l[k])


	# return codes		

def answer(l):
	# l.sort() # try pass tests w/o this line
	n = len(l) # make back substitution before submiting
	codes = 0 # numper of lucky triples
	used = [] # indexes of used as first in lucky-triple

	for i in xrange(0, n - 2): # mb start w/ len(l)
		if i not in used:
			temp_list = [] # elements that divides by l[i]
			for t in xrange(i + 1, n):
				if l[t] % l[i] == 0:
					temp_list.append(l[t])
			if len(temp_list) >= 2:
				print "TL:", temp_list
				for j in xrange(len(temp_list)):
					for k in xrange(j + 1, len(temp_list)):
						if temp_list[k] % temp_list[j] == 0:
							codes += 1
							print (l[i], temp_list[j], temp_list[k])
			used.append(i)
	return codes


# l = [2, 2, 3, 6, 7, 8, 10, 10, 11, 12]
# l = [1, 1, 1]

print(answer(l)) # seems to work well, but Time limit exceeded

# TODO: when pass all tests - check solutions of other guys on github

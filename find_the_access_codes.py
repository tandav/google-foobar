# mb use dict for lists instead of list
def answer(l):
	l.sort() # try pass tests w/o this line
	n = len(l) # make back substitution before submiting
	codes = 0 # numper of lucky triples
	triples = []
	list_map = [-1 for i in xrange(n)] # index -> list_to_search_in, 0 means search in l
	# lists = [] # lists of indexes dividends of each element in l
	lists = [] # 
	# xrange(1, n)


	for i in xrange(n - 2): # ceil(sqrt(n)) ?? == int(sqrt(n + 1))
		if i > 0 and l[i] == l[i - 1]: # skip dublicates 
			continue
			print('dublicates', i, l[i], l[i-1])
		# search in lists[list_map[i]]
		dividends = [] # indexes of dividends of l[i]
		print 'i =', i

		if list_map[i] < 0:
			for j in xrange(i + 1, n):
				if l[j] % l[i] == 0:
					if l[j] == l[j-1] and j > i + 1:
						continue
					dividends.append(j)
					if l[i] % l[list_map[j]] and list_map[j] != -1:
					# if l[i] % l[list_map[j]] and l[list_map[j]] != -1:
						list_map[j] = i

					if j + 1 < n:

						for k in xrange(j + 1, n):
							# print 'j =', j, 'k =', k
							if l[k] % l[j] == 0:
								# print 'hello'
								if l[k] == l[k-1] and k > j + 1:
									continue

								codes += 1
								print('< 0: ', 'idxs: ', i, j , k, 'values:', l[i], l[j], l[k])

		else:
			print('lists[map[i]]', lists[list_map[i]], [l[f] for f in lists[list_map[i]]])
			for ji, j in enumerate(lists[list_map[i]][:-1]): # i = 3, j = 7
				if l[j] % l[i] == 0:
					dividends.append(j)
					if l[i] % l[list_map[j]]:
						list_map[j] = i
					for k in lists[list_map[i]][ji + 1:]:
						# print('ji:', ji)
						if l[k] % l[j] == 0:
							codes += 1
							print('from maps: ', 'idxs: ', i, j , k, 'values:', l[i], l[j], l[k], 'ji: ', ji)



		lists.append(dividends[1:]) # del 1st element 'cause we dont need it (it will be first in lucky triple)
		print('cur_dividends', dividends[1:], [l[i] for i in dividends[1:]])
		print('list map:', list_map)
		print('')
		# print('lists:', lists)
		# for j in xrange(i + 1, n - 1):
			# for k in xrange(j + 1, n):
				# pass
		# add new pointers in map, new lists



	# for i in range(n - 2):
		# if i not in # ... make list?
			# for j in xrange(i + 1, n - 1):
				# if l[j] % l[i] == 0:

		# for x in xrange(1,10):
		# makin' list?
		
	return codes



# l = [2, 2, 3, 6, 7, 8, 10, 10, 11, 12]
l = [2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 15, 16, 18, 20, 21, 24, 30]
# l = [1,2,2,2,3]
print('ANSWER:', answer(l)) # seems to work well, but Time limit exceeded

# TODO: when pass all tests - check solutions of other guys on github

def childrens(node, depth):
	childs = []

	for i in range(depth):
		childs_copy = list(childs)
		childs = [childrens(c, 0) for c in childs_copy]
	return childs

def childrens_1(node):
	childs = []

	for i in reversed(range(len(node))):
		childs.append(node[:i] + node[i+1:])
	return childs
	# for i in range(len(node)):
	# 	childs.append([:i] + [i+1]:)
	# if depth == 0: return childs
	# else:
	# 	childs = [childrens(c, 0) for c in childs_copy]


def answer(l):
	if sum(l) % 3 == 0:
		return int(''.join(map(str,sorted(l, reverse=True))))
	elif len(l) == 1: # maybe len(l) == 0
		return 0
	else:
		l.sort()
		# print l
		for i in range(len(l)):
			l_copy = list(l)
			del(l_copy[i])
			if sum(l_copy) % 3 == 0:
				return int(''.join(map(str,sorted(l, reverse=True))))
		for i in range(len(l)):
			l_copy = list(l)
			del(l_copy[i])
			return answer(l_copy)

# print(answer([3, 1, 4, 1, 5, 9]))
arr = [3, 1, 4, 1, 5, 9]
arr.sort(reverse=True)
print(arr)
print(childrens_1(arr))

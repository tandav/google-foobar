# def answer(s):
# 	out = ''
# 	for si in s:
# 		if ord('a') <= ord(si) <= ord('z'):
# 			out += chr(ord('z') - ord(si) + ord('a'))
# 		else: out += si
# 	return out

# print(answer('Aab !c'))

def answer(s): return ''.join([chr(ord('z') - ord(si) + ord('a')) if ord('a') <= ord(si) <= ord('z') else si for si in s])

	# for si in s:
	# 	if ord('a') <= ord(si) <= ord('z'):
	# 		out += chr(ord('z') - ord(si) + ord('a'))
	# 	else: out += si
	# return out

print(answer('abcxyz A ^ / z'))

# s = list("abc")

# print # print s

def answer(s):
	return ''.join([chr(ord('z') - ord(si) + ord('a')) if ord('a') <= ord(si) <= ord('z') else si for si in s])

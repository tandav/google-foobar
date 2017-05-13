# check input strings, each one no larger than 10^50 len(M) and len
# so there's kinda subtask int(M), int(F)


## any (1, x) or (x, 1) -> success
## max(M, F) was changed, min - remained unchanged

def answer(M, F):
	M, F = int(M), int(F)
	if M <= 10**50  and F <= 10**50:
		
	# if int(M) <= 10**50 and int(F) <= 10**50:
		def answer(M, F):
	M, F = int(M), int(F)
	if M < 1e50 and F < 1e50:
		n = 0
		while M > 0 and F > 0:
			d = abs(M - F)
			if M > F: M = d
			else: F = d
			if M == 1 or F == 1: return str(n + max(M, F))
			n += 1
	return 'impossible'

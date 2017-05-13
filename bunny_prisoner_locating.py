def answer(x, y):
	return int(x * (x + 1) / 2 + (y -1)*x + (y - 2)*(y - 1) / 2)

# | 16
# | 11 17
# |  7 12 18
# |  4  8 13 19
# |  2  5  9 14 20
# |  1  3  6 10 15 21
#   +1 +2 +3


# 1  3  6  10  15  21
#  +2 +3 +4  +5  +6

# def function(n):
	# return n*(n+1)/2 

print(answer(4,3))

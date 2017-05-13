def answer(M, F):
    M, F = int(M), int(F)
    generations = 0
    min_max = [min(M, F), max(M, F)]
    while min_max[0] > 1 and min_max[1] > 1:
        min_max.sort()
        if min_max[1] %  min_max[0] == 0: return "impossible"
        generations += min_max[1] // min_max[0]
        min_max[1]  = min_max[1] %  min_max[0]
    generations += min_max[0] if min_max[1] == 1 else min_max[1]
    return str(generations - 1)
    return "impossible"

print(answer("123", "23"))

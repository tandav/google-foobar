def answer(M, F):
    generations = 0
    min_max = [int(M), int(F)]
    while min_max[0] > 1 and min_max[1] > 1:
        min_max.sort()
        if min_max[1] %  min_max[0] == 0:
            return "impossible"
        generations += min_max[1] // min_max[0]
        min_max[1]  = min_max[1] %  min_max[0]
    generations += max(min_max) - 1 # other than 1 in list
    return str(generations)

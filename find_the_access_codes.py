def answer(l):
    if len(l) < 3: return 0

    codes = 0
    for i in range(1, len(l) - 1):
        cnt_x = len([x for x in l[:i] if l[i] % x == 0])   # Count possible x in (x, y, z)
        cnt_z = len([z for z in l[i + 1:] if z % l[i] == 0])   # Count possible z in (x, y, z)
        codes += cnt_x * cnt_z  # Possible combination should be the product
    return codes

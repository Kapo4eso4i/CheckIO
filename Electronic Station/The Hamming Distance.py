def checkio(n, m):
    big = bin(max(m, n))
    tiny = bin(min(m, n))
    tiny = '0b' + (len(big) - len(tiny)) * '0' + tiny[2:]
    count = 0
    for i in range(len(big)):
        count += big[i] != tiny[i]
    return count

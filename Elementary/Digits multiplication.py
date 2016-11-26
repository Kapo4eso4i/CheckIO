def checkio(number):
    result = 1
    for ch in str(number):
        if ch != "0":
            result *= int(ch)
    return result

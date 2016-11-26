def checkio(data):
    ROMANS = (('M',  1000),
             ('CM', 900),
             ('D',  500),
             ('CD', 400),
             ('C',  100),
             ('XC', 90),
             ('L',  50),
             ('XL', 40),
             ('X',  10),
             ('IX', 9),
             ('V',  5),
             ('IV', 4),
             ('I',  1))
    result = ""
    count = 0
    while True:
        if data >= ROMANS[count][1]:
            result += ROMANS[count][0]
            data -= ROMANS[count][1]
        else:
            count += 1
            continue
        if data == 0:
            break
    return result

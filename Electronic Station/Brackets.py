def checkio(expression):
    br_pairs = {'(':')', '[':']', '{':'}'}
    filo = []
    for char in expression:
        if char in br_pairs.keys():
            filo.append(char)
        elif char in br_pairs.values():
            if filo and char == br_pairs[filo[-1]]:
                del filo[-1]
            else:
                return False
    return False if filo else True

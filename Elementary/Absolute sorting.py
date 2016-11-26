def checkio(numbers_array):
    numbers_dict = {}
    for number in numbers_array:
        numbers_dict[abs(number)] = number
    sorted_numbers = sorted(numbers_dict.keys())
    return [numbers_dict[x] for x in sorted_numbers]

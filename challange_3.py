alphabetic_position = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

vowels = "aeiou"


def remove_vowels(lower_str):
    l_str_list = []
    l_str_list[:] = lower_str
    for i, c in enumerate(l_str_list):
        if (c in vowels):
            l_str_list[i] = " "
    return "".join(l_str_list)


def calculate_consonant_values(l_str):
    only_consonant_str = remove_vowels(l_str)
    constant_list_groups = only_consonant_str.split(" ")
    constant_list_of_char_list = [[c for c in s] for s in constant_list_groups]
    summed_list_values_for_list_of_contants = [
        sum(
            [alphabetic_position[c] for c in l]
        ) for l in constant_list_of_char_list if l != []
    ]

    return summed_list_values_for_list_of_contants


def find_max_consonant_value(lower_case_str):
    return max(calculate_consonant_values(lower_case_str))

print (find_max_consonant_value("zodiacs"))
print (find_max_consonant_value("strength"))
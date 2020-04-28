def even_or_odd(x):
    if x % 2 == 0:
        print("even")
        return
    else:
        print("odd")


def is_permutation(first, second):
    first_dictionary = {}
    second_dictionary = {}

    for element in first:
        if first_dictionary.get(element) is not None:
            first_dictionary[element] = first_dictionary.get(element) + 1
        else:
            first_dictionary[element] = 1

    for element in second:
        if second_dictionary.get(element) is not None:
            second_dictionary[element] = second_dictionary.get(element) + 1
        else:
            second_dictionary[element] = 1

    print(second_dictionary)

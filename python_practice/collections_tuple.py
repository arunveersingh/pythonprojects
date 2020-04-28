# tuple, range, set
# tuple - immutable sequences of arbitrary objects


def learn_tuple():
    t = ("apple", "mango", "orange")
    print(t)

    for element in t:
        print(element)

    t_mix = (1, 20.4, 7800, "mango")
    print(t_mix)

    # tuple with single element
    t_single = (2)  # wrong
    print(type(t_single))
    t_single = (2,)  # right
    print(type(t_single))

    t_empty = ()
    print("t_empty type: " + str(type(t_empty)))

    t_without_parenthesis = 1, 2, 3, 5, "string"
    print("t_without_parenthesis type: " + str(type(t_without_parenthesis)))

    #  print(min(t_mix))  # this will not work
    print(min(t_single), max(t_single))


def min_max(t):
    return min(t), max(t)


learn_tuple()
lower, upper = min_max((1, 3, 5, 9, 0, 110))
print(lower)
print(upper)

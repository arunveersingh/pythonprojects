# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
from array import array


def rotate_array(input_array, array_size, shift):
    new_array = [int] * array_size
    current_index = 0
    for element in input_array:
        new_array[new_index(current_index, array_size, shift)] = element
        current_index += 1

    print(input_array)
    print(new_array)


def new_index(index, array_size, shift):
    extra = shift % array_size
    if extra >= 0:
        shift = extra

    shifted_index = index - shift

    if shifted_index < 0:
        shifted_index = shifted_index + array_size

    return shifted_index


# invoke the rotate_array
rotate_array(array("i", [1, 2, 3, 4, 5, 6, 7]), 7, 21)
rotate_array(array("i", [1, 2, 3, 4, 5, 6, 7]), 7, 0)
rotate_array(array("i", [1, 2, 3, 4, 5, 6, 7]), 7, 6)
rotate_array(array("i", [1, 2, 3, 4, 5, 6, 7]), 7, 7)
rotate_array(array("i", [1, 2, 3, 4, 5, 6, 7]), 7, 20)
rotate_array(array("i", [1, 2, 3, 4, 5, 6, 7]), 7, 24)

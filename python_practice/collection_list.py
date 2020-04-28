my_list = [100, -34, 0, 6, 8, 9]
print(my_list)
print(f"first element of list is {my_list[0]}")
print(f"last element of list is {my_list[-1]}")  # negative indices
print(f"second last element of list is {my_list[-2]}")
print(f"values in the range of 1 to the last are {my_list[1:]}")
print(f"values in the range of 1 to the last excluding last {my_list[1:-1]}")
print(f"values in the range of 0 to the 3 {my_list[:3]}")

my_new_list = my_list
print(f"is my_list is my_new_list (as it is reference assigning): {my_list is my_new_list}")

my_copied_list = my_list[:]
print(f"is my_list is my_copied_list (as it is copy): {my_list is my_copied_list}")

my_copied_list2 = my_list.copy()
print(f"my_copied_list2 {my_copied_list2}"
      f" my_list {my_list}")

my_copied_list3 = list(my_list)
print(f"my_copied_list3 {my_copied_list3}"
      f" my_list {my_list}")

# SHALLOW COPY
my_copied_list3.append(1000000)
print(my_copied_list3)
print(my_list)
my_list[3] = 1099
print(my_copied_list3)  # works as expected
print(my_list)   # works as expected


list_of_list = [[1, 3, 4], [0, 9, 8, 4], [300, 301, 302, 303]]
new_list_of_list = list_of_list[:]
print(new_list_of_list)
list_of_list[0] = [0]
print(list_of_list)
print(new_list_of_list)

new_list_of_list_using_copy = list_of_list.copy()
print("list_of_list", list_of_list)
print("new_list_of_list_using_copy", new_list_of_list_using_copy)
list_of_list[0][0] = 99999
print("list_of_list", list_of_list)
print("new_list_of_list_using_copy", new_list_of_list_using_copy)

random = "this is a random text"
random_list = random.split()
print("index of this is", random_list.index("this"))
print("count of this is", random_list.count("is"))
print("does random_list contains mango?", "mango" in random_list)
print("does random_list contains random?", "random" in random_list)

# how list.sort() works?
h = "I am bad or good depends on many of the presumably good factors chosen randomly. Right?".split()
h.sort()
print(h)
h.sort(key=len)  # callable function len
print("Sorted on callable function len", h)
print(' '.join(h))

k = sorted(h)
print(k)
print("Does sorted() create new instance: ", k != h)

r = reversed(h)
print(r)  # this return an iterator, to create a new list pass it to a list
print(list(r))  # new list is created passing an iterator to list

# List Comprehension Syntax
a = "this is really not so log string"
ar = [len(word) for word in a.split()]
print("list prepared using list comprehension syntax", ar)


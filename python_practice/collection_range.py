r = range(5, 10)
for element in r:
    print(element)


for element in range(1, 20, 2):
    print(element)


elements = [1, 2, 4, 5, 0, -100]
for element in enumerate(elements):
    print("*" * len(elements))
    print(element)
    print(element[0], element[1])

for i, v in enumerate(elements):
    print("value: ", v)
    print("index: ", i)

    print(f"index is {i} value is {v}")



count = 10


def change_count(number):
    count = number


def change_global_count(number):
    global count  # this forces the use of module/global level count
    count = number


change_count(5)  # this will not change the count at module level
print(count)  # this will print 10 as global count is not modified by previous call

change_global_count(7)
print(count)

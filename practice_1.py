# practice_1
# map
# make a list to replace numbers big and small between 0 to 50 to 100 with map and lambda function

my_list = [1, 4, 6, 9, 44, 66, 88, 99, 12, 34, 56, 78, 32, 41, 51, 67]
new_list = list(map(lambda x: "big" if x > 50 else "small", my_list))
print(new_list)


# sort this list by second arguments
my_list2 = [(1, 4), (5, 9), (6, 3)]
my_list2.sort(key=lambda x: x[1])
print(my_list2)


# write a generator to take a number and give 0 to number


def first_number(number):
    num = 0
    while num < number:
        yield num
        num += 1


for i in first_number(10):
    print(i)

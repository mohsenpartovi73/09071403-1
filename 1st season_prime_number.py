# first practice of maktabkhone
def maghsom_al(numbers):
    list_maghsom = []
    for maghsom in range(1, numbers):
        if numbers % maghsom == 0:
            list_maghsom.append(maghsom)
    list_maghsom.append(numbers)
    return list_maghsom


def adad_aval(numbers):
    list = []
    for num in range(1, numbers + 1):
        if numbers % num == 0:
            list.append(num)
    if len(list) == 2:
        print("prime")
    else:
        print("not prime")


number = []
for i in range(5):
    numbers = int(input("Enter a number: "))
    number.append(numbers)

max_number = max(number, key=lambda x: (adad_aval(x), x))
max_count = adad_aval(max_number)

print(f"bishtarin maghsom adad aval ra {max_number} darad ba {max_count} adad aval.")

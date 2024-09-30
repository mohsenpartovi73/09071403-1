def printer(lists):
    for list in lists:
        print(list[0], list[1], list[2])


lists_female = []
lists_male = []
tedad = int(input("how many you are:"))
for i in range(tedad):
    name = input("what is your name:").title()
    gender = input("what is your gender(male or female):")
    language = input("what is your program language:")
    if gender == "female":
        lists_female.append((name, gender, language))
    else:
        lists_male.append((name, gender, language))

print(lists_female, "\n", lists_male)

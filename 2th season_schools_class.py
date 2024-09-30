class School:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

    def ages(age):
        age_list = []
        num = int(input("how many student :"))
        for i in range(num):
            age = int(input("plz insert students ages:"))
            age_list.append(age)
        # printer_age = print('age_list of students :',age_list)
        # return printer_age
        return age_list

    def heights(height):
        height_list = []
        num = int(input("how many student :"))
        for i in range(num):
            height = int(input("plz insert students height:"))
            height_list.append(height)
        # printer_height = print('height_list of students :',height_list)
        # return printer_height
        return height_list

    def weights(weight):
        weight_list = []
        num = int(input("how many student :"))
        for i in range(num):
            weight = int(input("plz insert students weight:"))
            weight_list.append(weight)
        # printer_weight = print('weight_list of students :',weight_list)
        # return printer_weight
        return weight_list

    def average(my_list):
        sum_list = sum(my_list)
        average_list = sum_list / (len(my_list))
        # rinter_avg = print(average_list)
        # return printer_avg
        return average_list

    # class_num = int(input('how many class : '))

    print("age average class :", float(average(ages(1))))
    print("height average class :", float(average(heights(1))))
    print("weight average class :", float(average(weights(1))))
    # print('age average of first class is {} and for height is {} and weight is {}'.format(a,b,c))

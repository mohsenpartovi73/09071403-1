# practice_2


class Human:
    def __init__(self, gender, blood, identical_num):
        self.gender = gender
        self.blood = blood
        self.identical_num = identical_num

    def print_human(self):
        print(
            "this {x} blood is {y} and his/her id is {z} ".format(
                x=self.gender, y=self.blood, z=self.identical_num
            )
        )


human = Human("male", "B+", "431")
human.print_human()



class computer:
    def __init__(self,ram,hard,size):
        self.ram = ram
        self.hard = hard
        self.size = size

    def price(self):
        return self.hard + self.ram + self.size
        

hard = int(input('what:'))
ram =int(input('what:'))
size = int(input('what:'))
pc = computer(hard,ram,size)
print(pc.price())

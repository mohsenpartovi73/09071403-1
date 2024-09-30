import random
class Person:
    def __init__(self,name):
        self.name = name


        def printer(self):
            return self.name
        
class Footbal(Person):

    players_list = ['mohsen','amir','ali','sadegh','sina','jaber','ahmad','reza','milad','ashkan']
    random.shuffle(players_list)
    count = -1
    player = []
    for i in range(10):
        count += 1
        print(i+1,players_list[count])



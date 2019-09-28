#
#
class Critter(object):
#
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def talk(self):
        print('Меня зовут,', self.name)
def main():
    crit1 = Critter('')
    crit1.talk()
    crit2 = Critter('')
    crit2.talk()
main() 

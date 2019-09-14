#Моя зверюшка
#Конструктор

class Critter(object):
    #Виртуальный питомец
    def __init__(self):
        print('Появилась на свет зверюшка')
    def talk(self):
        print('Привет я зверюшка')
def main():
    crit1 = Critter()
    crit2 = Critter()
    crit1.talk()
    crit2.talk()
main()
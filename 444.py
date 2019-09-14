#Статические атрибуты и методы класса
class Critter(object):
    #
    total = 0
    @staticmethod
    def status():
        print('Общее число зверюшек',Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1
        
    def __str__(self):
        ans = "Объект класса Critter\n"
        ans += 'имя ' + self.name + "\n"
        return ans

    def talk(self):
         print('Меня зовут,', self.name)

def main():
    print('Доступ к атрибуту класса Critter.total', end = " ")
    print(Critter.total)
    print('создание зверушек')
    crit1=Critter('Зверушка 1')
    crit2=Critter('Зверушка 2')
    crit3=Critter('Зверушка 3')

    Critter.status()
    print('Доступ к атрибуьу классак через обект:', end=" ")
    print(crit1.total)
main()
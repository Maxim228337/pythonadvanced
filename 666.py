#Настроение
#Свойства

class Critter(object):
    #
    total = 0
    @staticmethod
    def status():
        print('Общее число зверюшек',Critter.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1
        
    def __str__(self):
        ans = "Объект класса Critter\n"
        ans += 'имя ' + self.name + "\n"
        return ans
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть одной строкой.")
        else:
            self.__name = new_name
            print("имя успешно изминено.")
    @property
    def mood(self):
        unhapiness = self.hunger + self.boredom
        if unhapiness < 5:
            m = "прекрасно"
        elif 5 <= unhapiness <= 10:
            m="Неплохо"
        elif 11<= unhapiness <= 15:
            m = 'Не особо'
        else:
            m = 'ужасно'
        return m        
    def talk(self):
         print('Меня зовут,', self.name)

def main():
    print('создание зверушек')
    crit1=Critter('Зверушка 1')
    crit2=Critter('Зверушка 2')
    crit3=Critter('Зверушка 3')

    Critter.status()
    print('Доступ к свойству объекта:', crit1.mood)
main()
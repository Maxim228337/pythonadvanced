<<<<<<< HEAD
import random
=======
from random import randint
b = {}
>>>>>>> 285c1c5461685b5bd3f7e6d46b778b041b9cbac2
class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod   
    def status():
        print("Общее число зверюшек", Critter.total)

<<<<<<< HEAD
    def __init__(self, name, hunger = 0, boredom = 0):
=======
    def __init__(self, name, hunger = 0, boredom =0):
>>>>>>> 285c1c5461685b5bd3f7e6d46b778b041b9cbac2
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Critter.total += 1
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверушки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    def talk(self):
        print("Меня зовут", self.name)
    


    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self,):
<<<<<<< HEAD
        self.hunger -= int(input())
=======
        self.hunger -= int(input("Сколько кормить? "))
>>>>>>> 285c1c5461685b5bd3f7e6d46b778b041b9cbac2
        print("Мррр...  Спасибо!")
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
<<<<<<< HEAD
        self.boredom -= int(input())
=======
        self.boredom -= int(input('Сколько Играть? '))
>>>>>>> 285c1c5461685b5bd3f7e6d46b778b041b9cbac2
        print("Уиии!")
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
<<<<<<< HEAD
=======
    
>>>>>>> 285c1c5461685b5bd3f7e6d46b778b041b9cbac2
    def __str__(self):
        a = "Имя зверушки: " + str(self.name) + '\n' + "Голод зверушки: " + str(self.hunger) + '\n' +  "Скука зверушки: " + str(self.boredom) + '\n'+"Настроение зверушки: " + str(self.mood) + '\n'
        return a
  
def main():
<<<<<<< HEAD
    crit_name = input("Как вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)
=======
    
    for i in range(5):
        crit_name = input("Как вы назовете свою зверюшку?: ")
        b.append(Critter(crit_name,randint(0,10),randint(0,10)))
>>>>>>> 285c1c5461685b5bd3f7e6d46b778b041b9cbac2

    choice = None  
    while choice != "0":
        print \
        ("""
        Моя зверюшка
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
<<<<<<< HEAD
=======
        4 - Конкретная зверушка
>>>>>>> 285c1c5461685b5bd3f7e6d46b778b041b9cbac2
        """)
    
        choice = input("Ваш выбор: ")
        print()

        # выход
        if choice == "0":
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == "1":
<<<<<<< HEAD
            crit.talk()
        
        # кормление зверюшки
        elif choice == "2":
            crit.eat()
         
        # игра со зверюшкой
        elif choice == "3":
            crit.play()
        
        elif choice == "secret":
            print(crit)
=======
            for elem in b:
                elem.talk()
        
        # кормление зверюшки
        elif choice == "2":
            for elem in b:
                elem.eat()
         
        # игра со зверюшкой
        elif choice == "3":
            for elem in b:
                elem.play()
        
        elif choice == "secret":
            for elem in b:
                 print(elem)

>>>>>>> 285c1c5461685b5bd3f7e6d46b778b041b9cbac2

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)
    
main()
# Моя зверюшка
3
class Critter(object):
    # Виртуальлный питомец
    def talk(self):
        print('Привет, Im зверюшка')
def main():
    crit=Critter()
    crit.talk()
main()
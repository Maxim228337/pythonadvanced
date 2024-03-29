# Блек Джек

import cards, games

class BJ_Card(cards.Positionable_Card):
    ACE_VALUE = 1

    @property 
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):        
    def populate(self):
            for suit in BJ_Card.SUITS:
                for rank in BJ_Card.RANKS: 
                    self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + "\t" + super(BJ_Hand, self).__str__()
        if self.total != 21 :
            rep += "(" + str(self.total) + ")"
        else:
            rep += "Поздравляю у вас 21 очко"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        contains_ace = False
        for card in self.cards:
            t += card.value
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and t <= 11:
            t+=10
        return t
    def is_busted(self):
        return self.total > 21
    def is_lucky(self):
        return self.total == 21



class BJ_Player(BJ_Hand):
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ",будете брать еще карты, на данный момент у вас (" + str(self.total) + ") очков")
        return response == "y"
    
    def bust(self):
        print(self.name, "Перебрал.")
        self.lose()
    def lose(self):
        print(self.name, "Проиграл.")
    def win(self):
        print(self.name, "Выиграл.")
    def push(self):
        print(self.name, "Сыграл в ничью с дилером.")
    def luck(self):
        print(self.name, "Везунчик у него 21")



class BJ_Dealer(BJ_Hand):

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "Перебрал.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
        


class BJ_Game:

    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Diler")
    
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting() and not player.is_lucky():
                self.deck.deal([player])
                print(player)
                if player.is_busted():
                    player.bust()
        if player.is_lucky:
            player.luck()

    
    def play(self):
        #сдача всем по две карты
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        #Первая карта дилера переворачивается
        for player in self.players:
            print(player)
        print(self.dealer)

        #Сдача дополнительных карт игрокам
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card() #Первая карта дилера раскрываеться

        if not self.still_playing:
            #Все игроки перебрали покажем только руку дилера
            print(self.dealer)

        else:
            #Сдача дополнительніх карт дилеру
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                #Выигрывают все кто еще в игре
                for player in self.still_playing:
                    player.win()
            else:
                #Сравниваем суммы очков
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

            #Удаление всех карт
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tДобро пожаловать в игру Блек-Джек!\n")

    names = []
    number = games.ask_number("Сколько всего игроков? (1-7):", low = 1, high = 7)
    for i in range(number):
        name = input("Введите имя игрока №" + str(i+1)+" :")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\n Хотите еще раз?")

main()
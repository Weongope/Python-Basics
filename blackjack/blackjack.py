import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"

#c = Card("Hearts","Five")

class Deck():
    def __init__(self):
        self.deck = []     #start with an empty list(deck)
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
             deck_comp += "\n" + card.__str__()
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
'''
d = Deck()
d.shuffle()
'''
class Hand:
    def __init__(self):
        self.cards = []     # start with an empty list as we did in the Deck class
        self.value = 0      # start with zero value
        self.aces = 0       # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjuct_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

'''
#player
test_player = Hand()
#Deal one card from the deck
pulled_card = test_deck.deal()
test_player.add_card(pulled_card)
'''
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Place your bet: "))
        except ValueError:
            print("Error. Please give a number representation. ")
            continue
        else:
            if chips.bet <= chips.total:
               # return chips.bet
                break
            else:
                print(f"Funds Unavailable. You only have {chips.total}")

def hit(deck, hand):
    pulled_card = deck.deal()
    hand.add_card(pulled_card)
    hand.adjuct_for_ace()

#(hit(test_deck, test_player))

def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        player_choice = input("Hit or Stand: (h/s)").upper()
        if player_choice[0] == 'H':
            hit(deck,hand)
        elif player_choice[0] == 'S':
            print("Dealer's turn")
            playing = False
        else:
            print("Please provide h or s! ")
            continue

        break

def show_some(player, dealer):
    print("The Dealer's hand: <hidden card> ", end = "")
    for card in dealer.cards:
        if not dealer.cards.index(card) == 0:
            print(card, sep = ",")

    print("Player's Cards: ",end = "")
    for card in player.cards:
        print(card, end = ", ")
    print()
    dealer_total = dealer.value
    #print(f"\nThe dealer has {dealer_total}")
    player_total = player.value
   # print(f"You have {player_total}")

#show_some(test_player,dealer)

def show_all(player, dealer):
    print("Dealer's Cards")
    for card in dealer.cards:
        print(card, end=", ")
    print()
    print("Player's Cards")
    for card in player.cards:
        print(card, end=", ")
    print()
#show_all(test_player,dealer)

def player_busts(player,dealer, chips):
    print("PLAYER BUST!")
    chips.lose_bet()

def player_wins(player,dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player,dealer, chips):
    print("PLAYER BUST!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and player tie! PUSH")

def black_jack_game():
    while True:
        # Print an opening statement
        print("Wecome to our game of BlackJact. It has been made exactly for you! (by weongope)")
        # Create & shuffle the deck, deal two cards to each player
        game_deck = Deck()
        game_deck.shuffle()

        player = Hand()
        dealer = Hand()
        for i in range(1,3):
            player.add_card(game_deck.deal())
            dealer.add_card(game_deck.deal())
        # Set up the Player's chips
        player_chips = Chips()
        # Prompt the Player for their bet
        take_bet(player_chips)
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)

        while playing:
            # Prompt for Player to Hit or Stand
            hit_or_stand(game_deck, player)
            # Show cards (but keep one dealer card hidden)
            show_some(player,dealer)
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.value > 21:
                player_busts(player,dealer,player_chips)

                break
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player.value <= 21:

            while dealer.value < 17:
                hit(game_deck,dealer)

            # Show all cards
            show_all(player, dealer)
            # Run different winning scenarios
            if dealer.value > 21:
                dealer_busts(player,dealer,player_chips)
            elif dealer.value > player.value:
                dealer_wins(player,dealer,player_chips)
            elif dealer.value < player.value:
                player_wins(player,dealer,chips)
            else:
                push(player,dealer)
        # Inform Player of their chips total
        print(f"\n Player has {player_chips.total} chips.")

        # Ask to play again
        new_game = input("Would you like to play another game? (y/n)")

        if new_game[0].upper() == "Y":
            playeing = True
            continue
        else:
            print("Thank you for the game!")
            break


black_jack_game()

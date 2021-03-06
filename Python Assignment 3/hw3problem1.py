# Natalya Tulloch
# 112791014
#ntulloch
#
# IAE 101 (Fall 2019)
# HW 3, Problem 1

# DON'T CHANGE OR REMOVE THIS IMPORT
from random import shuffle

# DON'T CHANGE OR REMOVE THESE LISTS
# The first is a list of all possible card ranks: 2-10, Jack, King, Queen, Ace
# The second is a list of all posible card suits: Hearts, Diamonds, Clubs, Spades
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "D", "C", "S"]

# This class represents an individual playing card
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank# REMOVE THIS AND REPLACE WITH YOUR CODE

    # DON'T CHANGE OR REMOVE THIS
    # This function creates a string out of a Card for easy printing.
    def __str__(self):
        return "[" + self.suit + ", " + self.rank + "]"

# This class represents a deck of playing cards
class Deck(cards):
    def __init__(self):
        self.cards = cards
        cards = []
        for s in suits:
            for r in ranks:
                if r != s:
                    cards.append((s,r))
        # REMOVE THIS AND REPLACE WITH YOUR CODE

    # DON'T CHANGE OR REMOVE THIS
    # This function will shuffle the deck, randomizing the order of the cards
    # inside the deck.
    # It takes an integer argument, which determine how many times the deck is
    # shuffled.
    def shuffle_deck(self, n = 5):
        for i in range(n):
            shuffle(self.cards)

    # This function will deal a card from the deck. The card should be removed
    # from the deck and added to the player's hand.
    def deal_card(self, player, hand):
        self.player = player
        self.hand = hand
        self.hand = []
        hand.add(cards[0])# REMOVE THIS AND REPLACE WITH YOUR CODE

    # DON"T CHANGE OR REMOVE THIS
    # This function constructs a string out of a Deck for easy printing.
    def __str__(self):
        res = "[" + str(self.cards[0])
        for i in range(1, len(self.cards)):
            res += ", " + str(self.cards[i])
        res += "]"
        return res

# This class represents a player in a game of Blackjack
class Player(hand, name, status):
    def __init__(self, name, hand, status):
        self.hand = hand
        self.name = name
        self.status = status
    name = ""
    hand = []
    status = True
    if sum(hand) > 21:
        status = False
        # REMOVE THIS AND REPLACE WITH YOUR CODE

    def value(self):
        while sum(hand) > 0 and sum(hand) < 21:
            return int(sum(hand))
        # REMOVE THIS AND REPLACE WITH YOUR CODE

    def choose_play(self):
        if player.hand =+ 1:
            print("Hit") # REMOVE THIS AND REPLACE WITH YOUR CODE
        else:
            print("Stay")

    # DON'T CHANGE OR REMOVE THIS
    # This function creates a string representing a player for easy printing.
    def __str__(self):
        res = "Player: " + self.name + "\n"
        res += "\tHand: " + str(self.hand[0])
        for i in range(1, len(self.hand)):
            res += ", " + str(self.hand[i])
        res += "\n"
        res += "\tValue: " + str(self.value())
        return res

# This class represents a game of Blackjack
class Blackjack(players, deck):
    def __init__(self, players):
        self.players = players # REMOVE THIS AND REPLACE WITH YOUR CODE
        players = []
        players.append(Player.object)

    def play_game(self):
        while num(Player) > 1 and Card() and Deck = 52:
           choose_play() # REMOVE THIS AND REPLACE WITH YOUR CODE

    #I have no idea what to do. This code doesn't work but I needed to submit something

    # DON'T CHANGE OR REMOVE THIS
    # This function creates a string representing the state of a Blackjack game
    # for easy printing.
    def __str__(self):
        res = "Current Deck:\n\t" + str(self.deck)
        res = "\n"
        for p in self.players:
            res += str(p)
            res += "\n"
        return res

# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    # Uncomment each section of test code as you finish implementing each class
    # for this problem. Uncomment means remove the '#' at the front of the line
    # of code.
    
    # Test Code for your Card class
    #c1 = Card("H", "10")
    #c2 = Card("C", "A")
    #c3 = Card("D", "7")

    #print(c1)
    #print(c2)
    #print(c3)

    print()

    # Test Code for your Deck class
    #d1 = Deck()
    #d1.shuffle_deck(10)
    #print(d1)

    print()

    # Test Code for your Player class
    #p1 = Player("Alice")
    #p2 = Player("Bob")
    #d1.deal_card(p1)
    #d1.deal_card(p2)
    #print(p1.value())
    #print(p2.value())
    #d1.deal_card(p1)
    #d1.deal_card(p2)
    #print(p1.value())
    #print(p2.value())
    #d1.deal_card(p1)
    #d1.deal_card(p2)
    #print(p1.value())
    #print(p2.value())
    #print(p1)
    #print(p2)
    #print(p1.choose_play())
    #print(p2.choose_play())

    print()

    # Test Code for your Blackjack class
    #players = [Player("Summer"), Player("Rick"), Player("Morty"), Player("Jerry")]
    #game = Blackjack(players)
    #print(game)
    #game.play_game()
    #print(game)

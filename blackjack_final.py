# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome, status = "", ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.contains_ace = False

    def __str__(self):
        output = "Hand contains "
        for card in self.cards:
            output = output + str(card) + ' '
        return output

    def add_card(self, card):
        self.cards.append(card)
        self.contains_ace = self.contains_ace or card.get_rank() == RANKS[0]

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0        
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
        if (self.contains_ace and hand_value + 10 <= 21):
            hand_value += 10
        return hand_value  
    
    def is_busted(self):
        return self.get_value() > 21
   
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos = (pos[0] + CARD_SIZE[0] + 10, pos[1])
         
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        output = "Deck contains "
        for card in self.deck:
            output = output + str(card) + ' '
        return output

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, score, status
    if (in_play):
        outcome = "New Deal?"
        in_play = False
        score -= 1
        status = "You lose."
    else:
        status = ""
        outcome = "Hit or stand?"
        player_hand = Hand()
        dealer_hand = Hand()    
        deck = Deck()
        deck.shuffle()    
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        in_play = True

def hit(): 
    global player_hand, score, in_play, deck, outcome, status
    if (in_play):
        player_hand.add_card(deck.deal_card())
        if (player_hand.is_busted()):
            in_play = False
            score -= 1     
            status = "You went bust and lose."
            outcome = "New Deal?"
       
def stand():    
    global in_play, dealer_hand, score, outcome, status
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if (in_play):
        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(deck.deal_card())
        if (dealer_hand.is_busted() or dealer_hand.get_value() < player_hand.get_value()):
            score += 1
            status = "You win."
        else:
            score -= 1
            status = "You lose."
        in_play = False
        outcome = "New Deal?"        

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [50, 50], 40, 'Aqua')
    canvas.draw_text("Dealer", [50, 130], 30, 'Black')
    canvas.draw_text(status, [200, 130], 30, 'Black')
    canvas.draw_text("Player", [50, 380], 30, 'Black')
    canvas.draw_text(outcome, [200, 380], 30, 'Black')
    canvas.draw_text("Score: " + str(score), [300, 50], 30, 'Black')    
    dealer_hand.draw(canvas, [50, 150])
    player_hand.draw(canvas, [50, 400])
    if (in_play):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_BACK_CENTER[0], 150 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

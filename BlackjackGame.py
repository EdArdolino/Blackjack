#Simple game of Blackjack 

##Plan##
#Dealer(House) and a Player
#Deal cards
#Display cards for the dealer and player
#Count card totals
#Hit or stand
#Over 21 is Bust 
#Dealer cards == Player cards (value) = Push 

import random

#Created Dealer and Player Cards
dealer_cards = []
player_cards = []

#Dealer Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer showing X & ", dealer_cards[1])

#Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("Player showing: ", player_cards)

#Sum Dealer Cards
if sum(dealer_cards) == 21:
    print("Dealer shows 21, Dealer wins.")
elif sum(dealer_cards) > 21:
    print("Dealer busted")

#Sum Player Cards
while sum(player_cards) < 21:
    action_taken = str(input("Stay or Hit?"))
    if action_taken == "Hit":
        player_cards.append(random.randint(1,11))
        print("Now showing: " + str(sum(player_cards)) + " with ", player_cards)
    else:
        print("Dealer shows: " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("Player shows: " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins")
        else:
            print("Player wins")
            break

#Determine Player counts
if sum(player_cards) > 21:
    print("Player busts, dealer wins")
elif sum(player_cards) == 21:
    print("Blackjack, player wins")
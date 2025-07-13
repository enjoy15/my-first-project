#  packages imports
import os
import random
import colorama
from colorama import Fore

os.system('cls')

# set up the game
suits = ("Hearts", "Clubs", "Diamonds", "Spades")
numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]


# define variables
player1_card = ()
player2_card = ()

player1_pack = []
player2_pack = []



# create card deck
def create_deck():
    deck = []
    for suit in suits:
        for number in numbers:
            card = (number,suit)
            deck.append(card)
    
    # print("deck = ",deck)
    random.shuffle(deck)
    # print("==============")
    # print("==============")
    # print(" shuffled deck = ",deck)
    return deck


# process card number
def process_card(card_number):
    if card_number == 11:
        return "Jack"
    if card_number == 12:
        return "Queen"
    if card_number == 13:
        return "King"
    if card_number == 14:
        return "Ace"
    else:
        return card_number


# creating a deck
deck_of_cards = create_deck()


# GAME LOGIC (LOOP)

while len(deck_of_cards) > 1:

    input(f"{Fore.WHITE}\npress enter to deal cards")
    
    os.system("cls")
    
    # deal the cards and remove them from the card deck
    player1_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player1_card)
    
    player2_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player2_card)
    
    # process picture cards
    p1_card_name = process_card(player1_card[0])
    p2_card_name = process_card(player2_card[0])
    
    
    # if player1 wins
    if player1_card[0] > player2_card[0]:
        
        # display cards
        print(f"{Fore.GREEN}Player1 card: {p1_card_name} of {player1_card[1]}")
        print(f"{Fore.RED}Player2 card: {p2_card_name} of {player2_card[1]}")
        
        
        print(f"{Fore.YELLOW}Player1 wins this hand")
        
        # add to a winning pack
        player1_pack.append(player1_card)
        player1_pack.append(player2_card)
        
        
    # if player2 wins
    elif player1_card[0] < player2_card[0]:
        
        # display cards
        print(f"{Fore.GREEN}Player1 card: {p1_card_name} of {player1_card[1]}")
        print(f"{Fore.RED}Player2 card: {p2_card_name} of {player2_card[1]}")
        
        
        print(f"{Fore.YELLOW}Player2 wins this hand")
        
        # add to a winning pack
        player2_pack.append(player1_card)
        player2_pack.append(player2_card)   
        
    # if its a draw
    else:
        
        # display cards
        print(f"{Fore.GREEN}Player1 card: {p1_card_name} of {player1_card[1]}")
        print(f"{Fore.RED}Player2 card: {p2_card_name} of {player2_card[1]}")
        
        print(f"{Fore.YELLOW} it is a Draw!")
        
        
        # add to a winning pack
        player1_pack.append(player1_card)
        player2_pack.append(player2_card)
    
    
    # display number of cards in a deck
    print(f"\n{Fore.BLUE} Number of the cards left: {len(deck_of_cards)}")
# END OF LOOP


# determine the winner

if len(player1_pack) > len(player2_pack):
    # player1 wins:
    print(f"{Fore.YELLOW} Player1 wins the game with {len(player1_pack)} cards over {len(player2_pack)} cards")

elif len(player1_pack) < len(player2_pack):
    # player2 wins:
    print(f"{Fore.YELLOW} Player2 wins the game with {len(player2_pack)} cards over {len(player1_pack)} cards")

else:
    # if its a draw
    print(f"{Fore.YELLOW} its a draw")
    


# END of a GAME

if input(f"{Fore.WHITE}\nwould you like to see the players packs (y/n)").lower() == "y":
    # display the cards in the player packs
    
    for card in player1_pack:
        print(f"{Fore.MAGENTA}Player1 pack: {process_card(card[0])} of {card[1]}")
    
    
    for card in player2_pack:
        print(f"{Fore.CYAN}Player2 pack: {process_card(card[0])} of {card[1]}")
    
    print(f"{Fore.RED}\nThank you for Playing!")

else:
     print(f"{Fore.RED}\nThank you for Playing!")
    
        



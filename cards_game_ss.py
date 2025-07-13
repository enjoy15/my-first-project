#packages imports
import os
import random
import colorama import Fore

os.system('clear')

#set up the game
suits = ('Hearts','Clubs','Dismonds','Spades')
numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]

#define variables
player1_card =()
player2_card =()

player1_pack = []
player2_pack = []

#create card deck
def create_deck():
    deck = []
    for suit in suits:
        for number in numbers:
            card = (number,suit)
            deck.append(card)
    print('deck =', deck)
    random.shuffle(deck)
    # print("-----------------------")
    # print("=======================")
    # print('shuffled deck =',deck)
    return deck


def process_card(card_number):
    if card_number == 11:
        return 'Jack'
    if card_number == 12:
        return 'Queen'
    if card_number == 13:
        return 'King'
    if card_number == 14:
        return 'Aid'   
    else:
        return card_number 

#create a deck
deck_of_cards = create_deck()

#GAME LOGIC (LOOP)

while len(deck_of_cards) > 1: 
    input(f'{Fore.WHITE}\n press enter to deal cards')

    os.system('clear')

    #deal the cards and remove them for the card deck
    player1_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player1_card)

    player2_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player1_card)

    p1_card_name = process_card(player1.card[0])
    p2_card_name = process_card(player2.card[0])

    #if player1 wins
    if player1_card[0] > player2_card[0]:

        print(f'{Fore.GREEN}Player1 card: {p1_card_name} of {player1_card}')
        print(f'{Fore.RED}Player2 card: {p2_card_name} of {player2_card}')

        print(f'{Fore.YELLOW}Player 1 wins this hand')

        #add to a winning pack
        player1_pack.append(player1_card)
        player2_pack.append(player2_card)


    #if player2 wins        
    elif player1_card[0] < player2_card[0]:
        #display cards
        print(f'{Fore.GREEN}Player1 card: {p1_card_name} of {player1_card}')
        print(f'{Fore.RED}Player2 card: {p2_card_name} of {player2_card}')
      
        print(f'{Fore.YELLOW}Player 2 wins this hand')
        #add to a winning pack
        player1_pack.append(player1_card)
        player2_pack.append(player2_card)

    else:
        print(f'{Fore.GREEN}Player1 card: {p1_card_name} of {player1_card}')
        print(f'{Fore.RED}Player2 card: {p2_card_name} of {player2_card}')

        print(f'{Fore.YELLOW} It is a draw')

        
        player1_pack.append(player1_card)
        player2_pack.append(player2_card)

    #display number of cards in a deck
    print(f'\n Fore.BLUE Number of the cards left: (len(deck_of_card))')

#END OF LOOP

#determine the winner

if len(player1_pack) > len(player2_pack):
    print(f'{Fore.YELLOW} Player1 win the game with {len{player1_pack} cards over {len(player2_pack)}} cards')

elif len(player1_pack) > len(player2_pack):
    print(f'{Fore.YELLOW} Player1 win the game with {len{player1_pack} cards over {len(player2_pack)}} cards')
else:

#END of a GAME

if input(f'{FORE.WHITE}\n would you like to see the player packs(y/n)').upper() =='Y':
    #display the card in the player packs
    for card in player1_pack:
        print(f'{Fore.MAGENTA}Player 1 pack:{process_card[0]} of {card[1]}')

    for card in player2_pack:
        print(f'{Fore.CYAN}Player 2 pack:{process_card[0]} of {card[1]}')
    print(f'{Fore.RED}\n Thank you for playing!')

else:
    print(f'{Fore.RED}\n Thank you for playing')
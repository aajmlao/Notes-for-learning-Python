import random
from colorama import Fore, Style

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')# initialization for the value of the cards
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')# initialization for the value of the cards
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11} # initialization for the value of the cards

class Player:

    def __init__(self, name, BotName='Gigi'):
        self.name = name
        self.BotName = BotName

class Card:
    """Describe one card."""
    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = values[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit

class Deck:
    """Set up the Deck for 52 Cards. Shuffle Deck and draw Card"""
    def __init__(self) -> None:
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)


    def draw(self):
        return self.all_cards.pop()

def Ace(list_numbers,total_sum):
    """Operate Ace logic here"""
    if total_sum > 21:
        if 11 in list_numbers: # Do we need to converce to str?
            total_sum = total_sum -10
            out_result = True # Game continues
        else:
            out_result = False # Game ends
    else:
        out_result = True

    return out_result,total_sum

def sumup(player_cards):
    player_number = [] # Empty List for each run.
    for card in player_cards:
        try:
            card_rank = card.__str__().replace('of',"") # split into a list
            temp_rank,temp_suit = card_rank.split()
            card_values = Card(temp_suit,temp_rank) # Call the class
            card_value = card_values.value
        except:
            card_value = card
            
        player_number.append(card_value)
        total_sum = sum(player_number)
    
    return total_sum,player_number

# Game begins 
print("Welcome to BlackJack Simple Demo!")
name = input("Please Enter Your Name: ")
initial_name = Player(name)
print(f'Hey, My name is {initial_name.BotName}. I will be you dealer. Good luck!')
player_cards = []
dealer_cards = []
game_on = True
new_card = Deck() # We need to run this for only one time.
new_card.shuffle()
while game_on:
    
    # Initialize the game and send 2 cards to each player. 
    if len(player_cards) < 2: # once player gets one card, and dealer get one card too. 
        player_cards.append(new_card.draw()) # player gets two cards

        dealer_cards.append(new_card.draw()) # dealer gets two cards
    
    elif len(player_cards) >=2: # more than 2 cards go here 
        print(dealer_cards[0], " + Unknown")
        print(player_cards[0]," + ",player_cards[1])
        # Choice Hit or Stay: ask this qustion until user input stay
        add_card = input('Hit or Stay: ')
        while add_card == 'Hit':
            player_cards.append(new_card.draw())
            for card in player_cards:
                print(Fore.GREEN,card)
            print(Style.RESET_ALL)
            add_card = input('Choice: Hit or Stay: ')
        # End
        # Break down a card

        # These lines are to get card value.
        total_sum,player_number = sumup(player_cards)

      
        if total_sum == 21:
            print('You win. You have 21 first.')
            break
        #End
        # Check Player Busted, End the game if it happend
        game_on,total_sum = Ace(player_number,total_sum)
        if game_on == False:
            print(Fore.RED,f"Game is over. {initial_name.name} busted. Dealer win")
            break
        elif total_sum > 21:
            print(Fore.RED,f"Game is over. {initial_name.name} busted at {total_sum}. Dealer win")
            break
        
        print(Fore.BLUE,f"{initial_name.name} has {total_sum} point.")
        print(f"{Fore.BLUE}{Style.RESET_ALL}")
        # Dealer play (Bot)
        print(f'{initial_name.BotName} turns.')
        total_sum_bot,bot_number = sumup(dealer_cards)
        if total_sum_bot == 21:
            print(Fore.RED,f'You lose. {initial_name.BotName} has 21')
            break
        
        while total_sum_bot < 21 and game_on == True:
            # total sum need to less than 21 and bigger than 18. 
            if total_sum_bot  < 18:
                bot_draw_card = new_card.draw()

                dealer_cards.append(bot_draw_card)

                total_sum_bot, dealer_cards = sumup(dealer_cards)
                game_on,total_sum_bot = Ace(dealer_cards,total_sum_bot)

            elif total_sum_bot > 21:
                print(Fore.RED,f'{initial_name.name} win!')
                break
            else:
                game_on = False
        else:
            if total_sum_bot > 21:
                print(Fore.RED,f"{initial_name.BotName} has {total_sum_bot}. {initial_name.BotName} Busted. {initial_name.name} win!")
                break

        # If there is no Busted, Run this block
        if total_sum > total_sum_bot:
            print(Fore.RED,f'{initial_name.name} has {total_sum}, and {initial_name.BotName} has {total_sum_bot}. {total_sum} > {total_sum_bot}. {initial_name.name} win!')
            break
        elif total_sum < total_sum_bot:
            print(Fore.RED,f'{initial_name.name} has {total_sum}, and {initial_name.BotName} has {total_sum_bot}. {total_sum} < {total_sum_bot}. {initial_name.BotName} win!')
            break
        elif total_sum == total_sum_bot:

            print(Fore.RED,f'{initial_name.name} has {total_sum}, and {initial_name.BotName} has {total_sum_bot}. {total_sum} < {total_sum_bot}. Game Tie')
            break
        else:
            print('Something Wrong. ENDING GAME!')
            break
        # End





        
        


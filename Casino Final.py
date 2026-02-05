import random
import json
import os

SAVE_FILE = "casino_data.json"

def load_tokens():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                return json.load(f).get("tokens", 100)
        except:
            return 100
    return 100

def save_tokens(tokens):
    with open(SAVE_FILE, "w") as f:
        json.dump({"tokens": tokens}, f)


def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

def calculate_score(hand):
    score = sum(card_value(card) for card in hand)
    # Check for aces to reduce score if over 21
    aces = sum(1 for card in hand if card[0] == 'Ace')
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def Blackjack():
    tokens = load_tokens()
    print(f"Welcome to Blackjack! You have {tokens} tokens.")
    
    
    # Main loop of the game
    while True:
        if tokens <= 0:
            print("You have no tokens, heres 50 to kick start your gambling journey.")
            tokens == 50
            save_tokens(tokens)
        
        
        print(f"\n--- New Round (Tokens: {tokens}) ---")
        
        
        # Betting phase
        bet = input(f"Place your bet (1-{tokens}): ")
        if not bet.isdigit() or int(bet) > tokens or int(bet) <= 0:
            print("Invalid bet.")
            continue
        bet = int(bet)
        
        # Making the deck
        card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        deck = [(card, category) for category in card_categories for card in cards_list]
        random.shuffle(deck)
        
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        
        while True:
            player_score = calculate_score(player_hand)
            print("\nCards the player has:", player_hand)
            print("Score player has", player_score)
            
            if player_score >= 21:
                break
            
            choice = input('["hit" to request another card, "stand" to stop]: ').lower()
            if choice == "hit":
                player_hand.append(deck.pop())
            elif choice == "stand":
                break
            else:
                print("Invalid choice. Please try again.")

            
        dealer_score = calculate_score(dealer_hand)
        if player_score <= 21:
            while dealer_score < 17:
                dealer_hand.append(deck.pop())
                dealer_score = calculate_score(dealer_hand)
            

        print("Cards Dealer Has:", dealer_hand)
        print("Score Of The Dealer:", dealer_score)
        print("Cards Player Has:", player_hand)
        print("Score Of The Player:", player_score)
        
        # Results and the payout of said results.
        if player_score > 21:
            print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
            tokens -= bet   
        elif dealer_score > 21:
            print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)")
            tokens += bet
        elif player_score > dealer_score:
            print("Player wins (Player Has High Score than Dealer)")
            tokens += bet
        elif dealer_score > player_score:
            print("Dealer wins (Dealer Has High Score than Player)")
            tokens -= bet
        else:
            print("It's a tie.")
            
            
            
        save_tokens(tokens)
        print(f"Current Tokens: {tokens}")

        if tokens <= 0:
            print("You are out of tokens!")
            
        else:
            if input("\nWould you like to play again? (Y or N): ").lower() != "y":
                break
        
        
def Roulette():
    print("")
    
    
    
def Slots():
    print("Place holder for slots")
    
def Texas_Holdem():
    print("Place holder for texas holdem")
    
def craps():
    print("Place holder for craps")
    
    
    
Blackjack()
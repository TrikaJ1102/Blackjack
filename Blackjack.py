import random

# Constants
CHIPS = [1, 5, 25, 50, 100]
STARTING_BALANCE = 1000

# ASCII Art
def show_logo():
    print(''' _     _            _    _            _
| |   | |          | |  (_)          | |
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   <
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |
                      |__/                ''')
    print('''                            _
       ,'`.    _  _    /\    _(_)_
      (_,._)  ( `' )  <  >  (_)+(_)
        /\     `.,'    \/      |''')

# Card Functions
def create_deck():
    base_cards = [(2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),
                  (10, '10'), (10, 'J'), (10, 'Q'), (10, 'K'), (11, 'A')]
    return base_cards * 4

def calculate_total(hand):
    total = sum(card[0] for card in hand)
    aces = sum(1 for card in hand if card[1] == 'A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def display_hand(hand, owner="Player"):
    cards = ', '.join(f"{card[1]}({card[0]})" for card in hand)
    print(f"{owner}'s Hand: {cards} | Total: {calculate_total(hand)}")

def get_bet(balance):
    print(f"\nBank Balance: ${balance}")
    print("Available chips: 1 | 5 | 25 | 50 | 100")
    bet = 0

    choice = input("ALL IN or choose bet amount? ").lower()
    if choice == "all in":
        print(f"You went ALL IN with ${balance}!")
        return balance

    while True:
        try:
            chip = int(input("Place your bet (select one chip): "))
            if chip in CHIPS and chip <= balance:
                bet += chip
                balance -= chip
                more = input("Add more chips? (y/n): ").lower()
                if more != 'y':
                    break
            else:
                print("Invalid chip or over your balance.")
        except ValueError:
            print("Please enter a number.")
    return bet

def player_turn(deck, hand):
    while True:
        display_hand(hand)
        if calculate_total(hand) > 21:
            print("BUST!")
            return False
        choice = input("Hit or Stand? ").lower()
        if choice == 'hit':
            hand.append(deck.pop())
        elif choice == 'stand':
            return True
        else:
            print("Please enter 'hit' or 'stand'.")

def dealer_turn(deck, hand):
    print("\nDealer's turn:")
    display_hand(hand, "Dealer")
    while calculate_total(hand) < 17:
        new_card = deck.pop()
        hand.append(new_card)
        print(f"Dealer drew {new_card[1]} ({new_card[0]})")
    display_hand(hand, "Dealer")

def determine_winner(player_hand, dealer_hand, bet, balance):
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)

    print(f"\nFinal Results:")
    display_hand(player_hand, "Player")
    display_hand(dealer_hand, "Dealer")

    if player_total > 21:
        print("You busted. Dealer wins.")
        return balance - bet
    elif dealer_total > 21 or player_total > dealer_total:
        print(f"You win! You gained ${bet}.")
        return balance + bet
    elif player_total < dealer_total:
        print("Dealer wins.")
        return balance - bet
    else:
        print("It's a tie!")
        return balance  # No change

# Game Loop
def play_game():
    balance = STARTING_BALANCE
    show_logo()

    while balance > 0:
        deck = create_deck()
        random.shuffle(deck)

        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        bet = get_bet(balance)

        print(f"\nYour cards: {player_hand[0][1]}({player_hand[0][0]}), {player_hand[1][1]}({player_hand[1][0]})")
        print(f"Dealer shows: {dealer_hand[0][1]}({dealer_hand[0][0]}), [Hidden Card]")

        if not player_turn(deck, player_hand):
            balance -= bet
        else:
            dealer_turn(deck, dealer_hand)
            balance = determine_winner(player_hand, dealer_hand, bet, balance)

        print(f"\nYour current balance: ${balance}")
        if balance <= 0:
            print("You're out of money! Game over.")
            break

        again = input("Play another round? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    play_game()

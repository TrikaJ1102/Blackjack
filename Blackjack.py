print(''' _     _            _    _            _
| |   | |          | |  (_)          | |
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   <
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |
                      |__/                ''')
print('''                            _
       ,'`.    _  _    /\    _(_)_
      (_,._)  ( `' )  <  >  (_)+(_)
        /\     `.,'    \/      |''')



import random

def hit(hand_cards):
    while True:
        ncard = deck.pop()
        print(f"You drew: {ncard[1]}, (value:{ncard[0]})")
        hand_cards.append(ncard)
        total = calculation(hand_cards)
        print(f"Total Value: {total}")

        if total > 21:
            print("BUST!")
            return  # Exit hit if busted

        choice = input("Hit or Stand? ").lower()
        if choice == "stand":
            stand()
            return  # Exit hit if player stands

def stand():
    global balance
    while calculation(dealer_cards) < 17:
        ncard = deck.pop()
        print(f"Dealer drew {ncard[1]}, (value{ncard[0]})")
        dealer_cards.append(ncard)

    player_total = calculation(hand_cards)
    dealer_total = calculation(dealer_cards)

    print(f"\nYour final total: {player_total}")
    print(f"Dealers' final total: {dealer_total}")

    if player_total > 21:
        print("You Busted! Dealer wins.")
    elif dealer_total > 21:
        print("You win!")
    elif player_total < dealer_total <= 21:
        print("Dealer wins")
    elif player_total == dealer_total:
        print("It's a tie!")

def calculation(hand_cards):
    total = 0
    ace = 0
    for card in hand_cards:
        total += card[0]
        if card[1] == "A":
            ace += 1

    while total > 21 and ace > 0:
        total -= 10
        ace -= 1
    return total

balance = 1000

while True:
    cards = [(2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'),
             (10, '10'), (10, 'J'), (10, 'Q'), (10, 'K'), (11, 'A')]
    deck = cards * 4
    random.shuffle(deck)

    card1 = deck.pop()
    card2 = deck.pop()
    dcard1 = deck.pop()
    dcard2 = deck.pop()

    hand_cards = [card1, card2]
    dealer_cards = [dcard1, dcard2]

    print(f"\nBank Balance: ${balance}")
    print("Available chips: 1 | 5 | 25 | 50 | 100")

    betting = input("ALL IN or choose bet amount (press yes): ")
    bet = 0

    if betting.lower() == "all in":
        bet = balance
        print(f"You went all in with ${balance}!")
    else:
        bet = int(input("Place your bet (select one chip): "))
        addBet = input("Do you want to add more chips? y/n: ").lower()

        while addBet == "y":
            add = int(input("Place your bet (select one chip): "))
            bet += add
            addBet = input("Do you want to add more chips? y/n: ").lower()

    print(f"Total bet placed: ${bet}")

    print(f"You drew: {card1[1]}, (value:{card1[0]}) and {card2[1]}, (value:{card2[0]})")
    print(f"Dealer drew: {dcard1[1]}, (value:{dcard1[0]}) and a facedown card.")

    choice = input("Hit or Stand? ").lower()
    if choice == "hit":
        hit(hand_cards)
    else:
        stand()

    # Determine winner and update balance
    player_total = calculation(hand_cards)
    dealer_total = calculation(dealer_cards)

    if player_total > 21:
        balance -= bet
    elif dealer_total > 21 or player_total > dealer_total:
        print(f"You won ${bet}!")
    elif player_total < dealer_total:
        balance -= bet

    if balance == 0:
        print("Uh oh, Table won! You're out of money.")
        break

    game = input("Do you want to play again? (y/n): ").lower()
    if game != "y":
        break
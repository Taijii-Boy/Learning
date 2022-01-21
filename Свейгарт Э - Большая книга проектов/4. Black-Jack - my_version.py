import random
import sys


def show_rules():
    print('''Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.''')


def create_deck() -> list:
    card_names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suits = {'hearts': chr(9829), 'diamonds': chr(9830), 'spades': chr(9824), 'clubs': chr(9827)}
    deck = [(card, suit) for card in card_names for suit in list(card_suits.values())]
    random.shuffle(deck)
    return deck


def show_cards(some_cards: list, backside: bool = False):
    rows = ['', '', '', '']
    first_card = True
    for card in some_cards:
        name, suit = card
        if backside and first_card:
            rows[0] += ' ___  '
            rows[1] += f'|## | '
            rows[2] += f'|###| '
            rows[3] += f'|_##| '
            first_card = False
        elif name == '10':
            rows[0] += ' ___  '
            rows[1] += f'|10 | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|_10| '
        else:
            rows[0] += ' ___  '
            rows[1] += f'|{name}  | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|__{name}| '

    for row in rows:
        print(row)


def config_game(money: int):
    show_rules()
    print(f'Your money: {money}')


def get_player_cards(deck, player_hand: list, cards_count=1) -> tuple:
    for count in range(cards_count):
        player_hand.append(deck.pop())
    return deck, player_hand


def get_dealer_cards(deck, dealer_hand: list, cards_count=1) -> tuple:
    for count in range(cards_count):
        dealer_hand.append(deck.pop())
    return deck, dealer_hand


def get_bet(max_bet: int) -> int:
    while True:
        print(f'How much do you bet? (1-{max_bet}, or QUIT)')
        bet = input('> ')
        if 'q' in bet.lower():
            sys.exit()
        elif not bet.isdecimal():
            continue
        elif 1 <= int(bet) <= 5000:
            print("\nBet: ", bet)
            return int(bet)


def get_game_score(dealer_hand: list, player_hand: list) -> tuple:
    score_list = []
    for hand in [dealer_hand, player_hand]:
        score = 0
        for card in hand:
            if card[0] in 'JQK':
                score += 10
                continue
            elif card[0] == 'A':
                if score + 10 <= 21:
                    score += 10
                else:
                    score += 1
                continue
            score += int(card[0])
        score_list.append(score)
    return score_list[0], score_list[1]  # (dealer_score, player_score)


def check_score(dealer_score: int, player_score: int, game_continue: bool = True) -> str:

    if (dealer_score == 21 and dealer_score != player_score) or (
            not game_continue and (21 < dealer_score < player_score)):
        return 'dealer_win'
    elif (player_score == 21 and player_score != dealer_score) or (
            not game_continue and (21 < player_score < dealer_score)):
        return 'player_win'
    return 'continue'


def show_game_table(dealer_hand: list, dealer_score: int, player_hand: list, player_score: int, money: int,
                    backside: bool):
    print(f"\nYour money: {money}")
    if backside:
        print('\nDEALER: ???')
    else:
        print(f'\nDEALER: {dealer_score}')
    show_cards(dealer_hand, backside)
    print(f'\nPLAYER: {player_score}')
    show_cards(player_hand)


def choose_move(first_round: bool = False):
    while True:
        if first_round:
            print("\n(H)it, (S)tand, (D)ouble")
            choice = input("> ").upper()
        else:
            print("\n(H)it, (S)tand")
            choice = input("> ").upper()
        if choice in 'HSD':
            return choice


def main():
    money = 5000
    max_bet = money
    dealer_hand = []
    player_hand = []
    player_chose = ''
    dealer_score = player_score = 0

    game_continue = True
    game_round = True

    config_game(money)
    while game_continue:
        first_round = True
        deck = create_deck()
        deck, dealer_hand = get_dealer_cards(deck, dealer_hand, 2)
        deck, player_hand = get_player_cards(deck, player_hand, 2)

        while game_round:
            bet = get_bet(max_bet)
            money -= bet

            if player_chose == 'H':
                deck, player_hand = get_player_cards(deck, player_hand)
                print(f'You draw {player_hand[-1][0]} of {player_hand[-1][1]}')  # You draw card.name of card.suite
            elif player_chose == 'S':
                pass
            elif player_chose == 'D':
                deck, player_hand = get_player_cards(deck, player_hand)
                print(f'You draw {player_hand[-1][0]} of {player_hand[-1][1]}')
                money -= bet

            if dealer_score < 17:
                deck, dealer_hand = get_dealer_cards(deck, dealer_hand)

            dealer_score, player_score = get_game_score(dealer_hand, player_hand)
            result = check_score(dealer_score, player_score)
            backside = True if result not in ('player_win', 'dealer_win') else False  # TODO исправить отображение карты
            show_game_table(dealer_hand, dealer_score, player_hand, player_score, money, backside)
            player_chose = choose_move(first_round)
            first_round = False


    # show_cards(player_hand, False)


if __name__ == '__main__':
    main()

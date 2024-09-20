import art
import random

# Selects random card from deck
# Ace is initially counted as 11; J, Q, & K are counted as 10; no joker in deck.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Returns score of cards in list
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If sum of cards is over 21 and contains Ace, it can be changed to 1 to keep playing
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Function to compare scores and determine winning results
def compare_scores(u_score, c_score):
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "Computer has a blackjack. You lose!"
    elif u_score == 0:
        return "You have a blackjack. You win!"
    elif u_score > 21:
        return "Your score is over 21. You lose!"
    elif c_score > 21:
        return "Computer scored over 21. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

# Function to play game
def play_game():
    print(art.logo)

    # User selected cards
    user_cards = []

    # Computer selected cards
    computer_cards = []

    # Defining variables to debug potential while loop issues
    user_score = -1
    computer_score = -1

    # Keeps game going until conditions met to end game
    is_game_over = False

    # Adds randomly selected cards to the user/computer hand
    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User chooses cards first while game continues to run 
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Game is over when user/computer gets blackjack or user goes over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        # User keeps adding cards to hand until they decide to stop
        else:
            user_deals_card = input("Type 'y' for another card or 'n' to pass: ")
            if user_deals_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer chooses cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results with winner determined
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

# Game play starts and continues as long as user wants
while input("Do you want to play BlackJack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
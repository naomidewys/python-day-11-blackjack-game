import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0

    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's a draw!")
    elif computer_score == 0:
        print("Computer has blackjack. You lose!")
    elif user_score == 0:
        print("You got a blackjack. You win!")
    elif user_score > 21:
        print("You went over 21. You lose!")
    elif computer_score > 21:
        print("Computer went over 21. You win!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("You lose!")

def blackjack_game():

    print(art.logo)
    print("Let's play a game of Black Jack.")

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False

    for card in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}. Your total: {user_score}.")
        print(f"Computer's first card: {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            add_new_card = input("Type 'y' for another card or 'n' to pass: ").lower()
            if add_new_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}. Your final score: {user_score}.")
    print(f"Computer's cards: {computer_cards}. Computer's score: {computer_score}.")
    compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 5)
    blackjack_game()

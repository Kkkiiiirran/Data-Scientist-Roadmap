import random
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# pick two random cards
#pick on two random cards for the computer
#display your cards
#display one of the computer's card

#ask user if they want more card
#if y 
#select third random card
#check if the total score of the computer is < 16 if yes add the 3rd card

#keep checking scores if score more than 21 print you lose
# when user says no check who is closer and print the winner
def blackjack():
    card1 = cards[random.randint(0, len(cards)-1)]
    card2 = cards[random.randint(0, len(cards)-1)]

    my_cards = []
    my_total = 0
    my_total+= card1
    my_total+= card2

    print(my_total)
    my_cards.append(card1)
    my_cards.append(card2)

    print(my_cards)

    ########
    c_card1 = cards[random.randint(0, len(cards)-1)]
    c_card2 = cards[random.randint(0, len(cards)-1)]

    compters_cards = []
    c_total = 0
    c_total+= c_card1
    c_total+= c_card2
    compters_cards.append(c_card1)
    compters_cards.append(c_card2)
    print(compters_cards[0])
    ########

    def checkResult(total1, total2):
        if total1 == 21:
            return "You WIN"
        elif total2 == 21:
            return "You Lose"
        elif total1 > 21:
            return "You Lose"
        elif total2 > 21:
            return "You Won"
        elif total1 > c_total:
            return "You Win"
        else: return "You Lose"

    print(f"compter total: {c_total}")
    while my_total <= 21 or c_total<= 21:
        moreCard = input("Do you want to pick a new card?")
        
        if c_total < 16:
            new_c_card = cards[random.randint(0, len(cards)-1)]
            compters_cards.append(new_c_card)
            c_total+= new_c_card

        if my_total < 21 and moreCard == "y":
            newcard = cards[random.randint(0, len(cards)-1)]
            my_cards.append(newcard)
            my_total+= newcard

        print(f"my total: {my_total}")
        print(f"compter total: {c_total}")

        if my_total > 21 and c_total > 21 or moreCard == "n": return print(checkResult(total1=my_total, total2=c_total))
    
    
    print(checkResult(my_total, c_total))

    



blackjack()
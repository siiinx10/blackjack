
import random

#create decxk of cards and create player dealer hand
deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10, 'J','Q','K','A','J','Q','K','A','J','Q','K','A']
playerHand=[]
dealerHand=[]
playerIn=True
dealerIn=True
#deal the card
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
#take player deal hand and calculate total of each hand
def total(turn):
    total = 0
    face = ['J','Q','K']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total+=1
        else:
            if total > 11:
                total += 10
            else:
                total += 11
    return total
#check for winner dealer or player
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand)> 2:
        return dealerHand[0], dealerHand[1]
#game loop
for _ in range (2):
    dealCard(dealerHand)
    dealCard(playerHand)
print(playerHand)
print(dealerHand)
while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and X")
    print(f"you has {playerHand} for a total of {total(playerHand)}")
    if playerIn:
        stayOrHit = input("1 to stay and 2 to hit")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break
if total(playerHand) == 21:
    print(f"You have a total of {playerHand} for a total of 21 and the dealer has {dealerHand}")
    print("Blackjack!")
elif total(dealerHand) == 21:
    print(f"You have a total of {playerHand} for a total of 21 and the dealer has {dealerHand}")
    print("Blackjack! Dealer wins")
elif total(dealerHand) > 21:
    print(f"You have a total of {playerHand} for a total of 21 and the dealer has {dealerHand}")
    print("Dealer busts!")
elif 21-total(dealerHand) < 21 - total(playerHand):
    print(f"You have a total of {playerHand} for a total of 21 and the dealer has {dealerHand}")
    print("Dealer Wins!")
elif 21-total(dealerHand) > 21 - total(playerHand):
    print(f"You have a total of {playerHand} for a total of 21 and the dealer has {dealerHand}")
    print("you Wins!")



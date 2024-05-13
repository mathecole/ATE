import random
player_count = 0
dealer_count = 0
dealer_card1 = 0
dealer_card2 = 0
player_card1 = 0
player_card2 = 0
bet = 0
balance = int(open("balance.save", "r"))
print("Your Balance is %s"%(balance))
bet = int(input("please enter your bets"))
if bet > balance:
    print("please leave")
    exit()
if bet <=0:
    print("you cannot afford this bet, please leave")
    exit()
print("your bet is %s$")
balance = balance - bet
def deal():
    while True:
        global dealer_count
        global player_count
        global player_card1
        global player_card2
        global bet
        dealer_show = random.randint(1,13)
        dealer_count = dealer_show + random.randint(1,13)
        player_card1 = random.randint(1,13)
        player_card2 = random.randint(1,13)
        player_count = player_card2 + player_card1
        print("Your cards are %s and the dealers first card is %s, do you wish to hit or stand?" % (
        player_count, dealer_show))
        while True:
            action = input("y- yes \n n- no")
            if action != "y" or action != "n":
                print("You must enter y or n, try again")
        if player_count == 21:
            bet = bet * 1.5
            print("you win %s$"%(bet))
with open("balance.save", "w") as file1:
    file1 .write("")
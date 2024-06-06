import random
player_count = 0
dealer_count = 0
dealer_card1 = 0
dealer_card2 = 0
player_card1 = 0
player_card2 = 0
bet = 0
f = (open("balance.save", "r"))
balance = int(f.read())
print("Your Balance is %s"%(balance))
bet = int(input("please enter your bets"))
if bet > balance:
    print("please leave")
    exit()
if bet <=0:
    print("you cannot afford this bet, please leave")
    exit()
print("your bet is %s"%bet)
balance = balance - bet
def deal():
        global dealer_count
        global player_count
        global player_card1
        global player_card2
        global bet
        global balance
        dealer_show = random.randint(1,13)
        dealer_count = dealer_show + random.randint(1,13)
        player_card1 = random.randint(1,13)
        player_card2 = random.randint(1,13)
        player_count = player_card2 + player_card1
        if player_count > 21:
            player_count -= 10
        print("Your cards are %s and the dealers first card is %s, do you wish to hit or stand?" % (
        player_count, dealer_show))
        while True:
            action = input("y- yes \n n- no")
            if action != "y" and action != "n":
                print("You must enter y or n, try again")
            if player_count == 21:
                bet = bet * 1.5
                balance + bet
                print("you win %s$"%(bet))
                break
            if action == "y":
                playeradd = random.randint(1,11)
                player_count += playeradd
                if player_count > 21 and playeradd == 11:
                    player_count -10
            if player_count > 21:
                print("you lose, your cards were %s"%player_count)
                break
            print("you now have %s cards" %player_count)
            if action == "n":
                if player_count == 21:
                    bet = bet * 2.5
                    balance += bet
                    print("you win with blackjack %s$" % (bet))
                    break
                if dealer_count < 17:
                    print("the dealer's cards are %s"%dealer_count)
                    while dealer_count <= 17:
                        dealer_add =random.randint(1,11)
                        dealer_count+=dealer_add
                        if dealer_count > 21 and dealer_add == 11:
                            dealer_count+= random.randint(1,10)
                        print("the dealer's cards are now %s"%dealer_count)
                    if dealer_count >21:
                        print("you win %s$"%(bet*2))
                        balance += bet*2
                        break
                    elif dealer_count > player_count:
                        print("you lose")
                        break
                    elif dealer_count < player_count:
                        print("you win")
                        balance += bet*2
                        break
                    if player_count == dealer_count:
                        print("it's a draw!")
                        break
                    break

deal()
print("your balance is now %s"%balance)
with open("balance.save", "w") as file1:
    file1 .write(str(balance))
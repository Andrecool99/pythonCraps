import random


# define function to roll dice
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


# initialize variables
money = 100
comeList = []

def bet_won(betAmt):
    print("You won the bet of $" + str(betAmt) + "!")
    print()
    global money
    money += betAmt * 2
    print("Balance: $" + str(money))
    main()


def bet_lost(betAmt):
    print("You lost the bet of $" + str(betAmt))
    print()
    global money
    print("Balance: $" + str(money))
    main()

def bet_tied(betAmt):
    print("You tied the bet of $" + str(betAmt))
    print()
    global money
    money += betAmt
    print("Balance: $" + str(money))
    main()

def pass_bet(betAmt):
    print("Pass Line Bet for $" + str(betAmt))
    global money
    global comeList

    money -= betAmt
    print("Rolling Dice...")
    diceRoll = roll_dice()
    print("Rolled a " + str(diceRoll))

    if diceRoll in [7, 11]:
        bet_won(betAmt)

    elif diceRoll in [2, 3, 12]:
        bet_lost(betAmt)

    else:
        print("Point set at " + str(diceRoll))
        point = diceRoll

        roundOver = False
        while not roundOver:
            print("Rolling Dice...")
            diceRoll = roll_dice()
            print("Rolled a " + str(diceRoll))

            if diceRoll == point:
                bet_won(betAmt)
                roundOver = True

            if diceRoll == 7:
                bet_lost(betAmt)
                roundOver = True


def dont_pass_bet(betAmt):
    print("Don't Pass Line Bet for $" + str(betAmt))
    global money
    global comeList

    money -= betAmt
    print("Rolling Dice...")
    diceRoll = roll_dice()
    print("Rolled a " + str(diceRoll))

    if diceRoll in [2, 3, 12]:
        bet_won(betAmt)

    elif diceRoll in [7, 11]:
        bet_lost(betAmt)

    else:
        print("Point set at " + str(diceRoll))
        point = diceRoll

        roundOver = False
        while not roundOver:
            print("Rolling Dice...")
            diceRoll = roll_dice()
            print("Rolled a " + str(diceRoll))

            if diceRoll == 7:
                bet_won(betAmt)
                roundOver = True

            if diceRoll == point:
                bet_lost(betAmt)
                roundOver = True


def come_bet(betAmt):
    print("Come Bet for $" + str(betAmt))
    global money
    global comeList

    money -= betAmt
    print("Rolling Dice...")
    diceRoll = roll_dice()
    print("Rolled a " + str(diceRoll))

    print("Point set at " + str(diceRoll))
    point = diceRoll

    roundOver = False
    while not roundOver:
        print("Rolling Dice...")
        diceRoll = roll_dice()
        print("Rolled a " + str(diceRoll))

        if diceRoll == point:
            bet_won(betAmt)
            roundOver = True

        if diceRoll == 7:
            bet_lost(betAmt)
            roundOver = True


def dont_come_bet(betAmt):
    print("Don't Come Bet for $" + str(betAmt))
    global money
    global comeList

    money -= betAmt
    print("Rolling Dice...")
    diceRoll = roll_dice()
    print("Rolled a " + str(diceRoll))

    print("Point set at " + str(diceRoll))
    point = diceRoll

    roundOver = False
    while not roundOver:
        print("Rolling Dice...")
        diceRoll = roll_dice()
        print("Rolled a " + str(diceRoll))

        if diceRoll in [2, 3]:
            bet_won(betAmt)
            roundOver = True

        elif diceRoll in [7, 11]:
            bet_lost(betAmt)
            roundOver = True

        elif diceRoll == 12:
            bet_tied(betAmt)
            roundOver = True



def main():

    #Get starting bet type
    betTypeValid = False
    betType = 0


    while not betTypeValid:
        print("Please select your bet type:")
        print("1.) Pass Line Bet")
        print("2.) Don't Pass Line Bet")
        print("3.) Come Bet")
        print("4.) Don't Come Bet")

        betType = int(input())

        betTypeValid = False
        if betType in [1,2,3,4]:
            betTypeValid = True

        if not betTypeValid:
            print("Invalid bet type!")


    #Get bet amount
    betValid = False
    betAmt = 0

    while not betValid:
        betAmt = int(input("You have $" + str(money) + ", how much would you like to bet? "))

        if (betAmt <= money):
            betValid = True

        if not betValid:
            print("Invalid bet amount.")

    if betType == 1:
        pass_bet(betAmt)

    elif betType == 2:
        dont_pass_bet(betAmt)

    elif betType == 3:
        come_bet(betAmt)

    elif betType == 4:
        dont_come_bet(betAmt)

print("Welcome to craps!")
main()
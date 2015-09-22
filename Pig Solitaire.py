import random

class Dice:

    def roll(self):
        return random.randint(1,6)

dice = Dice()

class Player:

    def __init__(self):
        self.dice = dice
        pass

    def user_turn(self):
        running_score = 0
        while True:
            roll = self.dice.roll()
            running_score += roll
            print("You rolled a {}".format(roll))
            print("Your round total is {}.".format(running_score))
            if roll == 1:
                print("Turn over. Computer's turn.")
                return False
            else:
                choice = input("Would you like to roll again? Please type Yes or No. ")
                if choice in ["Yes", "yes", "YES"]:
                    print("------------------------")
                    continue
                elif choice in ["No", "NO", "no"]:
                    print("Your round total was {}. Computer's turn.".format(running_score))
                    return False

    def accumulation(self):
        total_score =+ running_score
        total_turns =+ turn
        if total_turns == 7:
            print("Game over!")

class Computer:

    def __init__(self):
        self.dice = dice
        pass

    def computer_turn(self):
        self.running_score = 0
        turn = 1
        while True:
            roll = self.dice.roll()
            running_score += roll
            print("Computer rolled a {}".format(roll))
            print("Computer's round total is {}.".format(running_score))
            if roll == 1:
                print("Turn over. Player's turn.")
                return False
            else:
                if running_score < 50:
                    print("------------------------")
                    continue
                else:
                    print("Computer has passed. Computer's round total was {}. It's your turn!".format(running_score))
                    return False

# Initiate user turn:
   #matt = Player()
    #matt.user_turn()


# Initiate computer turn:
   #matt = Computer()
    #matt.computer_turn()

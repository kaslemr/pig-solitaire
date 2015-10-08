import random

class Dice:

    def roll(self):
        return random.randint(1,6)

class Computer_hard_mode:

    def __init__(self, rounds=7):
        self.dice = Dice()
        self.rounds = rounds
        self.score_total = 0

    def computer_turn(self):
        round_count = 0
        counter = 0
        self.roll_number = 0
        self.game_score = 0
        self.round_score = 0
        list_scores = []
        while round_count < self.rounds:
            round_count += 1
            print("Round #{}. Game total: {}.".format(round_count, self.game_score))
            counter = 0
            while counter < 1:
                roll = self.dice.roll()
                print("Computer rolls a {}".format(roll))
                if roll == 1:
                    self.round_score = 0
                    list_scores.append(self.round_score)
                    print("End of Round #{}. Round Score: {}. Total Score: {}.".format(round_count, self.round_score, self.game_score))
                    print("------------------------")
                    counter = 1
                else:
                    self.round_score += roll
                    if self.round_score < 20:
                        print("Computer chooses to roll again.")
                        print("------------------------")
                        continue
                    else:
                        self.game_score += self.round_score
                        list_scores.append(self.round_score)
                        print("Computer ends turn. Round Score: {}.".format(self.round_score))
                        print("------------------------")
                        self.round_score = 0
                        counter = 1
        print("Computer scored {} points in {} rounds.".format(self.game_score, self.rounds))

class Player:

    def __init__(self, rounds=7):
        self.dice = Dice()
        self.rounds = rounds
        self.score_total = 0

    def player_turn(self):
        round_count = 0
        counter = 0
        self.roll_number = 0
        self.game_score = 0
        self.round_score = 0
        list_scores = []
        while round_count < self.rounds:
            round_count += 1
            print("Round #{}. Game total: {}.".format(round_count, self.game_score))
            counter = 0
            while counter < 1:
                roll = self.dice.roll()
                print("You rolled a {}.".format(roll))
                print("------------------------")
                if roll == 1:
                    self.round_score = 0
                    list_scores.append(self.round_score)
                    print("End of Round #{}. Round Score: {}. Total Score: {}.".format(round_count, self.round_score, self.game_score))
                    print("------------------------")
                    counter = 1
                else:
                    self.round_score += roll
                    choice = input("Would you like to roll again? Please type Yes or No. ")
                    if choice in ["Yes", "yes", "YES"]:
                        print("------------------------")
                        continue
                    elif choice in ["No", "NO", "no"]:
                        self.game_score += self.round_score
                        list_scores.append(self.round_score)
                        print("You've ended your turn. Round Score: {}.".format(self.round_score))
                        print("------------------------")
                        self.round_score = 0
                        counter = 1
        print("End of game. You scored {} points in {} rounds.".format(self.game_score, self.rounds))

#Initiate user turn:
    #matt = Computer_hard_mode()
    #matt.computer_turn()

#Initiate computer turn:
    #computer = Computer_hard_mode()
    #computer.computer_turn()
    

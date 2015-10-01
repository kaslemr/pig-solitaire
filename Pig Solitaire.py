import random

class Dice:

    def roll(self):
        return random.randint(1,6)

dice = Dice()

class Player:

    def __init__(self):
        self.dice = Dice()
        self.player_round_total = 0
        self.player_score_total = 0
        pass

    def user_turn(self):
        u_current_round = 1
        u_running_score = 0
        current_round = 1
        running_score = 0
        self.player_round_total += current_round
        self.player_score_total += running_score
        print("Game point total: {}. This is Turn #{}.".format(self.player_score_total, self.player_round_total))
        while True:
            roll = self.dice.roll()
            running_score += roll
            print("You rolled a {}".format(roll))
            print("Your round total is {}.".format(running_score))
            if roll == 1:
                self.player_score_total += running_score
                self.running_score = running_score
                print("End of turn #{}. Round total: {}. Game total: {}.".format(self.player_round_total, running_score, self.player_score_total))
                return False
            else:
                choice = input("Would you like to roll again? Please type Yes or No. ")
                if choice in ["Yes", "yes", "YES"]:
                    print("------------------------")
                    continue
                elif choice in ["No", "NO", "no"]:
                    self.running_score = running_score
                    self.player_score_total += running_score
                    print("End of turn #{}. Round total: {}. Game total: {}.".format(self.player_round_total, running_score, self.player_score_total))
                    return False

class Computer:

    def __init__(self):
        self.dice = dice
        self.computer_round_total = int()
        self.computer_score_total = int()

    def computer_turn(self):
        c_current_round = 1
        c_running_score = 0
        self.computer_round_total += c_current_round
        self.computer_score_total += c_running_score
        print("Game point total: {}. This is Turn #{}.".format(self.computer_score_total, self.computer_round_total))
        while True:
            roll = self.dice.roll()
            c_running_score += roll
            print("Computer rolled a {}".format(roll))
            print("Computer's round total is {}.".format(c_running_score))
            if roll == 1:
                self.computer_score_total += c_running_score
                self.running_score = c_running_score
                print("End of turn #{}. Computer Round total: {}. Computer Game total: {}.".format(self.computer_round_total, c_running_score, self.computer_score_total))
                self.computer_score = self.computer_score_total
                self.computer_round = self.computer_round_total
                return False
            else:
                if c_running_score < 50:
                    print("Computer chooses to roll again.")
                    print("------------------------")
                    continue
                else:
                    self.running_score = c_running_score
                    self.computer_score_total += c_running_score
                    print("Computer has passed. End of turn #{}. Computer Round total: {}. Computer Game total: {}.".format(self.computer_round_total, c_running_score, self.computer_score_total))
                    self.computer_score = self.computer_score_total
                    self.computer_round = self.computer_round_total
                    return False

class Game:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def play_game
        self.player.user_turn()

player_a = Player()
# Initiate computer turn:
player_b = Computer()

game = Game(player_a, player_b)

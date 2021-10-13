import random

class RPS:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.computer_choice = random.choice(self.choices)

    def set_player_choice(self):
        pass

    def win(self):
        pass

    def lose(self):
        pass

    def check(self, player_choice):
        if(player_choice == "rock" and self.computer_choice == "paper"):
            self.lose()
        elif(player_choice == "rock" and self.computer_choice == "scissors"):
            self.win()
        elif(player_choice == "paper" and self.computer_choice == "scissors"):
            self.lose()
        elif(player_choice == "paper" and self.computer_choice == "rock"):
            self.win()
        elif(player_choice == "scissors" and self.computer_choice == "rock"):
            self.lose()
        elif(player_choice == "scissors" and self.computer_choice == "paper"):
            self.win()

    def play_again(self):
        pass


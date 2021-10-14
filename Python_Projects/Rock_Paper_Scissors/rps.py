import random

class RPS:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.computer_choice = random.choice(self.choices)

    def win(self, player):
        """
        Return win message
        """
        return "You win! You choose {} and computer choose {}".format(player, self.computer_choice)

    def lose(self, player):
        """
        Return lose message
        """
        return "You lose! You choose {} and computer choose {}".format(player, self.computer_choice)

    def check(self, player_choice):
        """
        Check if player have winning / losing choice
        """
        if(player_choice == "rock" and self.computer_choice == "paper"):
            return self.lose(player_choice)
        elif(player_choice == "rock" and self.computer_choice == "scissors"):
            return self.win(player_choice)
        elif(player_choice == "paper" and self.computer_choice == "scissors"):
            return self.lose(player_choice)
        elif(player_choice == "paper" and self.computer_choice == "rock"):
            return self.win(player_choice)
        elif(player_choice == "scissors" and self.computer_choice == "rock"):
            return self.lose(player_choice)
        elif(player_choice == "scissors" and self.computer_choice == "paper"):
            return self.win(player_choice)

    def play_again(self):
        """
        Play the game again
        """
        self.computer_choice = random.choice(self.choices)


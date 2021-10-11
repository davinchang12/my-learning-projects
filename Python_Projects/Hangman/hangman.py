import random
import time

class Hangman():
    def __init__(self):
        """
        Initialze class
        """

        self.guess_word = ["dog", "cat", "house", "film", "car", "planet", "bicycle", "laptop"]
        self.word = random.choice(self.guess_word)
        self.length = len(self.word)
        self.count = 0
        self.display = "_" * self.length
        self.guessed_word = []
        self.play_game = ""

    def play_again(self):
        """
        Check if player still want to continue or no

        If player answer yes, the game will continue.
        If player answer no, the game will stop and quit.
        """

        self.play_game = input("Do you want to play again? [y]Yes / [n]No\n")
        
        while self.play_game not in ["Y", "y", "N", "n"]: # Check if user gives wrong input
            self.play_game = input("Do you want to play again? [y]Yes / [n]No\n")
        
        if self.play_game in ["Y", "y"]:
            self.play()
        elif self.play_game in ["N", "n"]:
            print("Thanks for playing !")
            exit()

    def play(self):
        pass
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
        self.display = "_" * self.length
        self.guessed_word = []
        self.play_game = ""
        
        self.count = 0
        self.limit = 5

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

    def wrong_ans_print(self):
        """
        Print to screen if user guess wrong letter.
        """
        print("Wrong guess. " + str(self.limit - self.count) + " last guess remaining\n")

    def play(self):
        """
        Play hangman game.
        """
        guess = input("Guess the word : " + self.display + "\nHint:" + self.length + " word(s).\nEnter your guess : ").strip()
        if (len(guess == 0) or len(guess >= 2) or (guess <= 9)):
            print("Invalid input, try a letter!")
            self.play()
        elif guess in self.word:
            self.guessed_word.extend([guess])
            index = self.word.find(guess)
            self.word = self.word[:index] + "_" + self.word[index + 1:]
            self.display = self.display[:index] + "_" + self.display[index + 1:]
            print(self.display + "\n")
        elif guess in self.guessed_word:
            print("Try another letter.\n")
        else:
            self.count += 1
            if self.count == 1:
                time.sleep(1)
                print("   _____ \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")
                self.wrong_ans_print()
            elif self.count == 2:
                time.sleep(1)
                print("   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")
                self.wrong_ans_print()
            elif self.count == 3:
                time.sleep(1)
                print("   _____ \n"
                        "  |     | \n"
                        "  |     |\n"
                        "  |     | \n"
                        "  |      \n"
                        "  |      \n"
                        "  |      \n"
                        "__|__\n")
                self.wrong_ans_print()
            elif self.count == 4:
                time.sleep(1)
                print("   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")
                self.wrong_ans_print()
            elif self.count == 5:
                time.sleep(1)
                print("   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |    /|\ \n"
                    "  |    / \ \n"
                    "__|__\n")
                print("Wrong guess. You are hanged!!!\n")
                print("The word was: ", self.already_guessed, self.word)
                self.play_loop()
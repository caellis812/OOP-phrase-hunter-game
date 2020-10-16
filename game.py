import random
from phrase import Phrase


class InputError(Exception):
    pass
    

class Game:
    
    
    def __init__(self):
        self.phrases = [
            Phrase("not   my   cup   of   tea"),
            Phrase("have   your   cake   and   eat   it   too"),
            Phrase("an   apple   a   day   keeps   the   doctor   away"),
            Phrase("no   use   crying   over   spilled   milk"),
            Phrase("two   peas   in   a   pod"),
        ]
        self.active_phrase = None
        self.guesses = []
        self.missed = 0
        self.replay = ""
    
    
    def start(self):
        
        self.welcome()
        
        while self.replay == "" or self.replay == "y":
            self.active_phrase = self.get_random_phrase()
            
            if self.replay == "y":
                self.guesses = []
                self.missed = 0
                
            while self.active_phrase.check_complete(self.guesses) == False and self.missed < 5:
                self.active_phrase.display(self.guesses)
                current_guess = self.get_guess()
                self.guesses.append(current_guess)
                if self.active_phrase.check_letter(current_guess) == False:
                    self.missed += 1
                    print("\n\nOH NO! The letter '{}' isn't present. You have a total of {} incorrect guesses.".format(current_guess, self.missed))
            else:
                self.game_over()
        print("\nThanks for playing! Goodbye.")   
            
    
    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    
    def welcome(self):
        print("--------------------------")
        print("Welcome to Phrase Hunters!")
        print("--------------------------")
        print("""
Here's how to play the game:

Your goal is to to guess all the letters in a hidden, random phrase.
The phrase will consist only of letters (no numbers, puntuation or other special characters).

If at first you don't succeed, try, try, try, again.
But be careful...
Once you make five incorrect guesses, the game is over.

Best of luck!""")
    
    
    def get_guess(self):
        while True:
            try:
                current_guess = input("\nGuess a letter: ")
                current_guess = current_guess.lower()
                if current_guess < "a" or current_guess > "z":
                    raise InputError("\nOOPS! Invalid guess. Input cannot be a number or character. Enter a letter 'a' through 'z'.")
                elif len(current_guess) != 1:
                    raise InputError("\nOOPS! Invalid guess. Only one letter may be entered.")
                elif current_guess in self.guesses:
                    raise InputError("\nOOPS! You've already guessed that letter.")
                break
            except InputError as err:
                print("{}".format(err))
        return current_guess
        
    
    def game_over(self):
        if self.missed == 5:
            print("\n\n********* SORRY!! *********")
            print("You've reached the maximum number of incorrect guesses! \nGAME OVER :(")
        else:
            print("\n\n********* WINNER!!! *********")
            self.active_phrase.display(self.guesses)
            print("\nCongratulations, you've completed the phrase and won this round of Phrase Hunters!")
        self.replay = input("\nWould you like to play again? (Y/N): ").lower()
        while self.replay != "y" and self.replay != "n":
            self.replay = input("\nInvalid entry. Would you like to play again? (Y/N): ").lower()

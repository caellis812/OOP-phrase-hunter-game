# OOP-phrase-hunter-game
 Word guessing game
 
 OVERVIEW:

This code chooses a random phrase from a list of five phrases and displays each letter of the phrase as underscore (_) character placeholders.

After the player is prompted to guess a letter, the program compares the letter the player has chosen with the random phrase. If the letter is in the phrase, the phrase object is updated so that it displays the chosen letters on the screen.

A player continues to select letters until they guess all the letters of the phrase (and win), or makes five incorrect guesses (and lose). Finally, the player is given the option to play again.

PROJECT FILES:

1) phrase.py to create a Phrase class with methods for the following:
- handle the display of the phrase object
- check if a particular letter is in the phrase
- check if the phrase is complete

2) game.py to create a Game class with methods for the following: 
- choosing a random phrase
- starting the game
- prompting for guesses
- adding to the number of incorrect guesses
- checking for a win/loss state, and asking the player to play again

3) app.py to Import the Game class from the phrasehunter package:
- create a new instance of the Game class
- store this instance in a game variable
- call the start() method in order to start the game in the console

class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    
    def display(self, guessed_letters):
        print_phrase = ""
        for character in self.phrase:
            if character in guessed_letters or character == " ":
                print_phrase += character
            else:
                print_phrase += "_"
        print("\nPHRASE:",print_phrase,)
    
    
    def check_letter(self, letter):
        return letter in self.phrase
        
    
    def check_complete(self, guessed_letters):
        for character in self.phrase.replace(" ", ""):
            if character not in guessed_letters:
                return False
        else:
            return True
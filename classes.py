from dictionary import *

class Letter:
    def __init__(self, letter):
        self._letter = letter.upper()
        self._corresponding_morse = self.codify()
   
    @property
    def letter(self):
        return self._letter

    @property
    def corresponding_morse(self):
        return self._corresponding_morse

    def codify(self):
        #This function gets the user's inpurt and uses it as a key to return the corresponding value on the codify dict
        return codify_dictionary.get(self._letter)

class Morse:
    def __init__(self, morse):
        self._morse = morse
        self._corresponding_leeter = self.decodify()
  
    @property
    def morse(self):
        return self._morse

    @property
    def corresponding_leeter(self):
        return self._corresponding_leeter


    def decodify(self):
        #This functions gets the user's morse code input and return the corresponding letter
        return decodify_dictionary.get(self.morse)

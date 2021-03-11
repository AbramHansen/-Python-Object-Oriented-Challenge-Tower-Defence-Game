class Jumper:
    
    def __init__ (self):
        self.guesses = []
        self.parachutePieces = 4
    def getGuesses(self):
        return self.guesses
    def addGuess(self, guess):
        self.guesses.append(guess)
    def getLastGuess(self):
        self.guesses[-1]
    def cutParachute(self):
        self.parachutePieces -= 1
    def getNumParachutePieces(self):
        return self.parachutePieces
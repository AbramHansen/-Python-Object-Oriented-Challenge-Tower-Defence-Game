from game.console import Console
from game.jumper import Jumper
from game.puzzle import Puzzle

class Director:
    def __init__(self):
        self.jumper = Jumper()
        self.console = Console()
        self.puzzle = Puzzle()
        self.keepPlaying = True

    def start_game(self):
        while (self.keepPlaying):
            self.console.displayMessage(self.puzzle.getDisplayWord())
            self.console.displayParachute(self.jumper.getNumParachutePieces())
            
            userGuess = self.console.getGuess()
            if (not self.puzzle.isCorrect(userGuess)):
                self.jumper.cutParachute()
            
            if (self.puzzle.hasWon()):
                self.console.displayMessage("The word is: " + self.puzzle.getWord())
                self.console.displayParachute(self.jumper.getNumParachutePieces())
                self.console.displayMessage("Congratulations! You have won!")
                self.keepPlaying = False
            
            if (self.jumper.getNumParachutePieces() == 0):
                self.console.displayMessage("The word is: " + self.puzzle.getWord())
                self.console.displayParachute(self.jumper.getNumParachutePieces())
                self.console.displayMessage("YOU'RE DEAD X_X BETTER LUCK NEXT TIME!")
                self.keepPlaying = False
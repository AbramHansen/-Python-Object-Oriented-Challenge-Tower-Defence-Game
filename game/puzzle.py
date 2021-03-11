import random

class Puzzle:
    def __init__(self):
        wordsFile = open("game/words.txt", "r")
        self.words = []
        for line in wordsFile:
            self.words.append(line)
        wordsFile.close()
        index = random.randint(0, len(self.words) - 1)
        self.word = self.words[index]
        self.correct = []
        for i in range(0, len(self.word)):
            self.correct.append("_")
        self.displayWord = ""

    def isCorrect(self, guess):
        if guess in self.word:
            i = 0
            for char in self.word:
                if char == guess:
                    self.correct[i] = guess
                i += 1
            return True
        else:
            return False
    
    def getWord(self):
        return self.word

    def getDisplayWord(self):
        self.displayWord = ""
        for char in self.correct:
            self.displayWord += char
        return self.displayWord

    def hasWon(self):
        if self.displayWord == self.word:
            return True
        else:
            return False

#Test code for this class
# game = Puzzle()

# print(game.getWord())

# print(game.isCorrect("p"))
# print(game.getDisplayWord())
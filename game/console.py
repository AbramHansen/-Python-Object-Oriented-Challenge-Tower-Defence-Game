class Console:
    #Where the parachute is drawn and where the letters appear on screen

    def __init__(self):
        pass

    def getInput(self, message):
        return(input(message))

    def displayMessage(self, message):
        print(message)

    def getGuess(self): 
        #ask user for a character then return it
        #message used to ask for the char must match assignment instruction
        x = ""
        while True:
            try:
                x = (input("Guess a letter [a-z]: "))
                break
            except ValueError:
                print("Invalid. Please enter a letter (A-Z)")
        
        return x

    
    def displayParachute(self, parachutePieces):
        #draw the parachute based on number of parachute pieces the player has left
        #parachute pieces = 4: full parachute
        #parachute pieces= 3: take off one piece
        #parachute pieces = 2: has 2 pieces left
        #parachute pieces = 1: has 1 piece left
        #If guessesleft == 0, no more pieces left = dead.

        if parachutePieces == 4:
            print(" ---")
            print("/____\ ")
            print("\    /")
            print(" \  /")
            print("   0")
            print("  /|\ ")
            print("  / \ ")
        elif parachutePieces == 3:
            print("/____\ ")
            print("\    /")
            print(" \  /")
            print("   0")
            print("  /|\ ")
            print("  / \ ")
        elif parachutePieces == 2:
            print("\    /")
            print(" \  /")
            print("   0")
            print("  /|\ ")
            print("  / \ ")
        elif parachutePieces == 1:
            print(" \  /")
            print("   0")
            print("  /|\ ")
            print("  / \ ")
        elif parachutePieces == 0:
            print("   X")
            print("  /|\ ")
            print("  / \ ")

class Console:
    #Where the parachute is drawn and where the letters appear on screen


    def getInput(self, message):
        message = input("Guess a letter [a-z]: ")
        return message

    def displayMessage(self, message):
        #print(message)
        pass
    def getGuess(self, guess): 
        #ask user for a character then return it
        #message used to ask for the char must match assignment instruction
        guess = message
        print(guess)

    
    def displayParachute(self, parachutePieces):
        #draw the parachute based on number of parachute pieces the player has left
        #parachute pieces = 4: full parachute
        #parachute pieces= 3: take off one piece
        #parachute pieces = 2: has 2 pieces left
        #parachute pieces = 1: has 1 piece left
        #If guessesleft == 0, no more pieces left = dead.
        full =  print( "---")
                print("/____\ ")
                print("\    /")
                print(" \  /")
                print(   "0")
                print(  "/|\ ")
                print(  "/ \ ")

        oneoff= print("/____\ ")
                print("\    /")
                print(" \  /")
                print(   "0")
                print(  "/|\ ")
                print(  "/ \ ")

        twoleft=print("\    /")
                print(" \  /")
                print(   "0")
                print(  "/|\ ")
                print(  "/ \ ")
        
        oneleft=print(" \  /")
                print(   "0")
                print(  "/|\ ")
                print(  "/ \ ")

        dead= print(   "X")
              print(  "/|\ ")
              print(  "/ \ ")




        if parachutePieces == 4:
            print(full)
        elif: parachutePieces == 3:
            print(oneoff)
        elif: parachutePieces == 2:
            print(twoleft)
        elif: parachutePieces == 1:
            print(oneleft)
        else: parachutePieces == 0:
            print(dead)
import random

class ConnectFour:

    def __init__(self): 
        self.holes = [ [' ' for x in range(7)] for y in range(6)]
    
    
    def startGame(self):  # StartGame Method
        self.__init__()
        self.printBoard()

        while True:
            self.playerDropPieceInSlot()
            if self.checkForWinner():
                ans = input("\nAGAIN?(Y/N)\n> ")
                if ans.upper() == 'Y':
                    print()
                    self.startGame()
                    break
                elif ans != 'Y':
                    print("THANK YOU FOR PLAYING!")
                    break
            self.computerDropPieceInSlot()
            self.printBoard()
            if self.checkForWinner():
                ans = input("\nAGAIN?(Y/N)\n> ")
                if ans.upper() == 'Y':
                    print()
                    self.startGame()
                    break
                elif ans != 'Y':
                    print("THANK YOU FOR PLAYING!")
                    break
    

    def computerDropPieceInSlot(self):
        chosenCol = random.randint(0, len(self.holes[0]) - 1)  # 0-6
        num_of_rows = 0
        isColPlayable = True
        for x in range(0, len(self.holes)): # if column is not free to play, set isColPlayable to false
            if self.holes[x][chosenCol] != ' ':
                num_of_rows += 1
        if num_of_rows == len(self.holes):
            isColPlayable = False
        if isColPlayable:
            for x in range(len(self.holes) - 1, -1, -1):
                if self.holes[x][chosenCol] == ' ':
                    self.holes[x][chosenCol] = 'C'
                    break
        else:
            self.computerDropPieceInSlot()

    def checkforWinnerHorizontal(self):
        playerWon = False
        for row in range(len(self.holes) - 1, -1, -1):
            for col in range(0, len(self.holes[0])):
                if self.holes[row][col] != ' ': 
                    playerToken = self.holes[row][col]
                    newRow = row
                    newCol = col
                    try:
                        for x in range(4):
                            if self.holes[newRow][newCol] == playerToken:
                                newRow -= 1
                                newCol += 0
                                playerWon = True
                            else:
                                playerWon = False
                                break
                    except:
                        playerWon = False
                    if playerWon:
                        self.printBoard()
                        print(playerToken + " WON!")
                        return True


    def checkForWinner(self):
        if self.checkForWinnerRightDiagonal() == True or self.checkForWinnerLeftDiagonal() == True or self.checkforWinnerHorizontal() == True:
            return True
        else:
            return False

    def checkForWinnerLeftDiagonal(self):
        playerWon = False
        for row in range(len(self.holes) - 1, -1, -1):
            for col in range(0, len(self.holes[0])):
                if self.holes[row][col] != ' ': 
                    playerToken = self.holes[row][col]
                    newRow = row
                    newCol = col
                    try:
                        for x in range(4):
                            if self.holes[newRow][newCol] == playerToken:
                                newRow -= 1
                                newCol -= 1
                                playerWon = True
                            else:
                                playerWon = False
                                break
                    except:
                        playerWon = False
                    if playerWon:
                        self.printBoard()
                        print(playerToken + " WON!")
                        return True


    def checkForWinnerRightDiagonal(self):
        playerWon = False
        for row in range(len(self.holes) - 1, -1, -1):
            for col in range(0, len(self.holes[0])):
                if self.holes[row][col] != ' ': 
                    playerToken = self.holes[row][col]
                    newRow = row
                    newCol = col
                    try:
                        for x in range(4):
                            if self.holes[newRow][newCol] == playerToken:
                                newRow -= 1
                                newCol += 1
                                playerWon = True
                            else:
                                playerWon = False
                                break
                    except:
                        playerWon = False
                    if playerWon:
                        self.printBoard()
                        print(playerToken + " WON!")
                        return True
                        




    def playerDropPieceInSlot(self):
        playerChoice = self.getInputFromPlayer()
        num_of_rows = 0
        isColPlayable = True
        for x in range(0, len(self.holes)): # if column is not free to play, set isColPlayable to false
            if self.holes[x][playerChoice] != ' ':
                num_of_rows += 1
        if num_of_rows == len(self.holes):
            isColPlayable = False
        if isColPlayable:
            for x in range(len(self.holes) - 1, -1, -1):
                if self.holes[x][playerChoice] == ' ':
                    self.holes[x][playerChoice] = 'P'
                    break
        else:
            print("ROW IS FULL!")
            self.playerDropPieceInSlot()

    def getInputFromPlayer(self):
        while True:
            try:
                self.playerInput = int(input("\nWhich Row?\n> "))
            except:
                print("TYPE ERROR!\nINTEGERS ONLY")
                continue

            if self.playerInput >= 1 and self.playerInput <= 7:
                break
            else:
                print("ENTER VALID NUMBER!")
        # Logical Number
        self.playerInput -= 1 
        print()
        return self.playerInput

    def printBoard(self): # Prints gameBoard
        for x in range(0, len(self.holes)):
            print(self.holes[x])    


    


game = ConnectFour()
game.startGame()
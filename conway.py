from copy import deepcopy # Used to copy old game state
from random import randrange # Used to randomize the game state
from os import system # Used to clear the screen
from time import sleep # Used to wait before each new print 

class Board:
  # Initialize a board (rows x cols)
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.board = ['-' for i in range(0, rows*cols)] 
    self.generation = 0

  # Print the board so that each row is seperate
  # Using one list by using 2 for loops
  # First loop by row and second by columns
  def printBoard(self):
    for i in range(self.rows):
      for j in range(self.cols):
        print(self.board[i*self.cols + j], end="")
      print("\n", end="")
  
  # A state where the 2nd row has the first 3 filled
  # Used a website to make sure logic was correct
  def testState(self):
    for i in range(2, 5):
      self.board[1*self.cols + i] = 'X'
      self.board[2*self.cols + i-1] = 'X'

  # Giving each cell a 10% chance to be alive for the first (0) generation
  def randomState(self):
    for i in range(self.rows*self.cols):
      if randrange(10) == 0:
        self.board[i] = 'X'

  # Used to check each if each indiviudal cell
  # and use the game's rules as logic
  def checkState(self):
    # Take a copy of the board to use for next game state
    tempBoard = deepcopy(self.board)
      
    # Loop through each cell
    for i in range(self.rows):
      for j in range(self.cols):
        # Pass whether or not the current cell is alive or not
        # as it is relevant for the game's rules
        if self.board[i*self.cols + j] == 'X':
          alive = self.lifeCheck(i, j, True)
        else:
          alive = self.lifeCheck(i, j, False)

        # Update the board, but only for the temporary board 
        tempBoard[i*self.cols + j] = 'X' if alive == True else '-'
        if alive == True:
          tempBoard[i*self.cols + j] = 'X'
        else:
          tempBoard[i*self.cols + j] = '-'

    # Copy contents of the new board to original board
    self.board = deepcopy(tempBoard)

  def lifeCheck(self, row, col, alive):
    count = 0

    aboveRow = (row - 1) % self.rows
    belowRow = (row + 1) % self.rows

    # Check the rows above and below the current cell
    # This will wrap around the edges
    # = = = 
    # - X - 
    # = = = 
    # Checking cells (=) and ignoring (-)

    for i in range(3):
      if self.board[aboveRow*self.cols + ((col-1 + i) % self.cols)] == 'X':
        count += 1
      if self.board[belowRow*self.cols + ((col-1 + i) % self.cols)] == 'X':
        count += 1
    
    # Check cells on the same row
    # - - - 
    # = X = 
    # - - - 
    # Checking cells (=) and ignoring (-)
    if self.board[row*self.cols + ((col - 1) % self.cols)] == 'X':
      count += 1
    if self.board[row*self.cols + ((col + 1) % self.cols)] == 'X':
      count += 1

    # Check rules if cell was alive
    if alive == True:
      if count <= 1:
        return False
      elif count >= 4:
        return False
      # Cell with 2 or 3 is all that is left
      else:
        return True
    # Otherwise check rules for dead cell
    else:
      if count == 3:
        return True
      else:
        return False

def main():
  # Start the board n x m
  newBoard = Board(50, 50) 
  #newBoard.testState()

  # Randomize the game board
  newBoard.randomState()

  # Loop through by the number of generations
  while (newBoard.generation < 50):
    #Use system("cls") if not on Linux
    system("clear") # Since I'm on linux
    newBoard.printBoard()
    # Starting from 0
    print(f"\nGeneration: {newBoard.generation}") 
    sleep(1.5)
    newBoard.checkState()
    newBoard.generation += 1
      
if __name__ == '__main__':
    main()

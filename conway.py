from copy import deepcopy # Used to copy old game state

class Board:
  # Initialize a board (rows x cols)
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.board = ['-' for i in range(0, rows*cols)] 

  # Print the board so that each row is seperate
  def printBoard(self):
    #print(f"ROWS = {self.rows} and COLS = {self.cols}")
    #print(len(self.board))
    for i in range(self.rows):
      for j in range(self.cols):
        #print(f"I = {i} and J = {j}")
        print(self.board[i*self.cols + j], end="")
      print("\n", end="")
  
  # A state where the 2nd row has the first 3 filled
  def testState(self):
    for i in range(4):
      self.board[1*self.cols + i] = 'X'

  def checkState(self):
    # Take a copy of the board to use for next game state
    tempBoard = deepcopy(self.board)
    #for cell in tempBoard:
      
    for i in range(self.rows):
      for j in range(self.cols):
        if self.board[i*self.cols + j] == 'X':
          alive = self.lifeCheck(i, j, True)
        else:
          alive = self.lifeCheck(i, j, False)
        tempBoard[i*self.cols + j] = 'X' if alive == True else '-'
        if alive == True:
          tempBoard[i*self.cols + j] = 'X'
        else:
          tempBoard[i*self.cols + j] = '-'
    self.board = deepcopy(tempBoard)

  def lifeCheck(self, row, col, alive):
    count = 0

    # Check the rows above and below the current cell
    # This will wrap around the edges
    # = = = 
    # - X - 
    # = = = 
    aboveRow = (row - 1) % self.rows
    belowRow = (row + 1) % self.rows



    #print(f"Row {row} and col {col}")

    for i in range(3):
      #print(f"Row {row} and col {col}", end=" ")
      #print(aboveRow*self.cols + ((col-1 + i) % self.cols))
      #print("2", end=" ")
      #print(f"Row {row} and col {col}", end=" ")
      #print(belowRow*self.cols + ((col-1 + i) % self.cols))
      if self.board[aboveRow*self.cols + ((col-1 + i) % self.cols)] == 'X':
        #print(f"Happened here: {aboveRow*self.cols + ((col-1 + i) % self.cols)}", end=" ")
        #print(count)
        count += 1
      if self.board[belowRow*self.cols + ((col-1 + i) % self.cols)] == 'X':
        #print(f"Happened here: {belowRow*self.cols + ((col-1 + i) % self.cols)}", end=" ")
        #print(count)
        count += 1
    
    # Check cells on the same row
    # - - - 
    # = X = 
    # - - - 
    #print(f"BEFORE Row {row} and col {col}", end=" ")
    #print(row*self.cols + ((col - 1) % self.cols))
    if self.board[row*self.cols + ((col - 1) % self.cols)] == 'X':
      #print(f"Happened here: {row*self.cols + ((col - 1) % self.cols)}", end=" ")
      #print(count)
      count += 1
    if self.board[row*self.cols + ((col + 1) % self.cols)] == 'X':
      #print(f"Happened here: {row*self.cols + ((col + 1) % self.cols)}", end=" ")
      #print(count)
      count += 1

    #print(f"Row {row} and col {col} and COUNT = {count}")
    if alive == True:
      if count <= 1:
        return False
      elif count >= 4:
        return False
      # Cell with 2 or 3 is all that is left
      else:
        return True
    # Otherwise current cell is dead
    else:
      if count == 3:
        return True
      else:
        return False

def main():
  newBoard = Board(5, 5) 
  newBoard.testState()
  count = 0
  while (count < 3):
    newBoard.printBoard()
    print("")
    newBoard.checkState()
    count += 1

if __name__ == '__main__':
    main()

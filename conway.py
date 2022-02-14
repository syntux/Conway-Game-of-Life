class Board:
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.board = ['X' for i in range(0, rows*cols)] 

  def printBoard(self):
    for i in range(self.rows):
      for j in range(self.cols):
        print(self.board[i*self.cols + j], end="")
      print("\n", end="")

def main():
  newBoard = Board(5, 5) 
  newBoard.printBoard()

if __name__ == '__main__':
    main()

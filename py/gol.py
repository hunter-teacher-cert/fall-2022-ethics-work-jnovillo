# gol.py
# Jessica Novillo Argudo
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: N/A


"""
The Rules of Life:
  Survivals:
   * A living cell with 2 or 3 living neighbours will survive for the next generation.
  Deaths:
   * Each cell with >3 neighbours will die from overpopulation.
   * Every cell with <2 neighbours will die from isolation.
  Births:
   * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.
  NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.
"""

import random

def gol():
  """ Create a board 25x25 and randomically set cells alive.
  Call function to get the next 10 generations """
  
  rows = 25
  cols = 25
  board = set_alive_cells(rows, cols)
  # 0 to 10 generations
  for i in range(0, 11):
    print("Gen %s:" % i)
    print_board(board)
    print()
    board = generate_next_board(board)


def set_alive_cells(rows, cols):
  """ Randomically set cells alive and return the board """
  
  board = []
  for row in range(0, rows): 
    board.append([])
    for col in range(0, cols):
      if 0.5 > random.random():
        board[row].append("X")
      else:
        board[row].append("-")
  return board


def print_board(board):
  """ Print board """
  
  for row in board:
    line = ""
    for col in row:
      line += col + " "
    print(line)
    

def generate_next_board(board):
  """ Generate and return a new board representing next generation """
  
  new_board = []
  for row in range(0, len(board)):
    new_board.append([])
    for col in range(0, len(board[row])):
      new_board[row].append(get_next_gen_cell(board, row, col))
  return new_board


def get_next_gen_cell(board, r, c):
  """ Set cell status for the next generation """
  
  nextGenCell = '-'
  neighbours = count_neighbours(board, r, c)
  if board[r][c] == 'X':
    if neighbours < 2 or neighbours > 3:
      nextGenCell = '-' 
    else:
      nextGenCell = 'X' 
  elif neighbours == 3:
    nextGenCell = 'X'
  return nextGenCell


def count_neighbours(board, r, c):
  """ Count and return a cell's living neighbors """
  
  living_neighbors = 0
  for i in range(r-1, r+2): 
    if i >= 0 and i < len(board): 
      for j in range(c-1, c+2): 
        if j >= 0 and j < len(board[r]):
          if i==r and j==c:
            continue
          elif board[i][j] == 'X':
            living_neighbors += 1
  return living_neighbors

  
# Call game of life function 
gol()
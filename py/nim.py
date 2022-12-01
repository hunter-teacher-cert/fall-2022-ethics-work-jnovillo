# nim.py
# Jessica Novillo Argudo
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: N/A


import random 

def nim():
  """ NIM GAME: While stones are available the user and the computer
  take turn to remove stones from the bag """

  print("***** WELCOME TO THE GAME OF NIM *****")
        
  stones = 12
  player = "user"

  while stones > 0:
    # user's turn
    if player == "user":
      # prompt user for input (user turn)
      stones_taken = get_user_input()
      # calculate the number of stones remaining
      while stones_taken > 3 or stones_taken < 1:
        print("Try again, you should enter 1, 2 or 3: ")
        stones_taken = get_user_input()
      while stones_taken > stones:
        print("There are only %s in the bag." % stones)
        print("Try again, you should enter a number <= to %s" % stones)
        stones_taken = get_user_input()
      # remove stones from the bag
      stones -= stones_taken
      # print remaining stones
      print_message(stones)
      if stones < 1:
        break
      player = "computer"
    # computer's turn
    elif player == "computer":
      stones_taken = random.randint(1, 3)
      if stones_taken > stones:
        stones_taken = stones
      print("Now the computer selects %s" % stones_taken)
      # remove stones from the bag
      stones -= stones_taken
      # print remaining stones
      print_message(stones)
      # check if win
      if stones < 1:
        break
      player = "user"
  print("Congratulation %s you are the winner!!!" % player)


def get_user_input():
  """Get user input and validate if it is an integer.
  Otherwise the user is asked to try again."""
  
  error_flag = True
  while error_flag:
    try:
      user_input = int(input(
        "How many stones would you like to remove from the bag (1, 2, or 3)? "))
      error_flag = False
    except ValueError:
      print ("Invalid entry, you should enter an integer 1, 2 or 3. Try again.")
  return user_input


def print_message(stones):
  """ Print remaining stones message """
  
  print("There %s now %s %s remaining." % (
        "is" if stones == 1 else "are", stones,
        "stone" if stones == 1 else "stones"))
  

# Call the nim game function 
nim()
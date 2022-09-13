# binsearch.py
# Jessica Novillo Argudo
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: N/A


def binsearch(data, value):
  """ Call the recursive binary search function
  and print the index of the target value """
  
  target_index = binsearch_recursive(data, value, 0, len(data) - 1)
  print("The number %s is located at index %s" % (value, target_index))


def binsearch_recursive(data, value, low_index, high_index):
  """ Binary search recursive """
  
  if high_index >= low_index:
    middle_index = int((low_index + high_index) / 2)
    if value == data[middle_index]:
      return middle_index
    elif value > data[middle_index]:
      return binsearch_recursive(data, value, middle_index + 1, high_index)
    elif value < data[middle_index]:
      return binsearch_recursive(data, value, low_index, middle_index - 1)
  return -1

  
# Create list
data = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]
print("Array: %s" % data)
# Call binsearch function sending the list data and the target value
binsearch(data, 4)
binsearch(data, 0)
binsearch(data, 10)
binsearch(data, 9)
binsearch(data, 15)
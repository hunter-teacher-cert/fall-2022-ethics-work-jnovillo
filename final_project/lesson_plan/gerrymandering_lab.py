"""
This script creates a map of voters with districts and generates gerrymandering.
"""

def change_coordinate(map, coord1, coord2):
  """
    Change district to generate gerrymandering
  """
  ## Your code to change districts here

  return map


def print_map(d_map):
  """
    Print the map
  """
    
  for row in d_map:
    row_map = []
    for column in row:
      row_map.append("{color}({district})".format(
        color=column['color'], district=column['district']))
    print(*row_map)


def who_win(d_map, district_count):
    """
    Determine who wins
    """
      
    blue_district = 0
    red_district = 0
    for district_number in range(district_count):
        blue_people = 0
        red_people = 0
        for row in d_map:
            for column in row:
                if column['district'] == district_number + 1:
                    if column['color'] == "B":
                        blue_people += 1
                    elif column['color'] == "R":
                        red_people += 1
                    else:
                        raise Exception("we have another color")
                elif column['district'] is None:
                    print("d_map", d_map)
                    raise Exception("There is no district")
        if blue_people == red_people:
            #print(district_number + 1, d_map)
            raise Exception("We have an equality")
        elif blue_people > red_people:
            blue_district += 1
        else:
            red_district += 1
    #self.print_map(d_map)
    if blue_district > red_district:
        print("Blue wins, B:{bd} R:{rd}".format(bd=blue_district, rd=red_district))
    elif red_district > blue_district:
        print("Red wins, B:{bd} R:{rd}".format(bd=blue_district, rd=red_district))
    else:
        print("Tie, B:{bd} R:{rd}".format(bd=blue_district, rd=red_district))
    return {'B': blue_district, 'R': red_district}

map = [
  [
    {'color': 'B', 'district': 1},
    {'color': 'R', 'district': 1},
    {'color': 'B', 'district': 1},
    {'color': 'R', 'district': 1},
    {'color': 'B', 'district': 2},
    {'color': 'R', 'district': 2}
  ],
  [
    {'color': 'B', 'district': 1},
    {'color': 'R', 'district': 1},
    {'color': 'R', 'district': 3},
    {'color': 'B', 'district': 3},
    {'color': 'B', 'district': 2},
    {'color': 'B', 'district': 2}
  ],
  [
    {'color': 'R', 'district': 1},
    {'color': 'R', 'district': 3},
    {'color': 'R', 'district': 3},
    {'color': 'B', 'district': 3},
    {'color': 'R', 'district': 3},
    {'color': 'R', 'district': 2}
  ],
  [
    {'color': 'R', 'district': 1},
    {'color': 'B', 'district': 3},
    {'color': 'B', 'district': 3},
    {'color': 'B', 'district': 4},
    {'color': 'B', 'district': 2},
    {'color': 'B', 'district': 2}
  ],
  [
    {'color': 'B', 'district': 1},
    {'color': 'R', 'district': 3},
    {'color': 'R', 'district': 4},
    {'color': 'B', 'district': 4},
    {'color': 'B', 'district': 2},
    {'color': 'B', 'district': 2}
  ],
  [
    {'color': 'R', 'district': 4},
    {'color': 'B', 'district': 4},
    {'color': 'R', 'district': 4},
    {'color': 'B', 'district': 4},
    {'color': 'B', 'district': 4},
    {'color': 'R', 'district': 4}
  ],
]

print_map(map)
district_count = 4
who_win(map, district_count)
# Call your function change_coordinate to generate gerrymandering
# changes districts to favor Blue party
# You may change more than one coordinate
# map = change_coordinate() 
# map = change_coordinate()
print_map(map)
who_win(map, district_count)
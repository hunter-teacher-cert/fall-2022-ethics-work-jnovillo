import random
import copy

class Gerry:
    """
    Class to generate a random map of voters (Blue or Red), create some
    random districts and then change those districts to generate gerrymandering.

    Restraining odd number of people for the moment otherwise to avoid complexity.

    Parameter: 
      row_column = number of rows and cols to create the map of voters.
      blue_percent = percentage of Blue voters
      distrinct_count = number of districts
      make_win = party that should win
      grouping_blue = Blue voters grouped together (True or False)
    
    If make_win ("B" or "R"), gerrymadering will be generated and the map will reflect it
    """
  
    def __init__(self, row_column=4, blue_percent=0.5, district_count=4, make_win=None,
                 grouping_blue=False):
        # total number of voters
        self.total_people = row_column * row_column
        # blue voters
        total_blue = int(self.total_people * blue_percent)
        number_blue, number_red = 0, 0
        # Some conditions to raise exceptons in case of errors
        if (self.total_people/district_count) != int(self.total_people/district_count):
            raise Exception("Please find a combination of row/column and district to have an odd number of people per district")
        if (self.total_people/district_count) % 2 == 0:
            raise Exception("Please find a combination of row/column and district to have an odd number of people per district")
        if (self.total_people/district_count) < 3:
            raise Exception("Few people in districts")
        self.district_count = district_count
        # map of voters
        self.map = []
        # Let's randomly create the map of voters
        for row in range(row_column):
            row_map = []
            for column in range(row_column):
                remaining_blue = total_blue - number_blue
                remaining_red = self.total_people - total_blue - number_red
                add_color = None
                if remaining_red == 0:
                    add_color = "B"
                elif remaining_blue == 0:
                    add_color = "R"
                else:
                    if grouping_blue is True:
                        add_color = "B"
                    else:
                        add_color = random.choices(
                            ["B", "R"],
                            weights=[remaining_blue, remaining_red])[0]
                if add_color == "B":
                    number_blue += 1
                    row_map.append({
                        'color': 'B',
                        'district': None
                    })
                elif add_color == "R":
                    number_red += 1
                    row_map.append({
                        'color': 'R',
                        'district': None
                    })
                else:
                    raise Exception("Something is wrong, no color has been attributed")
            self.map.append(row_map)
        # create districts
        self.start_district()
        # display the map
        self.print_map(self.map)
        # determine and display the winner
        r = self.who_win(self.map)
        self.last_failed_district = []
        self.last_successful_district = []
        # if make_win is R or B:
        iter = 0
        if make_win:
            if make_win == "R":
                look_for = "R"
                look_against = "B"
            elif make_win == "B":
                look_for = "B"
                look_against = "R"
            while r[look_for] <= r[look_against]:
                iter += 1
                if iter == 1000:
                    raise Exception("Too many iterations. Try again.")
                # run gerrymandering algorithm to find a possibility to make B or R win
                self.let_make_win(make_win)
                # determine and display the winner
                r = self.who_win(self.map)
        return None

  
    def who_win(self, d_map):
        """
        Determine who wins
        """
      
        blue_district = 0
        red_district = 0
        for district_number in range(self.district_count):
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

  
    def let_make_win(self, make_win):
        """
        Gerrymandering algorithm to find a possibility to make make_win (R or B) win
        As we do not go over all the possibilities, we are not always successfull
        Future improvement: Go over all the possibilities optimizing time

        Two techniques are applied:
          * First we try is cracking: Split voters of the same party across other districts.
          * If there is no success with cracking, then we try packing: Pack voters of the
            same party in one districkt, but the party’ voting strength is weakened in 
            another discrict where the other party has more voters.
        """
      
        dico_district = {}
        for district_number in range(self.district_count):
            blue_people = 0
            red_people = 0
            for row in self.map:
                for column in row:
                    if column['district'] == district_number + 1:
                        if column['color'] == "B":
                            blue_people += 1
                        elif column['color'] == "R":
                            red_people += 1
                        else:
                            raise Exception("We have another color")
                    elif column['district'] is None:
                        print("self.map", self.map)
                        raise Exception("There is no district")
            if blue_people == red_people:
                print(district_number + 1, self.map)
                raise Exception("We have an equality")
            elif blue_people > red_people:
                dico_district[district_number + 1] = {
                    'district_number': district_number + 1,
                    'winner': "B", 'blue_people': blue_people, 'red_people': red_people}
            else:
                dico_district[district_number + 1] = {
                    'district_number': district_number + 1,
                    'winner': "R", 'blue_people': blue_people, 'red_people': red_people}
        if make_win == "B":
            search = "R"
            looking_people = 'blue_people'
            looking_other_people = 'red_people'
        elif make_win == "R":
            search = "B"
            looking_people = 'red_people'
            looking_other_people = 'blue_people'
        district_list = []
        for dis in dico_district:
            district_list.append(dico_district[dis])
        district_list = sorted(district_list, key=lambda t:t[looking_people], reverse=True)
        district_winner = []
        district_to_improve = None
        district_to_decrease = None
        if self.last_successful_district:
            last_successful_district = self.last_successful_district[-1]
        else:
            last_successful_district = []
        for dis in district_list:
            if dis['winner'] == make_win:
                district_winner.append(dis)
        if len(district_winner) == len(district_list):
            return False
        elif district_winner:
            print("methods increase and decrease")
            found_districts = False
            for index in range(len(district_winner), len(district_list)):
                if found_districts is True:
                    break
                district_to_improve = district_list[index]['district_number']
                for index2 in range(len(district_winner)):
                    district_to_decrease = district_list[index2]['district_number']
                    if ((district_to_improve, district_to_decrease) in self.last_failed_district or
                        (district_to_decrease, district_to_improve) == last_successful_district):
                        continue
                    else:
                        found_districts = True
                        break
            print("district_to_decrease", dico_district[district_to_decrease][looking_people] - dico_district[
                district_to_decrease][looking_other_people])
            # If the district_to_decrease lost, then we are doing another technique packing
            if (dico_district[district_to_decrease][looking_people] - dico_district[
                district_to_decrease][looking_other_people] == 1 or (district_to_improve, district_to_decrease) in self.last_failed_district or
                        (district_to_decrease, district_to_improve) == last_successful_district):
                print("let's deplete one district")
                found_districts = False
                for dis in district_list[::-1]:
                    if found_districts is True:
                        break
                    if dis[looking_people] > 0:
                        district_to_decrease = dis['district_number']
                        for index in range(len(district_list)):                           
                            district_to_improve = district_list[index]['district_number']
                            print("check", district_to_improve, district_to_decrease,
                                  (district_to_improve, district_to_decrease) in self.last_failed_district)
                            if ((district_to_improve, district_to_decrease) in self.last_failed_district or 
                                (district_to_decrease, district_to_improve) == last_successful_district or
                                district_to_decrease == district_to_improve):
                                continue
                            else:
                                found_districts = True
                                break
                if district_to_decrease == district_to_improve:
                    print("Doing nothing, exit")
                    return False
        else:
            print("let's deplete one district")
            found_districts = False
            for dis in district_list[::-1]:
                if found_districts is True:
                    break
                if dis[looking_people] > 0:
                    district_to_decrease = dis['district_number']
                    for index in range(len(district_list)):
                        district_to_improve = district_list[index]['district_number']
                        if ((district_to_improve, district_to_decrease) in self.last_failed_district or 
                            (district_to_decrease, district_to_improve) == last_successful_district or
                            district_to_decrease == district_to_improve):
                            continue
                        else:
                            found_districts = True
                            break
            if district_to_decrease == district_to_improve:
                print("Doing nothing exit")
                return False
        improvement = self.improve_one_district(district_to_improve, district_to_decrease,
                                                        make_win)
        if improvement:
            self.map = improvement
            self.print_map(self.map)
            self.last_failed_district = []
            self.last_successful_district = [(district_to_improve, district_to_decrease)]
            return True
        else:
            self.last_failed_district.append((
                district_to_improve, district_to_decrease))
            return False

          
    def improve_one_district(self, district_to_improve, district_to_decrease, make_win):
        """
        Check if there a possibility to interchange coordinates between
        2 district to improve the result of district_to_improve
        """
      
        print("let's improve", district_to_improve, "and decrease", district_to_decrease)
        coord_to_improve, coord_to_decrease = self.find_around_other_district(
            self.map, district_to_improve, district_to_decrease, make_win)
        dico_result_begin = self.who_win(self.map)
        #print("coord to improve", coord_to_improve, coord_to_decrease)
        for coord_improve in coord_to_improve:
            for coord_decrease in coord_to_decrease:
                d_map = copy.deepcopy(self.map)
                d_map[coord_improve[0]][coord_improve[1]]['district'] = district_to_improve
                d_map[coord_decrease[0]][coord_decrease[1]]['district'] = district_to_decrease
                print("Changing coordinates ", coord_improve, coord_decrease)
                check_is_good = self.check_district_still_compact(d_map)
                if check_is_good:
                    dico_result_now = self.who_win(d_map)
                    if make_win == "R":
                        if dico_result_now['R'] >= dico_result_begin['R']:
                            # Returning the first success
                            # We could do more here, but lack of time
                            return d_map
                        else:
                            continue
                    elif make_win == "B":
                        if dico_result_now['B'] >= dico_result_begin['B']:
                            return d_map
                        else:
                            continue
        return False

      
    def check_district_still_compact(self, d_map):
        """
        After interchaning 2 coordinates of 2 differents district
        check that the districts are still together and not apart
        """
      
        for district_number in range(self.district_count):
            coord_list = []
            for line, row in enumerate(d_map):
                for col, column in enumerate(row):
                    if column['district'] == district_number + 1:
                        coord_list.append((line, col))
            coord_together = []
            for coord in coord_list:
                found_one = False
                for mov in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    new_row = coord[0] + mov[0]
                    new_col = coord[1] + mov[1]
                    if (new_row, new_col) in coord_list:
                        found_one = True
                        coord_together.append([coord, (new_row, new_col)])
                if found_one is False:
                    print("map modified")
                    self.print_map(d_map)
                    return False
            done_cleaning = False
            found_list = []
            while done_cleaning is False:
                done_cleaning = True
                delete_coord = []
                for index, (coord_1, coord_2) in enumerate(coord_together):
                    if found_list == []:
                        found_list.append(coord_1)
                        found_list.append(coord_2)
                        delete_coord.append(index)
                    else:
                        if coord_1 in found_list:
                            if coord_2 not in found_list:
                                found_list.append(coord_2)
                            delete_coord.append(index)
                        elif coord_2 in found_list:
                            if coord_1 not in found_list:
                                found_list.append(coord_1)
                            delete_coord.append(index)
                if delete_coord:
                    done_cleaning = False
                    for index in sorted(delete_coord, reverse=True):
                        coord_together.pop(index)
                    delete_coord = []
            if coord_together:
                print("coord together", coord_together, found_list)
                print("map modified coord together")
                #self.print_map(d_map)
                return False
        return True

      
    def start_district(self):
        """
        Populate all the district, if there is an error, restart everything
        after 50 tries, stop it
        """
      
        people_per_district = int(self.total_people/self.district_count)
        self.district_population = []
        for district in range(self.district_count):
            self.district_population.append(people_per_district)
        if sum(self.district_population) > self.total_people:
            raise Exception("Something went wrong, there are too much people")
        elif sum(self.district_population) < self.total_people:
            district = 0
            while sum(self.district_population) < self.total_people:
                self.district_population[district] += 1
                district += 1
                if district == len(self.district_population):
                    district = 0
        map_done = False
        iteration = 0
        map_not_working = []
        while map_done is False:
            map_done = True
            iteration += 1
            print("iteration", iteration)
            if iteration == 50:
                raise Exception("Too much iteration without any success")
            self.restart_district()
            for district_number in range(self.district_count):
                temp_map = self.create_district(district_number + 1)
                if temp_map is False:
                    map_done = False
                    break
                else:
                    self.map = temp_map

  
    def restart_district(self):
        """
        Restart a district -> None
        """
      
        for row in self.map:
            for column in row:
                if column['district']:
                    column['district'] = None

  
    def create_district(self, district_number):
        """
        Create a district. If is not possible, return False
        """
      
        people_in_district = self.how_many_in_district(district_number, self.map)
        if people_in_district > 0:
            raise Exception("There are already people in the district")
        first_coord = (None, None)
        coord_found = False
        for line, row in enumerate(self.map):
            if coord_found is True:
                break
            for col, column in enumerate(row):
                if column['district'] is None:
                   first_coord = (line, col)
                   coord_found = True
                   break
        map_list = self.build_a_district(
            district_number, first_coord, self.map)
        if not map_list:
            print("bad", district_number)
            return False
        else:
            return random.choice(map_list)

          
    def how_many_color_people_in_district(self, color, district_number, d_map):
        """
        Count people of a certain color in a district
        """
      
        people = 0
        for row in d_map:
            for column in row:
                if column['district'] == district_number and column['color'] == color:
                    people += 1
        return people

      
    def how_many_in_district(self, district_number, d_map):
        """
        Count total people in a distric
        """
      
        people = 0
        for row in d_map:
            for column in row:
                if column['district'] == district_number:
                    people += 1
        return people
   
   
    def build_a_district(self, district_number, coord, d_map):
        """
        Building a district recursively (with a district number over the map). 
        The district is created randomly.
        If it is not possible to build a district, return an empty list.
        """
      
        temp_map = copy.deepcopy(d_map)
        self.set_up_people_in_a_district(coord[0], coord[1], district_number, temp_map)
        district_population = self.how_many_in_district(district_number, temp_map)
        if district_population == self.district_population[district_number - 1]:
            if district_population % 2:
                return [temp_map]
            else:
                if self.is_there_a_winner(district_number, temp_map):
                    return [temp_map]
                else:
                    return []
        map_list = []
        next_moves = self.next_coord_possible(temp_map, district_number)
        if not next_moves:
            return []
        for coord in next_moves:
            map_list_temp = self.build_a_district(
                district_number, coord, temp_map)
            for ml in map_list_temp:
                if self.is_map_blocked(ml):
                    continue
                if ml not in map_list:
                    map_list.append(ml)
        return map_list

  
    def is_there_a_winner(self, district_number, d_map):
        """
        Check if each district has a winner
        """
      
        blue_population = 0
        for row in d_map:
            for column in row:
                if column['district'] == district_number and column['color'] == "B":
                    blue_population += 1
        red_population = self.district_population[district_number -1] - blue_population
        if blue_population == red_population:
            return False
        else:
            if blue_population > red_population:
                return [True, 'B']
            else:
                return [True, 'R']

  
    def set_up_people_in_a_district(self, row, column, district_number, d_map=None):
        """
        Populate a district
        """
      
        mapo = None
        if d_map is None:
            mapo = self.map
        else:
            mapo = d_map
        if mapo[row][column]['district'] is not None:
            raise Exception("({row}, {column}) is already in a district".format(
                row=row, column=column))
        mapo[row][column]['district'] = district_number
        
    
    def is_map_blocked(self, d_map):
        """
        Check if there is a blockage assigning a district
        (a free point surrounded by only a district point)
        """
      
        for line, row in enumerate(d_map):
            for col, column in enumerate(row):
                if column['district'] is None:
                    next_move = self.find_around_free(d_map, line, col)
                    if not next_move:
                        return True
        return False

      
    def next_coord_possible(self, d_map, district_number):
        """
        Return one random point which is not in a district yet
        and is adjacent to the district
        """
      
        next_moves = []
        for line, row in enumerate(d_map):
            for col, column in enumerate(row):
                if column['district'] == district_number:
                    next_coord_list = self.find_around_free(d_map, line, col)
                    if next_coord_list:
                        next_moves += next_coord_list
        next_moves = list(set(next_moves))
        if next_moves:
            return [random.choice(next_moves)]
        else:
            return []
          
                    
    def find_around_free(self, d_map, row, col):
        """
        Around one point (row, col) find coordinates which are not in
        a district yet
        """

        coord_list = []
        mouvement_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        random.shuffle(mouvement_list)
        for row_adj, col_adj in mouvement_list:
            new_row = row + row_adj
            new_col = col + col_adj
            if new_row < 0 or new_row >= len(d_map):
                continue
            if new_col < 0 or new_col >= len(d_map[0]):
                continue
            if d_map[new_row][new_col]['district'] is None:
                return [(new_row, new_col)]
        return coord_list

  
    def find_around_other_district(self, d_map, district_1, district_2, make_win):
        """
        Iterate over each coordinate on the map to find coordinates of
        district_1 and district_2 to interchange to be able
        to add one more voter on district_1 and one less for district_2
        (voter equal to make_win)
        """
      
        coord_list_1, coord_list_2 = [], []
        for line, row in enumerate(d_map):
            for col, column in enumerate(row):
                if column['district'] == district_1:
                    mouvement_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for mov in mouvement_list:
                        new_row = line + mov[0]
                        new_col = col + mov[1]
                        if new_row < 0 or new_row >= len(d_map):
                            continue
                        if new_col < 0 or new_col >= len(d_map[0]):
                            continue
                        if (d_map[new_row][new_col]['district'] == district_2 and
                            d_map[new_row][new_col]['color'] == make_win):
                            coord_list_1.append((new_row, new_col))
        for line, row in enumerate(d_map):
            for col, column in enumerate(row):
                if column['district'] == district_2:
                    mouvement_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for mov in mouvement_list:
                        new_row = line + mov[0]
                        new_col = col + mov[1]
                        if new_row < 0 or new_row >= len(d_map):
                            continue
                        if new_col < 0 or new_col >= len(d_map[0]):
                            continue
                        if (d_map[new_row][new_col]['district'] == district_1 and
                            d_map[new_row][new_col]['color'] != make_win):
                            coord_list_2.append((new_row, new_col))
        dico_coord_1 = {}
        for coord in coord_list_1:
            if coord not in dico_coord_1:
                dico_coord_1[coord] = 0
            dico_coord_1[coord] += 1
        dico_coord_2 = {}
        for coord in coord_list_2:
            if coord not in dico_coord_2:
                dico_coord_2[coord] = 0
            dico_coord_2[coord] += 1
        coord_list_1, coord_list_2 = [], []
        for coord in dico_coord_1:
            coord_list_1.append([coord, dico_coord_1[coord]])
        for coord in dico_coord_2:
            coord_list_2.append([coord, dico_coord_2[coord]])
        coord_list_1 = sorted(coord_list_1, key=lambda t:t[1], reverse=True)
        coord_list_2 = sorted(coord_list_2, key=lambda t:t[1], reverse=True)
        coord_list_1 = [coord[0] for coord in coord_list_1]
        coord_list_2 = [coord[0] for coord in coord_list_2]
        return coord_list_1, coord_list_2

      
    def print_map(self, d_map):
        """
        Print the map
        """
      
        for row in d_map:
            row_map = []
            for column in row:
                row_map.append("{color}({district})".format(
                    color=column['color'], district=column['district']))
            print(*row_map)


if __name__ == '__main__':
    Gerry(row_column=6, blue_percent=0.55, district_count=4, make_win="R", grouping_blue=False)
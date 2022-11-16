"""
Plane Seating Algorithm

Collaborators: Jessica Novillo Argudo, Harrison Fung, Shana Elizabeth Henry
"""

"""This program simulates the sales of tickets for a specific flight.

A plane is represented by a list. Each element of the list is a row in
the plane (with plane[0] being the front) and reach row is also a
list.

Seats can be purchased as economy_plus or regular economy.

Economy_plus passengers select their seats when they purchase their tickts.
Economy passengers are assigned randomly when the flight is closer to full

create_plane(rows,cols):
  Creates and returns a plane of size rowsxcols
  Plans have windows but no aisles (to keep the simulation simple)

get_number_economy_sold(economy_sold):
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex: {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3
    seats, the Lee family 2

    Returns: the total number of seats sold

get_avail_seats(plane,economy_sold):
    Parameters: plane : a list of lists representing plaine
    economy_sold : a dictionary of the economy seats sold but
                   not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats
           that are "avail" or "win" and removes the number of
           economy_sold seats

get_total_seats(plane):
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane

get_plane_string(plane):
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 

purchase_economy_plus(plane,economy_sold,name):
    Params: plane - a list of lists representing a plane

            economy_sold - a dictionary representing the economy
                           sold but not assigned
            name - the name of the person purchasing the seat

    This routine randomly selects a seat for a person purchasing
    economy_plus. Preference is given to window and front seats.

seat_economy(plane,economy_sold,name):
    Similar to purchase_economy_plus but just randomy assigns
    a random seat.

purchase_economy_block(plane,economy_sold,number,name):
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary


fill_plane(plane):
  takes an empty plane and runs our simulation to sell seats and then
  seat the economy passengers. See comments in the function for details. 

main():
  The main driver program - start here

"""
import random


def create_plane(rows,cols):
    """

    returns a new plane of size rowsxcols

    A plane is represented by a list of lists. 

    This routine marks the empty window seats as "win" and other empties as "avail"
    """
    plane = []
    for r in range(rows):
        s = ["win"]+["avail"]*(cols-2)+["win"]
        plane.append(s)
    return plane

def get_number_economy_sold(economy_sold):
    """
    Input: a dicitonary containing the number of regular economy seats sold. 
           the keys are the names for the tickets and the values are how many

    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2

    Returns: the total number of seats sold
    """
    sold = 0
    for v in economy_sold.values():
        sold = sold + v["number"]
    return sold


def get_avail_seats(plane,economy_sold):
    """
    Parameters: plane : a list of lists representing plaine
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned

    Returns: the number of unsold seats

    Notes: this loops over the plane and counts the number of seats that are "avail" or "win" 
           and removes the number of economy_sold seats
    """
    avail = 0;
    for r in plane:
        for c in r:
            if c == "avail" or c == "win":
                avail = avail + 1
    avail = avail - get_number_economy_sold(economy_sold)
    return avail

def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing. 
    """
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s


def purchase_economy_plus(plane,economy_sold,name):
    """
    Params: plane - a list of lists representing a plane
            economy_sold - a dictionary representing the economy sold but not assigned
            name - the name of the person purchasing the seat
    """
    rows = len(plane)
    cols = len(plane[0])

    
    # total unassigned seats
    seats = get_avail_seats(plane,economy_sold)

    # exit if we have no more seats
    if seats < 1:
        return plane


    # 70% chance that the customer tries to purchase a window seat
    # it this by making a list of all the rows, randomizing it
    # and then trying each row to try to grab a seat

    
    if random.randrange(100) > 30:
        # make a list of all the rows using a list comprehension
        order = [x for x in range(rows)]

        # randomzie it
        random.shuffle(order)

        # go through the randomized list to see if there's an available seat
        # and if there is, assign it and return the new plane
        for row in order:
            if plane[row][0] == "win":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0])-1] == "win":
                plane[row][len(plane[0])-1] = name
                return  plane

    # if no window was available, just keep trying a random seat until we find an
    # available one, then assign it and return the new plane
    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


# THIS WILL BE LEFT EMPTY FOR THE FIRST STAGE OF THE PROJECT
def seat_economy(plane,economy_sold,name):
    """
    This is mostly the same as the purchase_economy_plus routine but 
    just does the random assignment. 

    We use this when we're ready to assign the economy seats after most 
    of the economy plus seats are sold

 
    """
    rows = len(plane)
    cols = len(plane[0])

    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "win" or plane[r_row][r_col] == "avail":
            plane[r_row][r_col] = name
            found_seat = True
    return plane


def purchase_economy_block(plane,economy_sold,number,name, option):
    """
    Purchase regular economy seats. As long as there are sufficient seats
    available, store the name and number of seats purchased in the
    economy_sold dictionary and return the new dictionary

    """
    #seats_avail = get_total_seats(plane)
    #seats_avail = seats_avail - get_number_economy_sold(economy_sold)
    seats_avail = get_avail_seats(plane, economy_sold)

    if seats_avail >= number:
        economy_sold[name]={"number": number, "option": option}
    return economy_sold


def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane

    comments interspersed in the code

    """

    
    economy_sold={}
    total_seats = get_total_seats(plane)
    


    # these are for naming the pasengers and families by
    # appending a number to either "ep" for economy plus or "u" for unassigned economy seat
    ep_number=1
    u_number=1

    # MODIFY THIS
    # you will probably want to change parts of this
    # for example, when to stop purchases, the probabilities, maybe the size for the random
    # regular economy size

    options = ["family", "group", "alone"]
    max_family_size = 3
    
    while total_seats > 1:
        option = random.choice(options)
        if option == "family":
          passengers = create_family(max_family_size) # dictionary 
          number_passengers = len(passengers)
          children = 1 # for this assigment we only consider one child per family to reduce complexity, a future implementation should consider more than 1 child per family
        elif option == "group":
          number_passengers = random.randint(2, max_family_size)
        elif option == "alone":
          number_passengers = 1
        if number_passengers > total_seats:
          continue
        r = random.randrange(100)
        if r > 30:
            name = "ep-%d" % ep_number
            if option == "alone":
                plane = purchase_economy_plus(plane,economy_sold,name)
                print("Customer flying alone %s has been accommodated" % name)
            elif option == "group":
                plane = accommodate_group(plane, number_passengers, name, economy_sold, "ep")
            elif option == "family":
                plane = accommodate_family(plane, number_passengers, name, economy_sold, "ep") # we consider 1 child per family, so no need to send number of children as parameter, but for a future implementation when there will be more than 1 child then the number of children should be added as parameter
            print(get_plane_string(plane))
            ep_number = ep_number + 1
           # total_seats = get_avail_seats(plane,economy_sold)
        else:
            #economy_sold = purchase_economy_block(plane,economy_sold,1+random.randrange(max_family_size),"u-%d"%u_number)
            economy_sold = purchase_economy_block(plane,economy_sold,number_passengers,"u-%d"%u_number, option)
            u_number = u_number + 1
        total_seats = get_avail_seats(plane,economy_sold)
            
    # once the plane reaches a certian seating capacity, assign
    # seats to the economy plus passengers
    # you will have to complete the seat_economy function
    # Alternatively you can rewrite this section

    priorities = {"family": [], "group": [], "alone": []} # priority to assign economy seats
    for name in economy_sold.keys():
        if economy_sold[name]["option"] == "alone": # people flying alone
            priorities['alone'].append(name)
        elif economy_sold[name]["option"] == "group": # group of people flying together
            priorities['group'].append(name)
        elif economy_sold[name]["option"] == "family": # families
            priorities['family'].append(name)
    for priority in ["family", "group", "alone"]: # accomdate customers based on their priority
        # ther priority order is family, group, alone
        for name in priorities[priority]:
            if priority == "family":
                plane = accommodate_family(plane, economy_sold[name]["number"], name, economy_sold, "u") 
            elif priority == "group":
                plane = accommodate_group(plane, economy_sold[name]["number"], name, economy_sold, "u")
            else:
                plane = seat_economy(plane, economy_sold, name)
                print("Customer flying alone %s has been accommodated" % name)
            print(get_plane_string(plane))
    return plane


def accommodate_group(plane, number_passengers, name, economy_sold, category):
    """
    This function tries to accommodate a group of people flying together in consecutive seats
    """
  
    print("Trying to allocate a group of %s together" % number_passengers)
    selected_seats = find_consecutive_seats(plane, number_passengers)
    if selected_seats != []: # if consecutive seats found
        plane = assign_selected_seats(plane, selected_seats, name)
        print("The group of %s %s has been allocated together" % (number_passengers, name))
    else: # when no consecutive seats found, seats will se assigned following the economy and economy plus rules
        for i in range(number_passengers):
            if category == "ep":
                plane = purchase_economy_plus(plane, economy_sold, name)
            else:
                plane = seat_economy(plane, economy_sold, name)
        print("The group of %s %s could not be allocated together" % (number_passengers, name))
    return plane

  
def accommodate_family(plane, number_passengers, name, economy_sold, category):
    """
    This function tries to accommodate families together. If not possible, it will try to 
    accommodate at least one adult with a child. If that is not possible, then seats will not 
    be assigned and a message will be displayed indicating that is not possible to
    allocate the family
    """
  
    print("Trying to allocate a family of %s that includes at least one child together" % number_passengers)
    selected_seats = find_consecutive_seats(plane, number_passengers)
    if selected_seats != []: # if consecutive seats were found
        plane = assign_selected_seats(plane, selected_seats, name)
        print("The family of %s %s has been allocated together" % (number_passengers, name))
    else:
        selected_seats = find_consecutive_seats(plane, 2) # find consecutive seats for 1 adult + 1 child
        if selected_seats != []: # if consecutive seats found for 1 adult + 1 child
            plane = assign_selected_seats(plane, selected_seats, name)
            for i in range(number_passengers - 2): # pending adults who need a seat
                if category == "ep":
                    plane = purchase_economy_plus(plane, economy_sold, name)
                else:
                    plane = seat_economy(plane, economy_sold, name)
            print("The family of %s %s was separated, but the child is next to an adult" % (number_passengers, name))
        else: # consecutive seats were not found
            print("The family of %s %s could not been allocated in the plane because there are not consecutive seats to have the child next to an adult." % (number_passengers, name))
    return plane

  
def assign_selected_seats(plane, selected_seats, name):
    """
    Assign seats to customers
    """
    for seat in selected_seats:
        plane[seat[0]][seat[1]] = name
    return plane


def find_consecutive_seats(plane, num_passengers):
    """
    Find consecutive seats in the plane. 
    If found returns an array with the seats, otherwise returns an empty array
    """
    seats = []
    for i, row in enumerate(plane):
        consecutive_seats = 0
        for j, cols in enumerate(row):
            if plane[i][j] == "win" or plane[i][j] == "avail":
                consecutive_seats += 1
                if consecutive_seats == num_passengers:
                  for index in range(num_passengers):
                    seats.append((i, j - index))
                  break
        if seats != []:
          break
    return seats

  
def create_family(max_family_size):
    """
    Generates a dictionary with the family members and their ages
    """
    passengers_info = {}
    children = 1 # to reduce complexity the code will consider only one child per family
    number_passengers = random.randrange(1, max_family_size) # generates number of adults, include 1, size not included
    counter_family = 0
    for i in range(number_passengers):
        passengers_info['family-' + str(counter_family+1)] = random.randint(12, 100) # randomly assigns ages to the adults
        counter_family += 1
    for i in range(children):
        passengers_info['family-' + str(counter_family+1)] = random.randint(2, 11) # randomly assigns ages to children betwee 2 and 11
        counter_family += 1
    return passengers_info 

  
def main():
    plane = create_plane(10,5)
    plane = fill_plane(plane)
    print("Final configuration")
    print(get_plane_string(plane))
if __name__=="__main__":
    main()
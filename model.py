# LFSR Simulator
# model.py
# Created by Mauro J. Pappaterra on 19 of August 2018.
from random import *

def lfsr ():
    """LFSR algorithm for generating random numbers"""

    MIN = 10
    MAX = 50 #9999

    seed = [0] * randint(MIN, MAX) # creates an empty seed with randomized size
    seed[0] = 1

    # FOR TESTING PURPOSES
    print(seed)

    seed_size =  len (seed)

    print ("Size of seed is of " + str(seed_size) + " cells")

    # Choose number of cells to become marked

    MIN_cells = 4
    MAX_cells = seed_size

    no_cells = randint (MIN_cells, MAX_cells)

    selected_cells = []

    print ("Selecting " + str(no_cells) + " cells")

    while (no_cells > 0):
        new_random = randint (0, seed_size - 1)

        #print("new number! " + str(new_random))

        if (not has(selected_cells, new_random)):
            selected_cells.append(new_random)
            #print("added! " + str(new_random))
            no_cells -= 1

    print (selected_cells)

    MIN_loops = 10
    MAX_loops = 100 #9999

    print("\nSeed -> " + print_seed(seed)) # print original seed

    loops =  randint (MIN_loops, MAX_loops)

    while (loops > 0):
        new_seed = 0

        for index in selected_cells:
            new_seed += seed [index]

        new_seed = new_seed % 2

        seed.insert (0,new_seed) # insert new seed on index 0
        del seed[-1] # delete last element

        # FOR TESTING PURPOSES
        #print("Loop -> " + str(loops) + " Shifting a -> " + str(new_seed))
        print("Seed -> " + print_seed(seed))

        loops -= 1

    random_binary = int("".join([str(x) for x in seed if True]), base = 10)
    random_decimal = int (random_binary)

    print("\nNew Random number -> " + str(random_binary) + " -> " + str(random_decimal))


def has (numbers_array, new_number):

    for number in numbers_array:
        if (number == new_number):
            return True

    return False

def print_seed (seed):

    print_this = ""

    for number in seed:
        print_this += " | " + str(number)

    return print_this + " | "

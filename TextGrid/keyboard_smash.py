"""
Keyboard smash

Write a program in keyboard_smash.py which generates a TextGrid with 1 row and NUM_LETTERS columns of randomly populated letters. To help, we've provided you with a get_random_value() function that randomly returns one of the most smashable keyboard characters -- the characters in the middle row of the keyboard.

Here's a sample run of the program (since randomness is involved, your output likely won't be the same):

$ python keyboard_smash.py
;SSL;J;JSL
"""

import random

from TextGrid import TextGrid

SMASHABLE_LETTERS = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';']
NUM_LETTERS = 10

def main():
    grid = TextGrid.blank(NUM_LETTERS, 1)
    
    # TODO: your code here!
    
    # Using a For-each loop, since all cells need to be changed, preferable due to shorter, more concise code: 
    
    for cell in grid:
        cell.value = get_random_value()
    # Using a classic for loop choosing all cells in x, requiring more lines:
    
    # for x in range(grid.width):
    #     random_value = get_random_value()
    #     cell = grid.get_cell(x, 0)
    #     cell.value = random_value
    
    print(grid)

def get_random_value():
    idx = random.randint(0,len(SMASHABLE_LETTERS) - 1) # randomly generate an index
    return SMASHABLE_LETTERS[idx] # return alphabetic letter

if __name__ == '__main__':
    main()

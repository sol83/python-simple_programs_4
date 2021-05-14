"""
Straight A's

Write a program in straight_As.py which will scan a TextGrid from left to right and top to bottom and, as soon as it encounters the letter 'A' (all the letters in the grid are guaranteed to be uppercase), changes all letters following the first occurrence of 'A' to the letter 'A'.

For example, for an input grid like this (this is the text of guava.txt, the default file):

GUAVA
GUAVA
GUAVA

The output should be:

GUAAA
AAAAA
AAAAA

We've provided you three files to test your code on -- guava.txt, antelope.txt, and honolulu.txt. Check them out in the file explorer, and change the value of DEFAULT_FILENAME to change which file is read into grid!

For this problem, we recommend you initialize a boolean variable and use it to keep track of whether you've seen the letter A already, or not.
"""

from TextGrid import TextGrid

DEFAULT_FILENAME = 'txt_files/guava.txt'

def main():
    grid = TextGrid(DEFAULT_FILENAME)
    # TODO: your code here!
    letter_A_seen = False # boolean value which will serve as a switch

    for y in range(grid.height):
        for x in range(grid.width):
            cell = grid.get_cell(x, y)
            if cell.value == 'A':
                letter_A_seen = True # flip the switch!
            if letter_A_seen:
                cell.value = 'A'
    
    print(grid)

if __name__ == '__main__':
    main()

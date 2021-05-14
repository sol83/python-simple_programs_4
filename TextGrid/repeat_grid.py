"""
Repeat grid

Write a program in repeat_grid.py that copies gridonto final_grid over and over, NUM_REPEATS times, side by side. Here's a sample run of the program on the default grid, abcd.txt, with NUM_REPEATS = 2 (this is the default value):

$ python repeat_grid.py
Initial grid:
AB
CD
Final grid:
ABAB
CDCD
"""

from TextGrid import TextGrid

DEFAULT_FILENAME = 'txt_files/abcd.txt'
NUM_REPEATS = 4

def main():
    grid = TextGrid(DEFAULT_FILENAME)
    print("Initial grid:")
    print(grid)
    final_grid = TextGrid.blank(NUM_REPEATS * grid.width, grid.height)
    
    # TODO: your code here!
    for repeat in range(NUM_REPEATS):
        start_x = grid.width * repeat
        for x in range(grid.width):
            for y in range(grid.height):
                cell = grid.get_cell(x, y)
                final_grid.set_cell(start_x + x, y, cell)
   
    print("Final grid:")
    print(final_grid)

if __name__ == '__main__':
    main()

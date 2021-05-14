"""
Digital negative

Write a program in digital_negative.py which takes a TextGrid of 0s and 1s and changes all 0s to 1s, and all 1s to 0s.

Here's a sample run of the program on zero_one.txt, which is the default file:

$ python digital_negative.py
Initial grid:
0000
1111
New grid:
1111
0000

We've additionally provided you with a checkerboard.txt file to test your code on; you can run your program on this file by changing DEFAULT_FILENAME to 'checkerboard.txt'.

Recall that you can access the value of a cell in the TextGrid using cell.value, and that all letter values are strings, not ints!
"""

from TextGrid import TextGrid

DEFAULT_FILENAME = 'txt_files/zero_one.txt'

def main():
    grid = TextGrid(DEFAULT_FILENAME)
    print("Initial grid:")
    print(grid)

    # TODO: your code here!
    for cell in grid:
        if cell.value == '0':
            cell.value = '1'
        else:
            cell.value = '0'     
    
    print("New grid:")
    print(grid)

if __name__ == '__main__':
    main()

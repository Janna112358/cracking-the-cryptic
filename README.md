# cracking-the-cryptic
Some python program(s?) to help with cracking the cryptic puzzles

## deep-thought
To help with the Deep Thought sudoku for THGTTG sudoku hunt 
(patreon content, not publicly availabe, sorry).

You can run the script deep_thought.py with python3. 

When run, the script computes all possible "boxes" according to the rules 
of Deep Thought (paraphrased):
 A box contains two digits in its top row, 
which multiplied together form a two-digit number that
occupies the bottom row of a box. 
For example:
    3  7 
    2  1
because 3 x 7 = 21
Representations of the boxes are saved to a file in the run directory, named 
all_boxes.txt (this is the same as the file in this repository). 
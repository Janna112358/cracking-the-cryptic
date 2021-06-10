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
    6  9 
    4  2
because 6 x 9 = 42 (oh yeah did I mention this is in base 13?!)
Representations of the boxes are saved to a file in the run directory, named 
all_boxes.txt (also [in this repository](https://github.com/Janna112358/cracking-the-cryptic/blob/master/all_boxes.txt)).

The script also allows checking if two boxes can form a "domino", i.e. if they
can be placed next to each other, overlapping in one column. For example:   
    6  9   and   9  3
    4  2         2  1
can domino, because the 9, 2 columns can overlap, and there are no other repeated
digits in each row.
Because there is a "triple domino" i.e threes boxes next to each other overlapping
in the puzzle, the script computes all possible combinations of boxes that do so.
These results are saved in the file triple_dominoes.txt (also [in this repository](https://github.com/Janna112358/cracking-the-cryptic/blob/master/triple_dominoes.txt)).
There is also a domino which sits entirely within one box of the sudoku, and therefore
can have none of its digits repeated. Possibilities for this are checked and saved in
no_repeat_dominoes.txt (also [in this repository](https://github.com/Janna112358/cracking-the-cryptic/blob/master/no_repeat_dominoes.txt))

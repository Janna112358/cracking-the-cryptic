"""
From a sudoku with additional rules about 2x2 boxes:
    
[paraphrased] A box contains two digits in its top row, 
which multiplied together form a two-digit number that
occupies the bottom row of a box. 
For example:
    3  7 
    2  1
because 3 x 7 = 21

This program figures out all valid boxes.
"""

import itertools

class Box:
    def __init__(self, topLeft, topRight, bottomLeft, bottomRight):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        
    def __repr__(self):
        return f"\n{self.topLeft} | {self.topRight}\n{self.bottomLeft} | {self.bottomRight}\n"
        
    def hasNoRepeats(self):
        """
        Check if this box could fit within a single box of the sudoku, i.e. has
        no repeated digits
        """
        return (self.topLeft != self.bottomRight and 
                self.bottomLeft != self.topRight)
    
    def doesDominoRight(self, other):
        """
        Check if this box can "domino" (overlap) with another box on its right
        """
        doesOverlap = (self.topRight == other.topLeft and 
                       self.bottomRight == other.bottomLeft)
        rowsOk = (self.topLeft != other.topRight and 
                  self.bottomLeft != other.bottomRight)
        return doesOverlap and rowsOk

    def doesDominoLeft(self, other):
        """
        Check if this box can "domino" (overlap) with another box on its left
        """
        return other.doesDominoRight(self)
    
    def doesDominoRightNoRepeat(self, other):
        """
        Check if this box can "domino" with another no its right, without having
        other digits repeated.
        """
        noRepeats = (self.hasNoRepeats() and 
                     other.hasNoRepeats() and 
                     self.topLeft != other.bottomRight and 
                     self.bottomLeft != other.topRight)
        return noRepeats and self.doesDominoRight(other)
    
    def doesDominoLeftNoRepeat(self, other):
        """
        Check if this box can "domino" with another no its left, without having
        other digits repeated.
        """
        return other.doesDominoRightNoRepeat(self)

    @classmethod
    def createIfValid(self, topLeft, topRight): 
        # sudoku
        if topLeft == topRight: 
            return None
        
        # find 2-digit product
        product = topLeft * topRight 
        if product < 10 or product > 99: 
            return None 
        bottomLeft = product // 10
        bottomRight = product%10
        
        # sudoku (no zeros) 
        if bottomRight == 0: 
            return None
        # sudoku
        if bottomLeft == bottomRight: 
            return None 
        if bottomLeft == topLeft or bottomRight == topRight:
            return None 
        
        return self(topLeft, topRight, bottomLeft, bottomRight)
        
    @classmethod
    def createAllValid(self): 
        allValidBoxes = []
        
        digits = range(1, 10)
        for i in digits:
            for j in digits: 
                box = self.createIfValid(i, j)
                if box is not None:
                    allValidBoxes.append(box)
        return allValidBoxes
    
def findNoRepeatDominoes():
    """Find all combinations of boxes that can "domino" and fit within
    a sudoku box.
    
    They have to overlap on one column to domino. To fit within a sudoku box,
    there can be no repeat digits (which is relevant for the other columns). 
    """ 
    dominoes = []
    
    boxes = Box.createAllValid()
    for box1, box2 in itertools.product(boxes, boxes):
        if box1 is box2:
            continue
        if box1.doesDominoRightNoRepeat(box2):
            dominoes.append([box1, box2])
    return dominoes
    
    
def findTripleDominoes():
    triples = []
    
    boxes = Box.createAllValid()
    for box1, box2, box3 in itertools.product(boxes, boxes, boxes):
        if box1 is box2 or box1 is box3 or box2 is box3: 
            continue
        
        if not box1.doesDominoRight(box2): 
            continue
        if not box2.doesDominoRight(box3):
            continue
        
        if (box1.topLeft == box3.topRight or 
            box1.bottomLeft == box3.bottomRight):
            continue
        
        triples.append([box1, box2, box3])
    return triples
        

if __name__ == "__main__": 
    boxes = Box.createAllValid()
    print(f"Found {len(boxes)} valid boxes.")
    
    #for box in boxes:
    #   print(box)
        
    with open('all_boxes.txt', 'w+') as outputFile:
        for box in boxes:
            outputFile.write(str(box))
            
    noRepeatDominoes = findNoRepeatDominoes()
    print(f"Found {len(noRepeatDominoes)} dominoes without repeats.")
    
    with open('no_repeat_dominoes.txt', 'w+') as outputFile2:
        for idx, domino in enumerate(noRepeatDominoes):
            outputFile2.write(f"\nNo repeat domino #{idx+1}")
            for box in domino:
                outputFile2.write(str(box))
            
    tripleDominoes = findTripleDominoes()
    print(f"Found {len(tripleDominoes)} triple dominoes!")
    
    with open('triple_dominoes.txt', 'w+') as outputFile3: 
        for idx, domino in enumerate(tripleDominoes):
            outputFile3.write(f"\nTriple domino #{idx+1}")
            for box in domino:
                outputFile3.write(str(box))
            
            

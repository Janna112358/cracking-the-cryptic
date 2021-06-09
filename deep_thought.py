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
            
    tripleDominoes = findTripleDominoes()
    print(f"Found {len(tripleDominoes)} triple dominoes!")
    
    with open('triple_dominoes.txt', 'w+') as outputFile: 
        for idx, domino in enumerate(tripleDominoes):
            outputFile.write(f"\nTriple domino #{idx+1}")
            for box in domino:
                outputFile.write(str(box))
            
            

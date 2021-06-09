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

class Box:
    def __init__(self, topLeft, topRight, bottomLeft, bottomRight):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        
    def __repr__(self):
        return f"\n{self.topLeft} | {self.topRight}\n{self.bottomLeft} | {self.bottomRight}\n"
        

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

if __name__ == "__main__": 
    boxes = Box.createAllValid()
    print(f"Found {len(boxes)} valid boxes.")
    
    #for box in boxes:
    #   print(box)
        
    with open('all_boxes.txt', 'w+') as outputFile:
        for box in boxes:
            outputFile.write(str(box))
            
            

import itertools
import random
import copy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        #If the number of mines is equal to the number of cells, then all cells are mines
        returnVal = set()
        if (self.count == len(self.cells)): 
            for cell in self.cells:
                returnVal.add(cell)
        return returnVal
        raise NotImplementedError

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        #If there are no mines, then all cells are safe
        returnVal = set()
        if (self.count == 0): 
            for cell in self.cells:
                returnVal.add(cell)
        return returnVal
        raise NotImplementedError

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        #Remove mine and reduce count
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1
        return None
        raise NotImplementedError

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        #Remove safe cells
        if cell in self.cells:
            self.cells.remove(cell)
        
        return None
        raise NotImplementedError


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        #Mark the moves and safe cells
        self.mark_safe(cell)
        self.moves_made.add(cell)
        
        #Make a copy of the cells
        addCells = set()
        
        #Find and verify all neighbor cells
        copyCount = copy.deepcopy(count)
        copyCell = copy.deepcopy(cell)
        nextCell = self.nextCells(cell)
        for c in nextCell:
            if c in self.mines:
                copyCount -= 1
            if c not in self.mines and c not in self.safes:
                addCells.add(c)
        
        #Add the sentence to the knowledge
        newSen = Sentence(addCells, copyCount)
        if (len(newSen.cells) > 0):
            self.sentCheck(newSen)
            self.knowledge.append(newSen)
            
        #Check the knowledge and add new inferences
        self.check()
        self.addInferences()
        
    def nextCells(self, cell):
        #Adding and return all neighboring cells
        returnVal = set()
        row, col = cell
        for r in range (self.height):
            for c in range (self.width):
                if (abs(row - r) < 2) and (abs(col - c) < 2) and (not (r, c) == cell):
                    returnVal.add((r, c))
        return returnVal
    
    def sentCheck(self, sentence):
        #Check all sentences for mines and safes
        mine = sentence.known_mines()
        safe = sentence.known_safes()
        for m in mine:
            self.mark_mine(m)
            self.check()
        for s in safe:
            self.mark_safe(s)
            self.check()
        
            
    def addInferences(self):
        #Iterate through the sentences
        for sen1 in self.knowledge:
            self.sentCheck(sen1)
            for sen2 in self.knowledge:
                if (sen1.cells.intersection(sen2.cells) and not(sen1.cells == sen2.cells)):
                    #cannot be equal sentences: find intersection and make new sentence
                    newSent = Sentence(sen2.cells - sen1.cells, abs(sen1.count-sen2.count))
                    if (len(sen1.cells) > len(sen2.cells)):
                        newSent = Sentence(sen1.cells - sen2.cells, abs(sen1.count-sen2.count))
                    #Check new sentence
                    self.sentCheck(newSent)
        
    def check(self):
        #Iterate through knowledge
        copyKnow = copy.deepcopy(self.knowledge)
        #Remove empty sentences, check the reset
        for sen in copyKnow:
            if len(sen.cells) == 0:
                try:
                    self.knowledge.remove(sen)
                except ValueError:
                    pass
            self.sentCheck(sen)
        
    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        #return safe cells that are not prior moves
        for cell in self.safes - self.moves_made:
            print(cell)
            return cell
            
    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        #Maintain track of previously generated coordinates
        checkVal = set()
        while len(checkVal) < self.height*self.width:
            #Generate a random coordinate
            row = random.randrange(self.height)
            col = random.randrange(self.width)
            #Check if coordinate is known to be unsafe or is already a move
            if (row, col) not in checkVal:
                if ((row, col) not in self.mines | self.moves_made):
                    return (row, col)
                checkVal.add((row, col))
        return None

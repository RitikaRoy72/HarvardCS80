"""
Tic Tac Toe Player
"""

import math

from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    x=0
    y=0
    for x in range (0, len(board)):
        for y in range (0, len(board[x])):
            if board[x][y] == X: 
                xCount +=1
            elif board[x][y] == O: 
                oCount += 1
                
    if xCount <= oCount: return X
    return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    returnVal = set()
    for x in range(0, len(board)):
        for y in range (0, len(board[x])):
            if board[x][y] == EMPTY:
                returnVal.add((x, y))
    return returnVal
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    col, row = action
    if col < 0 or row < 0: raise Exception
    new = deepcopy(board)
    
    if new[col][row] != EMPTY: raise Exception 
    new[col][row] = player(board)
    return new
   


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    options = [X, O]
    for play in options:
        for row in board:
            if row == [play] * len(board): return play
            
        for y in range(len(board)):
            column = [board[x][y] for x in range(len(board))]
            if column == [play] * len(board): return play
            
        if [board[y][y] for y in range(0, len(board))] == [play] * len(board): return play
        elif [board[y][~y] for y in range(0, len(board))] == [play] * len(board): return play
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None: 
        return True

    for x in range (0, len(board)):
        for y in range (0, len(board[x])):
            if board[x][y] == EMPTY: return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X: return 1
    elif winner(board) == O: return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        resultBoard, act = max(board)
        return act
    else:
        resultBoard, act = min(board)
        return act
    raise NotImplementedError
    
def max(board):
    move = None
    if terminal(board): return utility(board), move
    
    prevVal = -math.inf
    for act in actions(board):
        curVal, acts = min(result(board, act))
        if curVal > prevVal:
            prevVal = curVal
            move = act
    return prevVal, move
        
    
        
def min(board):
    move = None
    if terminal(board): return utility(board), move
    
    prevVal = math.inf
    for act in actions(board):
        curVal, acts = max(result(board, act))
        if curVal < prevVal:
            prevVal = curVal
            move = act
    return prevVal, move
  
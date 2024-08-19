from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    Or(AKnight, AKnave),
    Biconditional(And(AKnight, AKnave), AKnight)
    
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    #Declare each character as having a state (knight or knave)
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    
    #If AKnight, then both A and B must be knave (contradiction); If A is a Knave, then A's claims are false
    Biconditional(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    #Declare each character as having a state (knight or knave)
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(AKnight, BKnight),
    
    #If A is a knight, then both must be knights; If B is a knight, then they must be different states
    Biconditional(AKnight, And(BKnight, AKnight)),
    Biconditional(BKnight, AKnave)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    #Declare each character as having a state (knight or knave)
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    
    #If A is a knight, then they must be a knight or a knave; If B is a knight, then A must be a knave
    #If A is a knave then they would not declare, therefore, B's lie is A's truth; If C is a knight, then A must be a knight, otherwise they have both lied
    Biconditional(AKnight, Or(AKnight, AKnave)),
    Biconditional(BKnight, AKnave),
    Implication(AKnight, BKnave),
    Biconditional(CKnight, AKnight),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

import nltk
import sys
import copy

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S P S | S Conj S 
NP -> N | Det N | Det AdjP N | N Det | Det AP N | P NP | NP P NP
VP -> V | VP NP | VP PP | VP AdvP | AdvP VP | VP Conj VP | V Det
AdvP -> Adv | Adv AdvP
AdjP -> Adj | Adj AdjP
PP -> P NP | Np P
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    sent = list()
    
    # Iterate through the tokenized sentence 
    for word in nltk.word_tokenize(sentence):
        for letter in word:
            
            # test words if they are a letter, 
            # convert to lower case and append
            if letter.isalpha(): 
                sent.append(word.lower())
                break
    return sent
    
def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Iterate through subtrees ("branches") of tree
    returnlist = []
    for sub in tree.subtrees():
        
        # If a sub tree is a noun phrase iterate through leaves
        # If the leave if a noun phrase, then do not append
        temp = True
        if sub.label() == 'NP':
            for leaf in sub.subtrees():
                if leaf.label() == 'NP' and leaf != sub: temp = False
            if temp:
                returnlist.append(sub)
    return returnlist

    
if __name__ == "__main__":
    main()

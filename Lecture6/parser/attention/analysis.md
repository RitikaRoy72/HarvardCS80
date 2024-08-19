# Analysis
Natural Language Processing is a form of Artificial intelligence designed to understand and replicate human language. The AI system 
extracts information from sentences by explaining language through two lenses: syntax and semantics. In the case of analysis through 
syntax, the AI examines the context-free grammar structure of a sentence. In tokenization, sentences broken into their grammatical 
parts for analysis are used to analyze the sentence's meaning. By contrast, semantic analysis scrutinizes sentences based on the 
meaning of their wordsThe bag-of-words model, where the structure of the sentence is disregarded in place of valuing the meaning of 
the words, enables an AI model to draw meaning from a sentence regardless of its structure. Word meaning analysis is achieved through 
distributed representation, where each word is represented as a list of values, acknowledging each word and its distance to their synonyms 
via word2vec. However, conventional bag-of-words models, much like tokenization, fail to account for the relevance of each word in a 
sentence. Attention allows for some words in a sentence to be ranked by important to the meaning of the sentence than others. These 
algorithms combined, are implemented through Transformer training: each input, its attention, and its position are passed into the neural 
network simultaneously account for the results of each proceeding word passed into the same algorithm. This method ensures that text is 
processed quickly without compromising syntax or semantics. 

The (get_mask_token_index) function is designed to identify the position of a token within a sentence. This function returns the position 
of the [MASK] token in the transformers.BatchEncoding input so it can be passed to the into the mode. The (get_color_for_attention_score) 
function is a step in the generation of the attention visualization diagram which visually represents the importance of each word as a color 
on the white-to-black scale in RGB values. This step is completed in the (vizualize_attentions) function which iterates through the different 
layers and attention heads to generate a diagram representing the importance of one word to the next.


## Layer 1, Head 4

Layer 1 Attention head 4 diagram represents connections between each word and the word before it. The middle diagonal connects a word to 
its proceeding word (ie I (vertical) is connected to saw (horizontal) in the first sentence). The words with the lightest cells were shared 
between (i and saw) and (the and forest) indicating that the relation between these words played a pivotal role in the meaning of the sentence- 
the nouns and verbs in the sentence indicate the most important parts connecting the accounts to the meaning of the sentence. 

Example Sentences:
- I saw a [MASK] in the forest.
Predicted words: shadow, light, figure

- I drank water from a [MASK].
Predicted words: bottle, canteen, jug

- The sky is made of [MASK].
Predicted words: glass, clouds, stars

- I had [MASk] for dinner.
Predicted words: plans, enough, time

## Layer 10, Head 10

Layer 10 Attention head 10 diagrams represent the connection between all words (vertical) and the end token of the sentence. This layer 
connects words to the SEP token while other values are largely ignored in this layer. There are small amounts of noise connecting the middle 
parts of the sentences (ie the action verb and subject) however, the majority of words' relation to each other is ignored. This part of the 
analysis focuses on each word's connection to the end of the sentence as opposed to among each other. 

Example Sentences:
- I saw a [MASK] in the forest.
Predicted words: shadow, light, figure

- I drank water from a [MASK].
Predicted words: bottle, canteen, jug

- The sky is made of [MASK].
Predicted words: glass, clouds, stars

- I had [MASk] for dinner.
Predicted words: plans, enough, time
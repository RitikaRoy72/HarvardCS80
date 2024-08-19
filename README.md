# HarvardCS80
Summer of 2024- Harvard Extension School Introduction to AI with Python (CS 80 Course) by Professor Brian Yu

# Lecture 0: Search
Graph Theory concerns itself with search algorithms. Given an initiate state and a final state,
AI can implement many algorithms to satisfy constraints and ensure the connection of the two 
states. The agent is an entity that perceives the environment, while a state is a configuration 
of an agent- the node of the current state and connections to prior states. The key to 
optimizing the path cost is the balance minimization of the states traversed and attaining the 
optimal solution. Topics explored in this unit include:
* Breadth-first search
* Depth-first search
* Greedy Best-First search
* A* Search
* Adversarial Search
* Minimax
* Alpha-Beta Pruning
* Depth-Limited Minimax

# Lecture 1: Knowledge
Knowledge and logic are fundamental aspects of human intuition and deduction. Knowledge 
specifically concerns itself with finding a solution based on existing rules and information. 
Different logical connectives can be used to indicate the relation of one assertion to another.
This form of propositional logic can be used to deduct a conclusion from a series of 
statements. Topics explored in this unit include:
* First Order Logic
* Propositional Logic
* Entailment
* Inference
* Model Checking
* Resolution

# Lecture 2: Uncertainty
While knowledge is the key to inductive reasoning, AI has a limited amount of information about 
the world in which it must operate. This deficit of absolute information leaves space for 
uncertainty. Simply defined, uncertainty is the room for error when connecting an input to a 
given output. For AI to make the best possible decision, AI has to compute the best possible 
decision on limited information: the core of probability. Topics explored in this unit include:
* Probability
* Conditional Probability
* Random Variables
* Independence
* Bayes' Rule
* Joint Probability
* Bayesian Networks
* Sampling
* Markov Models
* Hidden Markov Models

# Lecture 3: Optimization
The architecture of a solution is not merely a connection from the initial to the final state
but rather the iterative process of improving both the journey to finding the solution and the
accuracy of the solution itself. Methods that optimize the training time and vitality of an AI 
are referred to as Optimization. The heart of optimization in AI is re-doing a process in a 
different direction to test for accuracy. In the case of a local search, this new direction 
starts with testing different neighboring nodes until the optimal node is found: this lends 
way to hill-climbing algorithms. The pitfall of this method is the chance of being caught in a 
local, not absolute, minimum error. Other forms of optimization include backtracking- moving 
from outputs to inputs, to determine the best solution and more. Topics explored in this unit 
include:
* Local Search
* Hill Climbing
* Simulated Annealing
* Linear Programming
* Constraint Satisfaction
* Backtracking Search

# Lecture 4: Learning
Many AI models are built on the premise of pattern recognition- identifying commonalities in 
inputs to associate with an output. This method of learning closely replicates human learning 
and pattern recognition abilities. The two major forms of learning are supervised and 
unsupervised learning. The heart of supervised learning is the mapping of discrete inputs onto
discrete outputs. This can take shape in many problem types (classification, regression, and 
the like). In supervised learning, it is critical to prevent the data from over-fitting or 
fine-tuning the algorithm to the point of unrecognition of new data. Often, favoring a less 
accurate general model (regularization) can yield a more beneficial solution than the reverse.
By contrast, unsupervised learning is the mapping of patterns onto data. This does not look 
for a discrete output to map data onto, but rather the identification of the patterns within 
the data. Topics explored in this unit include:
* Supervised learning
* Nearest-Neighbor Classification
* Perception Learning
* Support Vector Machines
* Regression
* Loss Functions
* Overfitting
* Regularization
* Reinforcement Learning
* Markov Decision Processes
* Q-Learning
* Unsupervised Learning
* k-means Clustering

# Lecture 5: Neural Networks
The architecture of the neural network is largely inspired by the mechanics of the human 
brain. The different neurons in a neural network send signals to and fro, much as the neurons 
in the human brain. The mathematical representation of AI as a neural network is determined by 
the training data and parameters of the network itself. The neural network follows a 
polynomial-like format (h(x1, x2, x3, ..., xn) = w0 + w1*x1 + w2*x2 + w3*x3 + ... + wn*xn). In 
this instance, (x) represents the inputs while (w) represents the weights of the neural 
network. However, (w0) specifically represents the bias in the neural network. The weights of 
the neural network are determined by activation functions (ie reLu, sigmoid, softmax, etc), 
indicating the connective of one input or neuron to the next. Optimization of the output 
employs methods such as Stochastic and Gradient descent and backpropagation. Applications of 
convolution neural networks span from language processing to computer vision. Topics explored
in this unit include:
* Artificial Neural Networks
* Activation Functions
* Gradient Descent
* Backpropagation
* Overfitting
* Tensorflow
* Image Convolution
* Convolutional Neural Networks
* Recurrent Neural Networks

# Lecture 6: Language
Natural Language processing encompasses a variety of tasks involving AI's work with human 
languages. The basics of language understanding encompass both syntax - the grammar of the 
language- and semantics - the meaning of the words. Examination of language through either 
lens yields meaning to the sentence. However, the combined examination of language through 
both lenses gives a more complete impact on a sentence. AI achieves this by the representation
of words as lists of numbers via word2vec models. This achieves semantic representation by 
associating words with similar words. Using the algorithms of attention, AI can assign 
importance to different words in a sentence, helping understand and respond to sentences via a 
mathematical understanding of language. Topics explored include:
* Syntax
* Semantics
* Context-Free-Grammar
* nltk
* n-grams
* Bag-of-Words Model
* Naive Bayes
* Word Representation
* word2vec
* Attention
* Transformers

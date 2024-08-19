# -*- coding: utf-8 -*
"""
Created on Sat Aug  3 12:38:57 2024

@author: Ritika
"""

** Documentation for methods **
# Load Data 
Try-Catch loop
Loops to access all images in a folder via os.listdir
Load data uses cv2.imread to load all images and labels into a tuple
Use cv2.resize to meet specifications for IMG_HEIGHT, IMG_WIDTH

# Get model
Implement a sequential model using the Keras package
The first convolution layer has shapes (28, 28, 32) with sigmoid activation
The pooling layer converts to a (14, 14, 32 0) shape
The second convolution layer has shape (6, 6, 32) with relu activation
Pooling layer converts it to 6, 6, 32
Dense layer converts the third parameter to 64, the kernel is set to a uniform
Layers are flattened (2304) size
Dense layer with 900 units and relu activation
Dropout of 0.4
Dense layer with 300 units and softmax activation
Model compiled with Adam optimization, categorial cross-entropy loss, and accuracy metrics


** Committed Changes **
## Load Data 
Started with an id statement to check for “DS_Start”, 
changed to try a loop 


# get model 
started with default test_size as 0.5 (Accuracy 0.93)
increased epochs to 15 (Accuracy 0.93)
changed default test_size to 0.8 (Accuracy 0.05) reverted change
decreased drop out to 0.2 (Accuracy 0.8201)
changed the second activation of the dense layer to relu (Accuracy 0.0053)
changed the first activation of the dense layer to sigmoid (Accuracy 0.0041) 
removed the first dense layer, moved layer dropout after the second dense layer (Accuracy 0.00048)
added 3 dense layers with relu activation (Accuracy 0.0062)
changed units in layer one NUM_CATEGORIES square, 
changed the second layer from dense to sigmoid, 
changed third layer dense to softmax (Accuracy 0.0565)
added dropout 0.5 after sigmoid activation (Accuracy 0.041)
changed first dense to softmax, second dense layer to relu (Accuracy 0.0986)
removed second dense layer (accuracy:0.0569)
changed first dense layer to sigmoid (Accuracy 0.9758)
learning rate changed to 0.1 (Accuracy 0.051) revert
changed test_size to 0.6 (Accuracy 0.9677)
changed drop out to 0.6 (Accuracy 0.9695)
added another convolution layer relu activation
added pooling layer (Accuracy 0.9022)
changed kernel to uniform, (Accuracy 0.9273)
removed the first pooling layer (accuracy is 0.9678)
reduced drop out to 0.5 (Accuracy 0.9661) revert
changed line 133 to softmax (accuracy 0.0518) revert
final run accuracy: 0.9810

** Learned Lessons **
An image classification neural network is a form of machine learning designed to classify images by category.
The CNN works with the different RGB values in a tuple; this creates a 3D shape. The data, organized by type 
and stored in a tuple with an image and label, is randomly assigned to a training and testing set.  Different 
layers in the CNN process the training data set. The convolutional layer applies filters to obscure the finer 
features of an image- thus, making it more suited for classification purposes. The flattening layer converted 
the three-dimensional RGB value to a two-dimensional figure. In the hidden layers, a function is formed via the 
weights, biases, and inputs. The result of the function determines the degree of correctness of an input based 
on the activation function. Gradient descent is a form of optimization of the neural network: the CNN adjusts 
the weights and biases to return more accuracy by minimizing the error. Randomly reiterating this process via an 
epoch improves the accuracy of prediction. Backpropagation is a method of connecting the output to the input in 
the neural network to adjust the weights and improve accuracy. Dropout is a form of reducing the reliance on 
certain nodes by removing them from the network. This helps the CNN predict a new data point by preventing 
overfitting to the given training dataset. Altering the type and usage of these aspects of a neural network can 
be met with varying success in prediction. Optimum accuracy is not a single solution but rather a set of solutions 
that meet a certain the creation of the programmer (ie a CNN that compiles most quickly, a CNN with the least loss, etc.)

Of the different facets of a cnn, dropout, layers, convolution, etc, some aspects have a more significant impact 
on a given data set than others.The first elements of the CNN adjusted were the activation functions in the dese 
layer. Each data set has an activation function that is best suited for it; the given GTSRB data set has the most 
accuracy with the softmax activation function implemented. In the case of the GTSRB dataset, the program requires a 
scale of correctness which relu and Softmax provide. Other activation functions such as step activation, provide a 
boolean output unsuited for this problem. Adding units to a dense layer impacts the resulting accuracy of the CNN by 
increasing the complexity of the CNN. However, adding units does not always improve the accuracy of the CNN. Excessive 
units are often weighted less, slow the training process, and do little for the accuracy of a CNN. Similarly, adding 
layers to a CNN makes a CNN increases the complexity of the CNN, often making it better suited to identify more features 
in an image. However, the excessive addition of layers does not necessarily improve accuracy. Changing the amount of 
convolution and pooling layers impacts the accuracy of a CNN. Adding more layers to remove finer features of an image, 
leaving only more pronounced and common features, helps the CNN identify images more accurately outside the dataset. While 
this does not lend higher training accuracy, it improves the accuracy of the CNN when it is given the testing dataset.


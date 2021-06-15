![](https://img.shields.io/github/followers/mandarmakhi?label=Follow%40mandarmakhi&style=social)
![](https://img.shields.io/github/forks/mandarmakhi/Machine-learning-With-Python-?label=Fork&style=social)
![](https://img.shields.io/github/stars/mandarmakhiMachine-learning-With-Python-?style=social)
![](https://img.shields.io/github/watchers/mandarmakhi/Machine-learning-With-Python-?style=social)
![](https://img.shields.io/github/issues/mandarmakhi/Machine-learning-With-Python-)
![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://mandarmakhi.github.io/Machine-learning-With-Python-/)]
![](https://img.shields.io/github/repo-size/mandarmakhi/Machine-learning-With-Python-)
![](https://img.shields.io/github/languages/code-size/mandarmakhi/Machine-learning-With-Python-)


# Machine-learning-With-Python-


Machine learning is the branch of artificial intelligence (AI) focused on building applications that learn from data and improve their accuracy over time without being programmed to do so. 

In data science, the algorithm is a sequence of statistical processing steps. In machine learning, algorithms are 'trained' to find patterns and features in massive amounts of data to make decisions and predictions based on new data. The better algorithm is a more accurate decision and prediction will become as it processes more data.

Examples of machine learning are all around us. Search the web and play music in response to our voice commands like digital assistants (ex: Alexa, Bixby, Google Assistant). Websites recommend products and movies and songs based on what we bought, watched or listened to before. Robots vacuum our floors while we do something better with our time. Spam detectors stop unwanted emails from reaching our inboxes. Medical image analysis systems help doctors spot tumors they might have missed. And the first self-driving cars are hitting the road.

We can expect more. As big data keep getting bigger as computing becomes more powerful & affordable as data scientists keep developing more capable algorithms, machine learning will drive greater efficiency in our personal and work lives.


***
You will Need Anaconda to Execute all the Codes So Install it first and then Go through the Below Codes.
To Download anaconda, [Click Here](https://www.anaconda.com/products/individual).

Then after installation of anaconda open anaconda navigator and install the jupyter notebook inside the anaconda environment then execute the .ipynb code inside the jupyter notebook.

Use this link to download repo or code, [Click Here](https://www.anaconda.com/products/individual).
***

## Types of Machine Learning Algorithms You Should Know

I particularly think that getting to know the types of Machine learning algorithms is like getting to see the Big Picture of AI and what is the goal of all the things that are being done in the field and put you in a better position to break down a real problem and design a machine learning system.
Terms frequently used in this post:

•	Labeled data: Data consisting of a set of training examples, where each example is a pair consisting of an input and a desired output value (also called the supervisory signal, labels, etc)

•	Classification: The goal is to predict discrete values, e.g. {1,0}, {True, False}, {spam, not spam}.

•	Regression: The goal is to predict continuous values, e.g. home prices.

## Types of machine learning Algorithms

There some variations of how to define the types of Machine Learning Algorithms but commonly they can be divided into categories according to their purpose and the main categories are the following:

•	Supervised learning

•	Unsupervised Learning

•	Semi-supervised Learning

•	Reinforcement Learning

***
# Supervised learning

•	Nearest Neighbor

•	Naive Bayes

•	Decision Trees

•	Linear Regression

•	Support Vector Machines (SVM)

•	Neural Networks




# Unsupervised Learning

•	k-means clustering, Association Rules


# Semi-supervised Learning

Semi-supervised learning offers a happy medium between supervised and unsupervised learning. During training, it uses a smaller labeled data set to guide classification and feature extraction from a larger, unlabeled data set. Semi-supervised learning can solve the problem of having not enough labeled data (or not being able to afford to label enough data) to train a supervised learning algorithm. 


# Reinforcement Learning

•	Q-Learning

•	Temporal Difference (TD)

•	Deep Adversarial Networks


***

# How machine learning works

There are four basic steps for building a machine learning application (or model). These are typically performed by data scientists working closely with the business professionals for whom the model is being developed.

Step 1: Select and prepare a training data set
Training data is a data set representative of the data the machine learning model will ingest to solve the problem it’s designed to solve. In some cases, the training data is labeled data—‘tagged’ to call out features and classifications the model will need to identify. Other data is unlabeled, and the model will need to extract those features and assign classifications on its own.

In either case, the training data needs to be properly prepared—randomized, de-duped, and checked for imbalances or biases that could impact the training. It should also be divided into two subsets: the training subset, which will be used to train the application, and the evaluation subset, used to test and refine it.

Step 2: Choose an algorithm to run on the training data set
Again, an algorithm is a set of statistical processing steps. The type of algorithm depends on the type (labeled or unlabeled) and amount of data in the training data set and on the type of problem to be solved.


Common types of machine learning algorithms for use with labeled data include the following:

## Regression algorithms:

Linear and logistic regression are examples of regression algorithms used to understand relationships in data. Linear regression is used to predict the value of a dependent variable based on the value of an independent variable. Logistic regression can be used when the dependent variable is binary in nature: A or B. For example, a linear regression algorithm could be trained to predict a salesperson’s annual sales (the dependent variable) based on its relationship to the salesperson’s education or years of experience (the independent variables.) Another type of regression algorithm called a support vector machine is useful when dependent variables are more difficult to classify.
## Decision trees:

Decision trees use classified data to make recommendations based on a set of decision rules. For example, a decision tree that recommends betting on a particular horse to win, place, or show could use data about the horse (e.g., age, winning percentage, pedigree) and apply rules to those factors to recommend an action or decision.

## Instance-based algorithms: 

A good example of an instance-based algorithm is K-Nearest Neighbor or k-nn. It uses classification to estimate how likely a data point is to be a member of one group or another based on its proximity to other data points.
Algorithms for use with unlabeled data include the following:

## Clustering algorithms: 

Think of clusters as groups. Clustering focuses on identifying groups of similar records and labeling the records according to the group to which they belong. This is done without prior knowledge about the groups and their characteristics. Types of clustering algorithms include the K-means, TwoStep, and Kohonen clustering.
Association algorithms: Association algorithms find patterns and relationships in data and identify frequent ‘if-then’ relationships called association rules. These are similar to the rules used in data mining.
Neural networks: A neural network is an algorithm that defines a layered network of calculations featuring an input layer, where data is ingested; at least one hidden layer, where calculations are performed make different conclusions about input; and an output layer. where each conclusion is assigned a probability. A deep neural network defines a network with multiple hidden layers, each of which successively refines the results of the previous layer. (For more, see the “Deep learning” section below.)

## Step 3: Training the algorithm to create the model

Training the algorithm is an iterative process–it involves running variables through the algorithm, comparing the output with the results it should have produced, adjusting weights and biases within the algorithm that might yield a more accurate result, and running the variables again until the algorithm returns the correct result most of the time. The resulting trained, accurate algorithm is the machine learning model—an important distinction to note, because 'algorithm' and 'model' are incorrectly used interchangeably, even by machine learning mavens.

## Step 4: Using and improving the model 

The final step is to use the model with new data and, in the best case, for it to improve in accuracy and effectiveness over time. Where the new data comes from will depend on the problem being solved. For example, a machine learning model designed to identify spam will ingest email messages, whereas a machine learning model that drives a robot vacuum cleaner will ingest data resulting from real-world interaction with moved furniture or new objects in the room.

***

# Deep learning

Deep learning is a subset of machine learning (all deep learning is machine learning, but not all machine learning is deep learning). Deep learning algorithms define an artificial neural network that is designed to learn the way the human brain learns. Deep learning models require large amounts of data that pass through multiple layers of calculations, applying weights and biases in each successive layer to continually adjust and improve the outcomes.

Deep learning models are typically unsupervised or semi-supervised. Reinforcement learning models can also be deep learning models. Certain types of deep learning models—including convolutional neural networks (CNNs) and recurrent neural networks (RNNs)—are driving progress in areas such as computer vision, natural language processing (including speech recognition), and self-driving cars. 

***

# Real-world machine learning use cases

As noted at the outset, machine learning is everywhere. Here are just a few examples of machine learning you might encounter every day:

Digital assistants: Apple Siri, Amazon Alexa, Google Assistant, and other digital assistants are powered by natural language processing (NLP), a machine learning application that enables computers to process text and voice data and 'understand' human language the way people do. Natural language processing also drives voice-driven applications like GPS and speech recognition (speech-to-text) software.

Recommendations: Deep learning models drive 'people also liked' and 'just for you' recommendations offered by Amazon, Netflix, Spotify, and other retail, entertainment, travel, job search, and news services.

Contextual online advertising: Machine learning and deep learning models can evaluate the content of a web page—not only the topic, but nuances like the author's opinion or attitude—and serve up advertisements tailored to the visitor's interests.

Chatbots: Chatbots can use a combination of pattern recognition, natural language processing, and deep neural networks to interpret input text and provide suitable responses.
Fraud detection: Machine learning regression and classification models have replaced rules-based fraud detection systems, which have a high number of false positives when flagging stolen credit card use and are rarely successful at detecting criminal use of stolen or compromised financial data.

Cybersecurity: Machine learning can extract intelligence from incident reports, alerts, blog posts, and more to identify potential threats, advise security analysts, and accelerate response.

Medical image analysis: The types and volume of digital medical imaging data have exploded, leading to more available information for supporting diagnoses but also more opportunity for human error in reading the data. Convolutional neural networks (CNNs), recurrent neural networks (RNNs), and other deep learning models have proven increasingly successful at extracting features and information from medical images to help support accurate diagnoses.

Self-driving cars: Self-driving cars require a machine learning tour de force—they must continuously identify objects in the environment around the car, predict how they will change or move, and guide the car around the objects as well as toward the driver's destination. Virtually every form of machine learning and deep learning algorithm mentioned above plays some role in enabling a self-driving automobile.

***
***
***

## 1.	 Searching Algorithms

•	Linear Search

•	Binary Search

•	Depth First Search

•	Breadth First Search

•	Jump Search

## 2.	Sorting Algorithms

•	Bubble Sort

•	Merge Sort

•	Selection Sort

•	Heap Sort

•	Insertion Sort

•	Radix Sort

•	Quick Sort

•	Tim Sort

## 3.	Greedy Algorithms

•	Huffman Coding

•	Fractional Knapsack Problem

•	Activity Selection

•	Job Sequencing Problem

## 4.	Dynamic Programming

•	Fibonacci Number Series

•	Knapsack Problem

•	Tower of Hanoi

•	Shortest Path by Dijkstra

•	Matrix Chain Multiplication

## 5.	Recursive Programming

•	Factorial 

•	Exponential 

•	Tower of Hanoi

•	Tree Traversal

•	DFS Of Graph



# Requirement
﻿The dependencies for running the project are:
* Numpy (version==1.21.0)
* Matplotlib.pyplot (version = 3.4.2)
* Networkx (version == 2.5)
* Osmnx (version==1.1.1)


We have used Anaconda to install these dependencies:
1. Anaconda can be downloaded from : (Installing on Windows — Anaconda documentation)
2. conda config --prepend channels conda-forge
3. conda create -n ox --strict-channel-priority osmnx 
4. conda install numpy 
5. conda install -c conda-forge networkx=2.5
6. conda install -c conda-forge matplotlib 


After running the above commands in terminal a new environment name ox is created.
We install all the other libraries in this environment.

# optimal-path-Qlearning
The objective of this project is to find optimal path between any two nodes.
To achieve an optimal path in our project we used **Q- learning**, a model-free
reinforcement learning algorithm, aimed to learn the quality of actions and telling an
agent what action is to be taken under which circumstance. It does not require a model
of the environment (hence "model-free"), and it can handle problems with stochastic
transitions and rewards without requiring adaptations.

# visual representaion of nodes and location
Using the networkx library we designed the nodes and **matplotlib**.
**pyplot** is used to plot the nodes and edges
![map](map.png)

Suppose we want to find optimal path between *L1* and *L7*.
The output is ['L1', 'L6', 'L16', 'L3', 'L2'] which is shown in the figure below:
![optimal_path](optimal_path.png)

# Extracting Nodes from openstreet map using OSMnx
We tried to take the real location of
Kathmandu, Ratnapark area and find the optimal nodes on it. We extracted
nodes of this area from openstreet map. On applying the Q-learning algorithm,
we could easily find the optimal path over a small distance but for the nodes
that were farther it had to use over 10,000 iterations and it took lots of time to
compute the optimal path. Deducing this was not efficient we went with the
dummy location. This could be a great future enhancement in this project.


import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# define the locations
fileOpen = open("nodes.txt", "r")
location = fileOpen.read().splitlines()
fileOpen.close()
print(location)

# mapping into a graph
G = nx.read_edgelist("edges_of_nodes.txt", create_using=nx.Graph(), nodetype=str)
pos = nx.spring_layout(G, seed=3000)
# nodes
options = {"node_size": 500, "alpha": 0.8}
nx.draw_networkx_nodes(G, pos, node_color="g", **options)
# edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos, width=4, alpha=0.5, edge_color="b")
nx.draw_networkx_labels(G, pos)
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.savefig('map.png')  # save graph in png file
plt.show()

# define locations to state
location_to_state = dict(zip(location, range(len(location))))
print(location_to_state)

# rewards
rewards = nx.to_numpy_matrix(G, nodelist=location)
print("The reward matrix is: ", rewards)

# Maps indices to locations
state_to_location = dict((state, location) for location, state in location_to_state.items())
print(state_to_location)

# Initialize parameters
gamma = 0.75  # discount factor 
alpha = 0.9  # learning rate


def optimal_route(start_node, end_node):
    # Copy the rewards matrix to new Matrix
    rewards_copy = np.copy(rewards)

    # Get the ending state corresponding to the ending node
    ending_state = location_to_state[end_node]

    # With the above information automatically set the priority of the
    # given ending state to the highest one
    rewards_copy[ending_state, ending_state] = 999

    # Initializing Q-values
    Q = np.array(np.zeros([len(location), len(location)]))
    # print("The initial Q matrix:", Q)

    for i in range(1000):       # iteration depends on number of nodes
        # pick up a state randomly
        current_state = np.random.randint(0, len(location))

        possible_actions = []
        for j in range(len(location)):  # appends array till the number of locations
            if rewards_copy[current_state, j] > 0:
                possible_actions.append(j)

        # pick an action randomly from the list of playable actions
        # leading us to the next state
        next_state = np.random.choice(possible_actions)

        # compute temporal difference
        # The action here exactly refers to going to the next state
        TD = rewards_copy[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state,])] - Q[
            current_state, next_state]

        # Update the Q-value using the Bellman equation
        Q[current_state, next_state] += alpha * TD
        print("The Q-values are:", Q)

    path = [start_node]
    next_location = start_node

    while next_location != end_node:
        starting_state = location_to_state[start_node]

        # Fetch the highest Q-value pertaining to starting state
        next_state = np.argmax(Q[starting_state,])

        # We got the index of the next state. But we need the corresponding letter.
        next_location = state_to_location[next_state]
        path.append(next_location)

        # Update the starting location for the next iteration
        start_node = next_location

    return path


begin = input("The location you want to start:")
end = input("The location you want to go:")

route = optimal_route(begin, end)
print("The optimal path is: ", route)

# mapping optimal path into a graph

H = nx.Graph()
I = nx.path_graph(route)
H.add_nodes_from(I)
H.add_edges_from(I.edges)
H.edges()
optimal_edges = H.edges()


# combining original map and optimal path map
F = nx.compose(G, H)
G.nodes(data=True)
H.nodes(data=True)
F.nodes(data=True)

pos = nx.spring_layout(F, seed=3000)
options = {"node_size": 500, "alpha": 0.8}

# nodes
nx.draw_networkx_nodes(F, pos, nodelist=location, node_color="g", **options)
nx.draw_networkx_nodes(F, pos, nodelist=route, node_color="tab:red", **options)

# edges
nx.draw_networkx_edges(F, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(F, pos, width=4, alpha=0.5, edge_color="b")
nx.draw_networkx_edges(F, pos, width=4, edgelist=optimal_edges, alpha=0.5, edge_color="tab:red")
nx.draw_networkx_labels(F, pos)
ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.savefig('optimal_path.png')
plt.show()

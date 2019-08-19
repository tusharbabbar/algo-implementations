""" Reccursive(TopDown) solution for finding optimal binary search tree.
    Problem: Given list of numbers provide the optimal binary search tree.
    Input: list of ascending sorted nodes with number of searches
"""

class Node():
    def __init__(self, value, searches):
        self.value = value
        self.searches = searches

    def __repr__(self):
        return '(%s, %s)' % (self.value, self.searches)

def obs(nodes):
    """ nodes: list of instances of Node
    returns: Optimal Number of searches, List of nodes of binary search tree in order of insertion to tree
    """
    if len(nodes) == 0:
        return 0, nodes

    if len(nodes) == 1:
        return nodes[0].searches, nodes

    options = []
    for idx, root in enumerate(nodes):
        left_obs = obs(nodes[0:idx])
        right_obs = obs(nodes[idx+1:])
        options.append((root, (left_obs[0] + right_obs[0], left_obs[1] + right_obs[1])))
    optimal_option = min(options, key=lambda x: x[1][0])
    val = sum([node.searches for node in nodes]) + optimal_option[1][0], [optimal_option[0]] + optimal_option[1][1]
    return val


if __name__ == "__main__":
    inputs = [(10,4), (12, 2), (13, 9), (16,6), (21,3)]
    nodes = [Node(i[0], i[1]) for i in inputs]
    print (obs(nodes))


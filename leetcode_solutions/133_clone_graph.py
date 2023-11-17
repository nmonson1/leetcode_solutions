"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node ==None: return None
        adj = {}
        seen_list={node}
        if node.neighbors == None: return Node(1)
        adj[1] = [i.val for i in node.neighbors]
        seen_list.update(node.neighbors)
        visited_list = {node}
        new_nodes = {}
        new_nodes[1] = Node(1)
        while visited_list < seen_list:
            next_node = (seen_list-visited_list).pop()
            adj[next_node.val] = [i.val for i in next_node.neighbors]
            seen_list.update(next_node.neighbors)
            visited_list.add(next_node)
            new_nodes[next_node.val] = Node(next_node.val)
        for n, val in adj.items():
            new_nodes[n].neighbors = [new_nodes[i] for i in val]
        return new_nodes[1]

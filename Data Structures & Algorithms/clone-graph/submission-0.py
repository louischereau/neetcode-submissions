"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def dfs(self, node: Optional['Node'], visited_nodes: Dict) -> Optional['Node']:
        if not node:
            return None

        if not node.neighbors and not visited_nodes.get(node):
            node_copy = Node(node.val, [])
            visited_nodes[node] = node_copy
            return node_copy

        neighbors_copy = []

        node_copy = Node(node.val, [])
        visited_nodes[node] = node_copy

        for neighbor in node.neighbors:
            if not visited_nodes.get(neighbor):
                neighbor_copy = self.dfs(neighbor, visited_nodes)
            else:
                neighbor_copy = visited_nodes[neighbor]

            neighbors_copy.append(neighbor_copy)

        node_copy.neighbors = neighbors_copy
        
        return node_copy

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node, {})
        

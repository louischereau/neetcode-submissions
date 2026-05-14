from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n <= 2:
            return [i for i in range(n)]

        adj = {k: [] for k in range(n)}

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        leaf_nodes = deque([node for node, neigh in adj.items() if len(neigh) == 1])

        remaining_nodes = n

        while remaining_nodes > 2:
            leaf_count = len(leaf_nodes)
            remaining_nodes -= leaf_count
            for _ in range(leaf_count):
                leaf = leaf_nodes.popleft()
                # Only neighbir of leaf
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    leaf_nodes.append(neighbor)

        return list(leaf_nodes)



        






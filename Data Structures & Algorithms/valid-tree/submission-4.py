from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        stack = [(0, -1)]  # (current node, parent node)
        visited = set()

        for parent, child in edges:
            graph[parent].append(child) 
            graph[child].append(parent) # Undirected: add both directions

        while stack:
            node, parent = stack.pop()
            visited.add(node)
            for child in graph[node]:
                if child == parent: continue   # Don't go back the way we came
                if child in visited: return False # Real cycle detected
                stack.append((child, node))

        return len(visited) == n

        
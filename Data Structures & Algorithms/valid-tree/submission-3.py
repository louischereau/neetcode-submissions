from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        stack = [(0, -1)]
        visited = set()

        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)

        while stack:
            node, parent = stack.pop()
            visited.add(node)
            for child in graph[node]:
                if child == parent: continue
                if child in visited: return False
                stack.append((child, node))

        return len(visited) == n

        
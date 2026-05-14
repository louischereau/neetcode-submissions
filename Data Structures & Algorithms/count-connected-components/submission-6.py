from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        connected_components = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent=None):
            if node in visited:
                return True

            visited.add(node)

            for child in graph[node]:
                if child != parent and child not in visited:
                    dfs(child, node)
            
            return False


        for node in range(n):
            visited_tree = dfs(node)
            if not visited_tree:
                connected_components += 1


        return connected_components
        




        
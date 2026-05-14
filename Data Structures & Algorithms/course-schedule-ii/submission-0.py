from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)

        state = [0] * numCourses

        result = []
        
        def dfs(course):
            if state[course] == 1: 
                return False
            if state[course] == 2: 
                return True

            state[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            state[course] = 2
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return result
        

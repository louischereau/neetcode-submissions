from collections import deque, defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Collect all unique characters and initialize data structures
        chars = set(char for word in words for char in word)
        graph = defaultdict(list)
        indegree = {c: 0 for c in chars}
        
        # Step 2: Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            found_diff = False
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    # w1[j] comes before w2[j]
                    graph[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    found_diff = True
                    break
            
            # Edge case: If w1 is longer than w2 and w2 is a prefix of w1 (e.g., "abc", "ab")
            if not found_diff and len(w1) > len(w2):
                return ""

        queue = deque([char for char in chars if indegree[char] == 0])

        order = []

        while queue:
            char = queue.popleft()

            order.append(char)

            for next_char in graph[char]:
                indegree[next_char] -=1
                if indegree[next_char] == 0:
                    queue.append(next_char)

        # Step 4: Check if all characters were processed (detects cycles)
        if len(order) != len(chars):
            return ""
            
        return "".join(order)

            



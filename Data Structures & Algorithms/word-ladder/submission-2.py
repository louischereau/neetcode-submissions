from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(set)

        words = [beginWord, endWord] + wordList

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if sum(c1 != c2 for c1, c2 in zip(words[i], words[j])) == 1:
                    graph[words[i]].add(words[j])
                    graph[words[j]].add(words[i])

        
        queue = deque([beginWord])

        count = 1

        visited = set([beginWord])

        while queue:

            for _ in range(len(queue)):
            
                word = queue.popleft()

                if word == endWord:
                    return count

                for other_word in graph[word]:
                    if other_word not in visited:
                        queue.append(other_word)
                        visited.add(other_word)

            count += 1


        return 0
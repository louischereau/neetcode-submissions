from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        hashmap = defaultdict(list)
        for word in strs:
            anagram = "".join(sorted(word))
            hashmap[anagram].append(word)
        return list(hashmap.values())

        
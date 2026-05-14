class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        anagrams = set(["".join(sorted(word)) for word in strs])
        hashmap = dict([(anagram, []) for anagram in anagrams])
        for word in strs:
            anagram = "".join(sorted(word))
            hashmap[anagram].append(word)
        return list(hashmap.values())

        
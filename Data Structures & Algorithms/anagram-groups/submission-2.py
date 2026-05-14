from collections import defaultdict

class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     if not strs:
    #         return []
    #     hashmap = defaultdict(list)
    #     for word in strs:
    #         anagram = "".join(sorted(word))
    #         hashmap[anagram].append(word)
    #     return list(hashmap.values())

    # Better performance: Use character frequency instead of sorted strings
    # to group anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use defaultdict to group words by their frequency key
        ans = defaultdict(list)
        
        for s in strs:
            # Create a list of 26 zeros (one for each lowercase English letter)
            count = [0] * 26
            
            for char in s:
                # ord() gets the ASCII value. subtracting ord('a') maps 'a'->0, 'b'->1, etc.
                count[ord(char) - ord('a')] += 1
            
            # Convert the list to a tuple because lists are not hashable (cannot be dict keys)
            ans[tuple(count)].append(s)
            
        return list(ans.values())

        
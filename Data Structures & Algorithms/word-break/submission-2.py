class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        # 1. Convert wordDict to a Set for O(1) lookups (High performance!)
        word_set = set(wordDict)
        
        def dp(start: int) -> bool:

            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set and dp(end): 
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False


            


        return dp(0)


        
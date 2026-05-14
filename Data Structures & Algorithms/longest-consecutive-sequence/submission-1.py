class Solution:
    def indexExists(self, hash_table, index) -> bool:
        try:
            hash_table[index]
            return True
        except:
            return False

    def longestConsecutive(self, nums: List[int]) -> int:
        hash_table = dict()
        max_length = 0
        for num in nums:
            hash_table[num] = 0
        for num in hash_table.keys():
            try:
                hash_table[num-1]
            except:
                hash_table[num] = 1
                continue
        for num in hash_table.keys():
            if hash_table[num]:
                length = 0
                index = num
                while self.indexExists(hash_table, index):
                    length +=1
                    index +=1
                max_length = max(max_length, length)

        return max_length
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = dict()
        result = []
        for num in nums:
            if num in hash_table.keys():
                hash_table[num] += 1
            else:
                hash_table[num] = 0
        while k > 0:
            max_value = max(hash_table.values())
            key_of_max_value = [key for key, v in hash_table.items() if v == max_value][0]
            result.append(key_of_max_value)
            hash_table.pop(key_of_max_value)
            k -= 1
        return result
        
        
                
        
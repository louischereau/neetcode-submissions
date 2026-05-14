class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        indeces = set()
        for triplet in triplets:
            if self.anyElementLargerThanInTarget(triplet, target):
                continue
            for i in range(3):
                if triplet[i] == target[i]:
                    indeces.add(i)

        return len(indeces) == 3

    def anyElementLargerThanInTarget(self, triplet, target):
        for i in range(3):
            if triplet[i] > target[i]:
                return True
        return False
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        hand.sort()
        count = Counter(hand)
        

        for initial_card in hand:
            if not count[initial_card]: continue
            for card in range(initial_card, initial_card + groupSize):
                if count[card]:
                    count[card] -= 1
                else:
                    return False

        return True
                 


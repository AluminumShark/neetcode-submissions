# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
            
        n = len(pairs)
        res = [list(pairs)]

        for i in range(1, n):
            j = i - 1
            curr = pairs[i]

            while j >= 0 and pairs[j].key > curr.key:
                pairs[j+1] = pairs[j]
                j -= 1

            pairs[j+1] = curr

            res.append(pairs[:])

        return res
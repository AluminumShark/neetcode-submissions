# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []

        res = []
        n = len(pairs)

        res.append(list(pairs))

        for i in range(1, n):
            cur = pairs[i]
            j = i - 1

            while j >= 0 and pairs[j].key > cur.key:
                pairs[j+1] = pairs[j]
                j -= 1
            pairs[j+1] = cur
            
            res.append(list(pairs))

        return res

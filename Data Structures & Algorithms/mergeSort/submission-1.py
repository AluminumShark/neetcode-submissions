# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
            
        mid = len(pairs) // 2

        leftSorted = self.mergeSort(pairs[:mid])
        rightSorted = self.mergeSort(pairs[mid:])

        return self.merge(leftSorted, rightSorted)

    def merge(self, left, right):
        i = j = 0
        res = []

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1

        return res

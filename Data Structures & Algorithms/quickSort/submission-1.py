# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quickSort(pairs, 0, len(pairs) - 1)
        return pairs
    def _quickSort(self, arr, start, end):
        if not arr or start < 0 or end >= len(arr):
            return

        if end - start + 1 <= 1:
            return arr

        pivot = arr[end]
        left = start

        for i in range(start, end):
            if arr[i].key < pivot.key:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        arr[left], arr[end] = arr[end], arr[left]

        self._quickSort(arr, start, left - 1)
        self._quickSort(arr, left + 1, end)
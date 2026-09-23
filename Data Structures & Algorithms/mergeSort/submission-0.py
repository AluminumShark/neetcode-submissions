# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._mergeSort(pairs, 0, len(pairs) - 1)
    def _mergeSort(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs

        medium = (start + end) // 2

        self._mergeSort(pairs, start, medium)
        self._mergeSort(pairs, medium + 1, end)

        self._merge(pairs, start, medium, end)

        return pairs

    def _merge(self, arr, start, medium, end):
        left = arr[start : medium + 1]
        right = arr[medium + 1 : end + 1]

        i, j, k = 0, 0, start

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
        return arr


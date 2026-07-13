class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for k, v in enumerate(numbers):
            c = target - v
            if v in d:
                return [min(d[v]+1, k+1), max(d[v]+1, k+1)]
            d[c] = k
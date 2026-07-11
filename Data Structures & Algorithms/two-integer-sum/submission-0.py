class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for k, v in enumerate(nums):
            c = target - v
            if c in d:
                return [d[c], k]
            d[v] = k
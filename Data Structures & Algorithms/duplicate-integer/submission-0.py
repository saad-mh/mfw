class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for el in nums:
            if el not in d:
                d[el] = 1
            else:
                return True
        return False
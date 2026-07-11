class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for el in s:
            if el not in d1:
                d1[el] = 1
            else:
                d1[el] += 1
        for el in t:
            if el not in d2:
                d2[el] = 1
            else:
                d2[el] += 1
        return d1 == d2
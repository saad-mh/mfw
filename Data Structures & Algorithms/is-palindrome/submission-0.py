class Solution:
    def isPalindrome(self, s: str) -> bool:
        cl = "".join(filter(str.isalnum, s))
        wha = list(cl.lower())
        i, j = 0, len(wha)-1
        while (i <= j):
            if not (wha[i] == wha[j]):
                return False
            i += 1
            j -= 1
        return True
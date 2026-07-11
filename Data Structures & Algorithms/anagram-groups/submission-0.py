class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i, el in enumerate(strs):
            d = {}
            for l in el:
                if l not in d:
                    d[l] = 1
                else:
                    d[l] += 1
            map[tuple(sorted(d.items()))] = map.get(tuple(sorted(d.items())), []) + [el]
        return list(map.values())
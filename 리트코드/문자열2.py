from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        print(a)
        for s in strs:
            a[''.join(sorted(s))].append(s)
        return list(a.values())
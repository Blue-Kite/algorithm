from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = collections.defaultdict(list)
        for s in strs:
            words[''.join(sorted(s))].append(s)
        return words.values()
        
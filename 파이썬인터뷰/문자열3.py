from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = collections.defaultdict(int)
        plist = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        
        for p in plist:
            if p not in banned:
                word[p] += 1
 
        maxcnt = 0
        for w in word.keys():
            if word[w] > maxcnt: 
                maxcnt = word[w]
                answer = w
        return answer

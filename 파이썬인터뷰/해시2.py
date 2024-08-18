from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sdict = collections.defaultdict(int)
        answer = 0
        start = 0

        # 중복 발생 : 중복 발생한 지점 + 1 으로 시작점 옮김 , 중복발생지점포함 이전은 윈도우 더 이상 포함 불가능하니까 
        # 중복 발생 x : 윈도우 크기 구함
        # 현재 문자의 위치 저장 

        for idx, item in enumerate(s):
            if item in sdict and start <= sdict[item]:
                start = sdict[item] + 1
            else:
                answer = max(answer, idx-start+1)
            sdict[item] = idx

        return answer
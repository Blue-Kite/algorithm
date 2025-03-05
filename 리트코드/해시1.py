#3. Longest Substring Without Repeating Characters

#슬라이딩 내부에서 중복이 발생하는지 확인
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        answer = 0

        for idx, st in enumerate(s):
            #슬라이딩
            if st in used and start <= used[st]:
                start = used[st] + 1
            else:
                answer = max(answer, idx-start+1)
            used[st] = idx
        return answer



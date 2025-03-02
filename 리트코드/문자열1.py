#Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''

        for i in range(len(s)-1):
            result = max(result, expand(i, i), expand(i, i+1), key=len)
        return result

"""
left: 회문의 가장 왼쪽, right: 회문의 가장 오른쪽
예를 들어, "aba"가 회문

left = 1, right = 1로 시작 (가운데 'b')
s[1] == s[1] 비교 (참)
확장: left = 0, right = 2
s[0] == s[2] 비교 ('a' == 'a', 참)
확장: left = -1, right = 3 (범위를 벗어남)
루프 종료 후 s[left+1:right] = s[0:3] = "aba" 반환
"""
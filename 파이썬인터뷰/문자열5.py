class Solution:
    def expandPalind(self, s, left, right):
        while left < right and left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        #통과를 못했기때문에 변경된 값을 원복하고 right는 슬라이싱이라서 어차피 -1됨
        return s[left+1 : right]

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        answer = ''
        for i in range(len(s) - 1): #len(s)-2까지 반복문 돌림
            answer = max(answer, self.expandPalind(s, i, i+1), self.expandPalind(s, i, i+2), key=len)
        return answer

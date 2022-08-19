class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 단순한 nested loop(N^2) -> Time Limit Exceeded
        # current longest length를 참고하여 loop(N^2)
        # current longest length를 참고하여 n-gram 형식으로
        
        longestPalindrome = ""
        length = 0
        
        for i in range(len(s)):
            curr = s[i:i+length]
            for j in range(i+length,len(s)):
                curr += s[j]
                if self.isPalindrome(curr):
                    if len(curr) > len(longestPalindrome):
                        longestPalindrome = curr
                        length = len(longestPalindrome)
        
        return longestPalindrome
                
    def isPalindrome(self, s: str) -> bool:
        
        if s == s[::-1]:
            return True
        else:
            return False
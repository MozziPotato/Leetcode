class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Brute Force (N^3) -> Time Limit Exceeded
        
        ############################################################################
        
        # current longest length를 참고하여 loop(N^3) -> Accepted(Runtime 9117ms)
        
        #longestPalindrome = ""
        #length = 0
        
        #for i in range(len(s)):
        #    curr = s[i:i+length]
        #    for j in range(i+length,len(s)):
        #        curr += s[j]
        #        if self.isPalindrome(curr):
        #            if len(curr) > len(longestPalindrome):
        #                longestPalindrome = curr
        #                length = len(longestPalindrome)
        #
        #return longestPalindrome
        
        ############################################################################
    
        # current longest length를 참고하여 n-gram check -> Time Limit Exceeded
        
        #longestPalindrome = ""
        #length = 0
        
        #for n_gram in range(1,len(s)+1):
        #    found = False
        #    startnum = 0
        #    endnum = n_gram
        #    while not found and endnum < len(s)+1:
        #        found = self.isPalindrome(s[startnum:endnum])
        #        if not found:
        #            startnum += 1
        #            endnum += 1
        #        else:
        #            longestPalindrome = s[startnum:endnum]
        #
        #return longestPalindrome
                
    #def isPalindrome(self, s: str) -> bool:
        
    #    if s == s[::-1]:
    #        return True
    #    else:
    #        return False
    
        length = len(s)
        longest = ""
        max_length = 0

        for i in range(0,length):
            
            # 홀수일 때, 좌우 expand 탐색
            left, right = i, i
            while left >= 0 and right < length and s[left] == s[right]:
                if right-left+1 > max_length:
                    longest = s[left:right+1]
                    max_length = right-left+1
                left -= 1
                right += 1
                
            # 짝수일 때, 좌우 expand 탐색
            left, right = i, i+1
            while left >= 0 and right < length and s[left] == s[right]:
                if right-left+1 > max_length:
                    longest = s[left:right+1]
                    max_length = right-left+1
                left -= 1
                right += 1
                
        return longest
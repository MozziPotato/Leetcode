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
    
        n = len(s)
        res = ""
        maxl = 0

        for i in range(0,n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxl:
                    res = s[l:r+1]
                    maxl = r-l+1
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > maxl:
                    res = s[l:r+1]
                    maxl = r-l+1
                l -= 1
                r += 1
        return res
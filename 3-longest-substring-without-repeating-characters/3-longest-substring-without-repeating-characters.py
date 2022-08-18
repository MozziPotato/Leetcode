class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        longest_length = 1
        
        for i in range(len(s)):
            
            mySet = set()
            curr_length = len(mySet)
            
            for j in range(i, len(s)):
                
                if s[j] not in mySet:
                    mySet.add(s[j])
                    curr_length += 1
                else:
                    if longest_length < curr_length:
                        longest_length = curr_length
                    break
            
            if longest_length < curr_length:
                longest_length = curr_length
        
        return longest_length
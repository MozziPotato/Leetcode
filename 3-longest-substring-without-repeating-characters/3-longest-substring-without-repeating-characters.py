class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        curr = ""
        longest = ""
        
        for ch in s:
            
            if ch not in curr:
                curr += ch
            else:
                if len(curr) > len(longest):
                    longest = curr
                curr += ch
                curr = curr[curr.find(ch)+1:]
        
        if len(curr) > len(longest):
            longest = curr
            
        return len(longest)
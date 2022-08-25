class Solution:
    def decodeString(self, s: str) -> str:
        if (right := s.find(']')) == -1:
            return s
        at = right - 1
        while s[at].isalpha():
            at -= 1    
        left = at
        at -= 1  # assert s[cursor] == '['
        while s[at].isdigit():
            at -= 1
            
        return self.decodeString(s[:at + 1] + (int(s[at + 1:left]) * s[left + 1:right]) + s[right + 1:])
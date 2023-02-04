class Solution:
    def romanToInt(self, s: str) -> int:
        
        # 12번 solution을 참고하여 벤치마킹
        # 숫자를 하나씩 더해주는 방식으로 진행
        
        integer = 0
        
        roman2value = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        
        index = 0
        
        while index <= len(s)-1:
            
            if index == len(s)-1:
                integer += roman2value[s[index]]
                index += 1
            else:
                roman = s[index] + s[index+1]
                if roman in roman2value.keys():
                    integer += roman2value[roman]
                    index += 2
                else:
                    integer += roman2value[roman[0]]
                    index += 1
        
        return integer
        
        
        
        
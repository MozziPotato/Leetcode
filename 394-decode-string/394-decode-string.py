class Solution:
    def decodeString(self, s: str) -> str:
        
        # ASCII numbers: 48 ~ 57
        # ASCII alphabets: 97 ~ 122
        
        container = []
        
        bracket_count = 0
        bracket = ""
        output = ""
        
        for ch in s:
            
            if ch == "[":
                if bracket_count == 0:
                    bracket_count += 1
                else:
                    bracket_count += 1
                    bracket += ch
            
            elif ch == "]":
                if bracket_count > 1 :
                    bracket_count -= 1
                    bracket += ch
                else:
                    bracket_count -= 1
                    container.append(bracket)
                    bracket = ""
            
            elif bracket_count > 0:
                bracket += ch
            
            else:
                container.append(ch)
                
        number = ""
        times = False
        
        for element in container:
            
            if len(element) > 1:
                tmp = self.decodeString(element)
                number = int(number)
                output += number * tmp
                number = ""
                
            elif 48 <= ord(element) <= 57:
                number += element
                times = True
              
            else:
                if number != "":
                    number = int(number)
                    output += number * element
                    number = ""
                else:
                    output += element
                
        return output
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        dictForRows = {i: list() for i in range(numRows)}
        
        row = 0
        down = True
        
        if numRows == 1:
            return s
        
        for ch in s:
            
            dictForRows[row].append(ch)
            
            if row == (numRows-1):
                down = False
            
            if row == 0:
                down = True
            
            if down:
                row += 1
            else:
                row -= 1
                
        output = ""
        
        for row, strings in dictForRows.items():
            for string in strings:
                output += string    
        
        return output
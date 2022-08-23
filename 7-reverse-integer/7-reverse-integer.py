class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            x = str(x)
            x = x[1:]
            x = x[::-1]
            
            if x[0] == "0":
                x = x[1:]
                
            x = -int(x)
            
        elif x > 0:
            x = str(x)
            x = x[::-1]
            
            if x[0] == "0":
                x = x[1:]
                
            x = int(x)
            
        else:
            return 0
        
        if x < -2**31 or x > 2**31-1:
            return 0
        
        else:
            return x
        
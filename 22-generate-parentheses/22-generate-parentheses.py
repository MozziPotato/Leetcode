class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        
        def generator(out=[], left=0, right=0):
            
            if len(out) == 2*n:
                output.append("".join(out))
                return
                
            if left < n:
                out.append("(")
                generator(out, left+1, right)
                out.pop()
            
            if right < left:
                out.append(")")
                generator(out, left, right+1)
                out.pop()
                
        generator()
        
        return output
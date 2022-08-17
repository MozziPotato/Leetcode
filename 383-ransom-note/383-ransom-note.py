class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        isCanConstruct = True
        note = dict()
        mag = dict()
        
        for spel in ransomNote:
            if spel in note:
                note[spel] += 1
            else:
                note[spel] = 1
        
        for spel in magazine:
            if spel in mag:
                mag[spel] += 1
            else:
                mag[spel] = 1
            
        for spel in set(ransomNote):
            if not spel in mag:
                isCanConstruct = False
            else:
                if mag[spel] < note[spel]:
                    isCanConstruct = False
                    
        return isCanConstruct
        
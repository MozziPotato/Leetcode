class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        c = Counter(arr)
        halfSize = len(arr)/2
        
        setCount = 0
        setSize = 0
        
        for num, counts in c.most_common():
            setCount += counts
            setSize += 1
            if setCount >= halfSize:
                return setSize
        
        return setSize
            
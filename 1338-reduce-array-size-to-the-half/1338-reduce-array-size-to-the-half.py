class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        myDict = dict()
        halfSize = len(arr)/2
        
        for ele in arr:
            
            if ele in myDict:
                myDict[ele] += 1
            else:
                myDict[ele] = 1
                
        myDict = dict(sorted(myDict.items(), key=lambda x:x[1], reverse=True))
        
        sumSize = 0
        count = 0
        
        for key, val in myDict.items():
            sumSize += val
            count += 1
            if sumSize >= halfSize:
                break
                
        return count
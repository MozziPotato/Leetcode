class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # 01.28 PM 7:10 ~ 8:40 (1 hour and half)

        # unsorted array에서 가장 작은 missing integer을 찾는데,
        # time Complexity를 O(n)으로 맞추기 위해서는 sorting 작업 없이 해야될 것으로 보임.
        # 결국 array를 그대로 놔두고 n바퀴 안에서 해결해야 함.
        # 일단 exception부터 처리.

        # n개의 pointer를 쓰는 방식을 생각해보다가 막혔는데, related topic을 보니까 Hash Table이 있음.
        # 그러면 array를 돌면서 어떤 hash function으로 elements를 분리시켜봐야 한다는 것 같은데...
        # 단순히 분리만 시키는 것 만으로는 작은 값을 찾기 어려울 것 같고, 분리시키면서 동시에 정렬을 해내야 할 것 같음.
        # 아무튼, O(N)의 작업을 통해 정렬된 무언가를 만들어내고,
        # 최종 정렬된 array를 돌며 missing value를 찾아내야 할 것으로 생각.

        # 그러면 어떻게 hash function을 사용해서 분리 + 정렬을 수행할 수 있을까?
        # 1. 일단 첫 번째 바퀴를 돌면서 양수의 min 값과 max 값을 찾아낸다. -> O(N)
        # 2. [0] * max 만큼의 new array(결국 hash table)를 만든다.
        # 3. 두 번째 바퀴를 돌면서 양수의 값을 index로 갖는 new array의 값을 +1 한다. -> O(N)
        # 4. new array를 돌면서 최초의 0이 있는 값의 index를 return. -> O(N)
        # 최종적으로 O(3N) 이면 끝낼 수 있음.

        # # exception
        # if len(nums) == 1:
        #     if nums[0] != 1:
        #         return 1
        #     else:
        #         return 2

        # min_value = math.inf
        # max_value = -math.inf
        
        # # find min, max
        # for num in nums:
        #     if num > 0:
        #         if num < min_value:
        #             min_value = num
        #         if num > max_value:
        #             max_value = num
        
        # # exception (all nums are negative)
        # if max_value == -math.inf:
        #     return 1
        
        # # make hash table
        # hash_table = [0] * max_value

        # # hashing
        # for num in nums:
        #     if num > 0:
        #         hash_table[num-1] += 1

        # # find first 0's index (=missing value) and return
        # for idx, hash_value in enumerate(hash_table):
        #     if hash_value == 0:
        #         return idx + 1
                
        # # if all elements are sorted
        # return max_value + 1

        # problem: 매우 큰 수가 있으면 new array를 만들 때 memory를 크게 잡아먹으면서 Runtime Error(MemoryError)
        # solution: dictionary
        # 그러면 min, max를 찾아다닐 필요가 없으니 len(nums)==1 에 대한 exception도 불필요해짐.
        # 1바퀴 돌면서 key랑 value만 update 한 후에, 1부터 max 값까지 for문 돌면서 최초로 key가 없는 값을 return.

        # make hash table
        hash_table = dict()

        # get max value
        max_value = 0

        # hashing
        for num in nums:
            if num > 0:
                if num not in hash_table.keys():
                    hash_table[num] = 1
                else:
                    hash_table[num] += 1
                if num > max_value:
                    max_value = num

        # exception (all values are negative)
        if max_value == 0:
            return 1

        # find missing key
        for key in range(1, max_value+1):
            if not hash_table.get(key):
                return key
        
        # exception (all values are sorted)
        return max_value + 1

        # solution 2
        # i=1
        # num_set = set(nums)
        # while True:
        #     if i not in num_set:
        #         i += 1
        # return i

        

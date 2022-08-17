class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        amount_list = []
        
        for account in accounts:
            amount_list.append(sum(account))
            
        return max(amount_list)
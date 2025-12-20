class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for customers in accounts:
            for j in range(1, len(customers)):
                customers[j] += customers[j - 1]
        for i in range(1, len(accounts)):
            accounts[i][-1] = max(accounts[i][-1], accounts[i - 1][-1])
        return accounts[-1][-1]
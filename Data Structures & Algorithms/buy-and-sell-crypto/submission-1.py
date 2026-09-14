class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices)[::-1]:
            return 0
        
        prof = 0
        for i in range (len(prices)):
            for j in range(i, len(prices)):
                prof = max(prof,(prices[j]-prices[i]))
        return prof

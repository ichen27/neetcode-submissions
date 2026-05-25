class Solution:
    def rob(self, nums: List[int]) -> int:
        # Brute force approach:
        ## Each home, return every possible combination
        ## Combinations include skipping one house or 2 houses
        ## Start from first or second house

        # 2 recursive functions
        # Recursive function
        ## Max of combinations of i + 1 or i + 2
        ## Global variable
        ## add amount of money 

        maxMoney = 0
        index = 0
        hist = {}

        def recursive_robber(index):
            nonlocal maxMoney
            if index >= len(nums):
                return 0
            
            if index in hist:
                return hist[index]

            oneSkip = recursive_robber(index + 2)
            twoSkip = recursive_robber(index + 3)
            
            money = nums[index] + max(oneSkip, twoSkip)

            maxMoney = max(maxMoney, money)

            hist[index] = money


            return money

        recursive_robber(index) 
        recursive_robber(index + 1)


        return maxMoney
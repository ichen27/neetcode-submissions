class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Greedy algorithm; take best possible cases
        # [2]
        # [2, -3]
        # [2, -3, 4]
        # Array that ends that i, take max sub array
        # For loop to iterate through array:
        # Update max when reaches a new max sub array
        

        # Brute force approach
        # iterate through array, nested array
        # Find max sum
        # variable fo max


        subarrays = []
        runningSum = 0
        maxNum = 0
        i = 0
        j = 0
        while i < len(nums):
            j = i
            while j < len(nums) + 1:
                if j < len(nums):
                    runningSum = runningSum + nums[j]
                    if runningSum < nums[j]:
                        i = j-1
                        break
                subarrays.append(nums[i:j])
                if runningSum > maxNum or j == 0:
                    maxNum = runningSum

                j += 1
            runningSum = 0
            i += 1
                
        for i in subarrays:
            print(i)

        return maxNum
                



class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recursive Function
        # Dont rob and move on or rob and skip 1

        if len(nums) == 1:
            return nums[0]

        nofirst = nums[1:len(nums)]
        nolast = nums[0:len(nums) - 1]

        print(f"first: {nofirst}")
        print(f"last: {nolast}")
        
        def recursiveRobber(index, houseMem, num):
            if index >= len(num):
                return 0

            if index in houseMem:
                return houseMem[index]

            skip = recursiveRobber(index + 1, houseMem, num)
            rob = num[index] + recursiveRobber(index + 2, houseMem, num)

            houseMem[index] = max(skip, rob)


            return houseMem[index]
        

        return max(recursiveRobber(0, {}, nofirst), recursiveRobber(0, {}, nolast))

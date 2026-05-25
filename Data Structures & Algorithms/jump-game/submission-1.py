class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Integer array
        # Each element is max jump length from that position
        # 1 = jump 1 index, 2 = jump 1 or 2 indexes
        # Start from index 0
        
        # Backtracking solution
        # Trying everying jump length availible from every position 
        # Reach end return True
        # Return true if any are true

        # Optimization:
        ## Stores boolean value from each index in dict
        ## if already in dict, return that value

        mem = {}

        def recursiveJumper(index):
            nonlocal mem
            # Base cases
            # If index reaches last index, return True
            # If goes past last index, return False
            if index == len(nums) - 1:
                return True
            elif index >= len(nums):
                return False

            if index in mem:
                return mem[index]
            
            # Jump length is the element at the index
            jumpLength = nums[index]

            # If you can't jump from that position, return false
            if jumpLength == 0:
                return False

            # Iterates through every possible jump from an index
            # If any return True, then return True
            for i in range(1, jumpLength + 1):
                if recursiveJumper(index + i) == True:
                    mem[index] = True
                    return True
            
            # If no combination returns True, return False
            mem[index] = False
            return False

        return recursiveJumper(0)






        
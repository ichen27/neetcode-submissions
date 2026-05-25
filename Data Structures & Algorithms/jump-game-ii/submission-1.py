class Solution:
    def jump(self, nums: List[int]) -> int:
        # Array nums where each element represents max length of jump from that index
        # Minimum number of jumps it takes to reach the last positions


        # Greedy solution 
        # Iterate backward
        # Store each elements min jump to get to end 
        # Array of same length as nums that stores min jump from index

        # array of -1 of same length as nums
        # will store mininum jumps
        jump = [-1] * len(nums)
        jump[-1] = 0
        # minimum index an index must jump to in order to reach end
        target = len(nums) - 1

        # Iterate backwards
        for i in range(len(nums) - 2, -1, -1):
            # If index can reach the target
            if i + nums[i] >= target:
                # Range within nums that the index can jump to
                jumpRange = i + nums[i] + 1
                if jumpRange > len(nums):
                    jumpRange = len(nums)
                # Calculates the index with min jumps within its jump range
                # That will be in the next jump
                next = min(jump[target:jumpRange], key=lambda x: x if x >= 0 else len(nums))
                # New target becomes current
                target = i
                # The min jump of current index becomes 1 + the jumps after
                jump[i] = 1 + next
        
        print(jump)
        # return the min jump from first index
        return jump[0]




        
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy algorithm
        # starting at first index
        # Iterate through every possible jump, and jump to furthest possible jump

        # right and left pointer, jump count
        right = left = 0
        count = 0

        # Runs as long as left pointer is not at the last index
        while left < len(nums) - 1:
            maxJump = 0
            maxIndex = 0

            if nums[left] + left >= len(nums) - 1:
                count += 1
                return count
            # As long as the right pointer is in the range or in the array
            while right <= left + nums[left] and right < len(nums):
                # Update maxJump if element has further jump
                if nums[right] + right > maxJump:
                    maxJump = nums[right] + right
                    maxIndex = right
                right += 1
            
            # Increment count
            # Jump to max Index
            count += 1
            left = maxIndex
            right = maxIndex

        return count

        

        
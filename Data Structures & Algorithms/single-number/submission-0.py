class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        reverse = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for x,y in count.items():
            if y == 1:
                return x


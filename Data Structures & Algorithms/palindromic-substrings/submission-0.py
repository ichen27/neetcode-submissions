class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        # expands out given a left and right
        # Conditional checks of expansion
        def expand(left, right):
            nonlocal count
            while True:
                if left < 0 or right > len(s) - 1:
                    break

                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break



        # loop to each value
        # Odd and even
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)


        return count
        
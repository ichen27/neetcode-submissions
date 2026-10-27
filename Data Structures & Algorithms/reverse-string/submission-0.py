class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """


        r = 0
        l = len(s) - 1


        while r < l:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp

            r += 1
            l -= 1


        return s
class Solution:
    def isHappy(self, n: int) -> Bool:
        curr = []
        past = []
        temp = n
        add = 0

        while True:
            past.append(n)
            curr = []
            add = 0
            temp = n
            
            while temp > 0:

                curr.append(temp % 10)
                temp //= 10

            for i in curr:
                add = add + (i * i)

            if add == 1:
                return True
            if add in past:
                return False

            n = add
        
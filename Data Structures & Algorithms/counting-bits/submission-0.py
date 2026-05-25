class Solution:
    def countBits(self, n: int) -> List[int]:
        # Arr from 0 - n
        # Counts number of 1's in binary representation of every number

        # For loop in range from 0 to n
        # For each n, add mod 2 and shift over

        bit_arr = []

        for i in range(n+1):
            num = i
            bit_count = 0

            while num != 0:
                bit_count += num % 2
                num = num >> 1

        
            bit_arr.append(bit_count)


        return bit_arr





                
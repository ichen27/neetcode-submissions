class Solution:
    def numDecodings(self, s: str) -> int:
        # Hash map with letters to numbers
        # Decode helper function
        # Recursive Function, traverse with 1 digit or 2
        alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        count = 0

        def decoder(remaining: str) -> int:
            nonlocal count
            if remaining == "":
                count += 1
                return
            if int(remaining[0]) <= 26 and int(remaining[0]) != 0:
                decoder(remaining[1:])
            if len(remaining) > 1:
                if int(remaining[0:2]) <= 26 and remaining[0:2][0] != "0":
                    decoder(remaining[2:])

            return
        
        decoder(s)
        return count

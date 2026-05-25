class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + f"{len(i)}#{i}"
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        new_s = []
        start = 0
        if len(s) == 1:
            return [""]

        while start < len(s) - 1:
            length = ""
            for i in range(start, len(s)):
                if s[i] == "#":
                    start = i + 1
                    break
                length = length + s[i]
            print(f"Length: {length}")
        
            length = int(length)

            new_s.append(s[start:start + length])
            start = start + length
        
        return new_s

        

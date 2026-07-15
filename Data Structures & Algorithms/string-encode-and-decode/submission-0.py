class Solution:
    def __init__(self):
        self.shift = -10
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            tmp = ""
            for c in s:
                tmp += chr((ord(c) + self.shift) % 256)
            
            encoded_str += tmp + "❤"

        print(encoded_str)
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        tmp = ""
        print(s)
        for c in s:
            if c == "❤":
                print(tmp)
                decoded_strs.append(tmp)
                tmp = ""
                continue
            tmp += chr((ord(c) - self.shift) % 256)

        return decoded_strs
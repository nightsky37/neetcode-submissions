class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
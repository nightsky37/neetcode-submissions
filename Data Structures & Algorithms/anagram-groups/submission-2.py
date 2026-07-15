class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            
            freq = tuple(freq) # dict key must be immutable
            print(freq)
            if freq not in table:
                table[freq] = [s]
            else:
                table[freq].append(s)
        
        return list(table.values())
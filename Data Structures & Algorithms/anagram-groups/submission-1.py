class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        for idx, s in enumerate(strs):
            is_added = False
            for g in result:
                if s in g:
                    is_added = True
            if is_added: continue
            table_cur = {}
            group = [s]
            for c in s:
                table_cur[c] = table_cur.get(c, 0) + 1
            for i, s_tmp in enumerate(strs[idx + 1:]):
                table_tmp = {}
                for c in s_tmp:
                    table_tmp[c] = table_tmp.get(c, 0) + 1
                if table_cur == table_tmp:
                    group.append(s_tmp)

            result.append(group)

        return result
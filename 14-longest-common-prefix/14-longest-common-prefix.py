class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        pre_idx = 0
        
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                pre_idx += 1
            else:
                break
        return strs[0][:pre_idx] if pre_idx else ""
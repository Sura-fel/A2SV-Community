class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        for i in range(len(a), 0, -1):
            if all([(a[:i] == wrd[:i]) for wrd in strs]):
                return a[:i]
            i -= 1
        return ""

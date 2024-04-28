class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words = [set(wrd) for wrd in words]
        i, count = 0, 0
        while i<len(words)-1:
            for j in range(i+1, len(words)):
                if words[i] == words[j]:
                    count += 1
            i += 1
        return count

from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for word in words:
            cur = Counter(word)
            count = count&cur
        return list(count.elements())

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr=" ".join(words)

        subStr=[word for word in words if arr.count(word)>1]

        return subStr
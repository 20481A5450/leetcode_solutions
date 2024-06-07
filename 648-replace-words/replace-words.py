from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Sort dictionary based on length of roots to ensure shortest root is used first
        dictionary.sort(key=len)
        
        def replace(word):
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word
        
        words = sentence.split()
        replaced_words = [replace(word) for word in words]
        
        return ' '.join(replaced_words)
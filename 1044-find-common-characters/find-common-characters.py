from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the counter with the first word's frequencies
        min_freq = Counter(words[0])
        
        # Update the counter to the minimum frequencies across all words
        for word in words[1:]:
            word_counter = Counter(word)
            for char in min_freq:
                if char in word_counter:
                    min_freq[char] = min(min_freq[char], word_counter[char])
                else:
                    min_freq[char] = 0
        
        # Collect the characters based on the minimum frequencies
        result = []
        for char, freq in min_freq.items():
            result.extend([char] * freq)
        
        return result

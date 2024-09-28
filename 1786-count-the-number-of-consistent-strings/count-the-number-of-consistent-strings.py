class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        # create a hash map to store the string (allowed) characters
        hash = set()
        for i in allowed:
            hash.update(i)

        # Loop through each word in the 'words' array
        for word in words:
            check = 1   # Initialize check as true for each word
            for char in word:
                # if any character of the string doesn't exist in hashmap, mark the word as inconsistent
                if char not in hash: 
                    check = 0
            # If 'check' is still true, the word is consistent; increment the result
            if check == 1: res+=1
        return res
        
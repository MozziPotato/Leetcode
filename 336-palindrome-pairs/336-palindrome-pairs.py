class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        def is_palindrome(string):
            return string == string[::-1]

        # map with index
        words = {word: i for i, word in enumerate(words)}

        palins = []
        for word, idx in words.items():
            for i in range(len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]

                if is_palindrome(prefix):
                    rev = suffix[::-1]
                    if rev != word and rev in words:
                        palins.append([words[rev], idx])

                # i != len(word) must be checked,
                # because this means "" is being appended,
                # while "" is already prepended.
                if i != len(word) and is_palindrome(suffix):
                    rev = prefix[::-1]
                    if rev != word and rev in words:
                        palins.append([idx, words[rev]])

        return palins
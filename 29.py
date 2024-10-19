from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        
        # Initialize basic variables
        word_len = len(words[0])
        total_words = len(words)
        substring_len = word_len * total_words
        word_count = Counter(words)  # Count the frequency of words in the words array
        result = []

        # Loop through each starting index in s, but only the first "word_len" indices
        for i in range(word_len):
            left = i
            current_count = Counter()  # Tracks words in the current window
            word_counted = 0  # Number of valid words counted in the current window
            
            # Traverse the string in chunks of word_len
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]  # Extract word from current window
                
                if word in word_count:
                    current_count[word] += 1
                    word_counted += 1
                    
                    # If a word count exceeds the expected frequency, slide the window
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        word_counted -= 1
                        left += word_len
                    
                    # Check if we found a valid concatenated substring
                    if word_counted == total_words:
                        result.append(left)
                else:
                    # Reset if the word is not in words
                    current_count.clear()
                    word_counted = 0
                    left = right + word_len
        
        return result
        

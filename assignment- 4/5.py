sentence = input("Enter a sentence: ")
words = sentence.split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Frequency of occurrence of each word in the given sentence:")
print(word_freq)
max_freq = max(word_freq.values())
most_frequent_words = [word for word, freq in word_freq.items() if freq == max_freq]

print("Word(s) with highest frequency:")
print(most_frequent_words)

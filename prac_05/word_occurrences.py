word_occurrence = {}
user_text = input("Enter a sentence: ")
words = user_text.split()

for word in words:
    frequency = word_occurrence.get(word, 0)
    word_occurrence[word] = frequency + 1

for word in sorted(word_occurrence):
    print(f"{word:{max(len(word) for word in words)}} : {word_occurrence[word]}")


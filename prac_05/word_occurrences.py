
user_text = input("Enter a sentence: ")
words = user_text.split()
print(words)
for word in words:
    print(len(words[word]))
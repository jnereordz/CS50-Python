import emoji

word = input("Input: ")

response = emoji.emojize(word, language='alias')
print(f"Output: {response}")


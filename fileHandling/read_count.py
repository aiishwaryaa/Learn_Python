with open("new_file.txt", "r") as f:
    text = f.read()
words = text.split()
print("word count:", len(words))    
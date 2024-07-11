user = input("Enter sentences: ")

sentences = []

curr = ""

for i in user:
    curr += i
    if i in ".!?":
        sentences.append(curr)
        curr = ""

if curr:
    sentences.append(curr)

print(sentences)

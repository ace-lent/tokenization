user = input("Enter: ")

words = []
curr = ""

for i in user:
    if i in ",;|":
        if curr:  
            words.append(curr)
            curr = ""
    else:
        curr += i

if curr: 
    words.append(curr)

print(words)

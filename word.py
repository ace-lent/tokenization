user = input("enter sentence: ")
arr = []
curr = ""

for i in user:
    if i == " ":
        arr.append(curr)
        curr = ""  
    else:
        curr += i

arr.append(curr)

print(arr)
list_url = []

# Push
list_url.append('https://www.w3schools.com/python/python_dsa_stacks.asp')
list_url.append('https://www.w3schools.com/python/default.asp')
list_url.append('https://www.w3schools.com/python/python_intro.asp')
print("Stack: ", list_url)

# Peek
topElement = list_url[-1]
print("Peek: ", topElement)

# Pop
poppedElement = list_url.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", list_url)

# isEmpty
isEmpty = not bool(list_url)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(list_url))
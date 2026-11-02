#hello
with open("data.txt", "r") as f:
    contents = f.read()
print(contents)
print(contents.count('e'))

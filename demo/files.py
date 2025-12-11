# with open("data.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# with open("output.txt", "w") as f:
#     f.write("Result: " + content)

# with open("data.txt", "r") as f:
#     content = f.read()
#     print(content)

with open("data.txt", "r") as f:
    content = f.read()
    print("Words: ", len(content.split(" ")))
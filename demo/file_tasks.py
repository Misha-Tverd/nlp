import re

with open("data.txt", "r") as f:
    content = f.read()
    # line = len(re.findall(r'[.?!]\s*', content))
    # print(line)



    line = content.lower()
    count = 0
    if "python" in line:
        count += 1
        print(count)

    with open("data_copy.txt", "w") as repeat:
        repeat.write(content)
        print(repeat)



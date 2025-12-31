import json

with open("user.json", "r") as f:
    content = json.load(f)
    content["skills"].append("linux-admin")
    print(content)
    # json.dump(f, content)

with open("user.json", "a") as f:
    print(content)
    json.dump(content, f)
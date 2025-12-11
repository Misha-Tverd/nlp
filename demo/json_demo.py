import json 


user = {
    "name": "Misha",
    "age": 23,
    "skills": ["python", "git", "linux"]

}

with open("user.json", "w") as f:
    print(f)
    json.dump(user, f)

with open("user.json", "r") as f:
    data = json.load(f)
    print(data["skills"])

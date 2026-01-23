def read(path) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write(path, text):
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)

def format_result(data: dict) -> str:
    text = ""
    for key, value in data.items():
        text += f"{key}: {value}\n"
    return text
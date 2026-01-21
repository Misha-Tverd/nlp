
def read_text_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
            return ""
    except Exception:
            return ""    
        

def write_text_file(path, text):
    erorrs = []
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)
    except Exception:
        return "Path to file not correct"
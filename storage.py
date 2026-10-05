import json,os

DEFAULT_FILE = "tasks.json"

def load_tasks(file_path=DEFAULT_FILE):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            return []
        return json.loads(content)

def save_tasks(tasks, file_path=DEFAULT_FILE):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


 


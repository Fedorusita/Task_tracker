import json,os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)  

 


# if __name__ == "__main__":
#     tasks = load_tasks()
#     tasks.append({"id": 1, "description": "test", "status": "todo"})
#     save_tasks(tasks)
#     print(load_tasks())
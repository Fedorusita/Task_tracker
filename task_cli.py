import sys
from datetime import datetime
from storage import save_tasks, load_tasks

def add_task(description):
    tasks = load_tasks()
    new_id = max((t["id"] for t in tasks), default = 0) + 1
    now = datetime.now().isoformat()
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createAt": now,
        "updateAT": now,
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [args]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: description is required")
            return
        add_task(sys.argv[2])
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
# command = sys.argv[1] if len(sys.argv) > 1 else None

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


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Error: task with ID {task_id} not found")


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
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: update requires <id> and <description>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print(f"Error: '{sys.argv[2]}' is not a valid ID")
            return
        update_task(task_id, sys.argv[3])
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
# command = sys.argv[1] if len(sys.argv) > 1 else None

import json
import os

TODO_FILE = "todo.json"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def handle_todo(args):
    if not args:
        print("todo 可用命令：add/list/delete")
        return

    command = args[0]
    todos = load_todos()

    if command == "add":
        item = " ".join(args[1:])
        todos.append(item)
        save_todos(todos)
        print(f"已添加：{item}")

    elif command == "list":
        if not todos:
            print("暂无待办事项")
        for i, t in enumerate(todos, 1):
            print(f"{i}. {t}")

    elif command == "delete":
        try:
            index = int(args[1]) - 1
            removed = todos.pop(index)
            save_todos(todos)
            print(f"已删除：{removed}")
        except:
            print("删除失败，请确认编号是否正确")

    else:
        print("未知 todo 命令")

import argparse
from .weather import get_weather
from .todo import handle_todo
from .notes import write_note
from .ipinfo import get_ip_info

def main():
    parser = argparse.ArgumentParser(description="DailyToolkit CLI")
    parser.add_argument("tool", help="选择工具：weather/todo/notes/ip")
    parser.add_argument("arg", nargs="*", help="工具参数")

    args = parser.parse_args()

    if args.tool == "weather":
        city = " ".join(args.arg)
        get_weather(city)
    elif args.tool == "todo":
        handle_todo(args.arg)
    elif args.tool == "notes":
        write_note()
    elif args.tool == "ip":
        get_ip_info()
    else:
        print("未知工具")

if __name__ == "__main__":
    main()

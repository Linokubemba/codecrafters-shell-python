import sys

COMMANDS = { "echo", "exit", "type" }

def run(cmd, args):
    match cmd:
        case "echo":
            print(args)
        case "type":
            if not (args in COMMANDS):
                raise ValueError(args + ": not found")
            print(args, "is a shell builtin")
        case default:
            raise ValueError(cmd + ": command not found")

def main():
    while True:
        sys.stdout.write("$ ")
        cmd, *args = input().split(" ", 1)
        if cmd == "exit":
            sys.exit(0)

        try:
            run(cmd, args[0] if args else "")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

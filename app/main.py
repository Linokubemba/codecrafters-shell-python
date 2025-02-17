import sys

def echo(args: str):
    print(args)

def exit(status: int):
    sys.exit(status)

def type(cmd: str):
    suffix = ": command not found"
    if cmd in COMMANDS:
        suffix = " is a shell builtin"
    print(cmd + suffix)

def parse_cmd(input: str) -> str | None:
    cmd, *args = input.split(" ", 1)
    return cmd, args

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        cmd, args = parse_cmd(input())
        try:
            run = COMMANDS[cmd]
            run(args[0])
        except Exception:
            print(cmd + ": command not found")



if __name__ == "__main__":
    COMMANDS = {
        "echo": echo,
        "exit": exit,
        "type": type
    }
    main()

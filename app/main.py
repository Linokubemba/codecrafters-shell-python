import sys

def parse_cmd(input: str) -> str | None:
    cmd, *args = input.split(" ", 1)    
    return cmd, args

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        cmd, args = parse_cmd(input())
        match cmd:
            case "exit":
                sys.exit(args[0])
            case "echo":
                print(args[0])
            case "type" | _:
                if cmd == "type" and args[0] in ["type", "echo", "exit"]:
                    print(args[0], "is a shell builtin")
                else:
                    print(cmd + ": command not found")



if __name__ == "__main__":
    main()

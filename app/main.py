import sys

def parse_cmd(input: str) -> str | None:
    args = input.split(" ", 2)
    cmd = args[0]
    match cmd:
        case "echo":
            if len(input) > 4:
                return input[5:]
        case _:
            return cmd + ": command not found"

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        in_cmd = input()
        if in_cmd == "exit 0":
            sys.exit(0)
        out_cmd = parse_cmd(in_cmd)
        print(out_cmd)



if __name__ == "__main__":
    main()

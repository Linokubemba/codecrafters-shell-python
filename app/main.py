import sys
import subprocess


def exec_sh(input):
    if input == "exit 0":
        sys.exit(0)

    status, output = subprocess.getstatusoutput(input)
    cmd, *args = input.split(" ", 1)
    if status != 0:
        msg = f"{args[0]}:" if args else f"{cmd}: command"
        raise ValueError(f"{msg} not found")

    print(output)


def main():
    while True:
        sys.stdout.write("$ ")
        try:
            exec_sh(input())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

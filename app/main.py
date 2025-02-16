import sys


def main():
    status = 1
    while status:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        in_value = input()
        if in_value == "exit 0":
            status = 0
            break
        print(in_value + ": command not found")

    return status


if __name__ == "__main__":
    print(main())

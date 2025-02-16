import sys

def get_input():
    sys.stdout.write("$ ")
    in_value = input()
    return in_value + ": command not found\n"


def main():
    while True:
        out_value = get_input()
        sys.stdout.write(out_value)



if __name__ == "__main__":
    main()

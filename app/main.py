import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    in_value = input()
    out_value = in_value + ": command not found"
    sys.stdout.write(out_value)


if __name__ == "__main__":
    main()

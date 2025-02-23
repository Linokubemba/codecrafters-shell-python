import os
import sys
import subprocess


BUILTIN_CMDS = {
    "echo", "type", "exit", "pwd"
}

def exec_builtin(cmd, args):
    match cmd:
        case "pwd":
            return os.getcwd()
        case "echo":
            return args
        case "type":
            if args in BUILTIN_CMDS:
                return args + " is a shell builtin"
            return exec_sh(cmd, args)

def exec_sh(cmd, args):
    input = " ".join([cmd, args])
    status, output = subprocess.getstatusoutput(input)
    if status != 0:
        msg = f"{args}:" if args else f"{cmd}: command"
        raise ValueError(f"{msg} not found")
    return output

def main():
    while True:
        sys.stdout.write("$ ")
        sh_input = input()        
        try:
            if sh_input == "exit 0":
                sys.exit(0)

            cmd, *args = sh_input.split(" ", 1)
            args = args[0] if args else ""
            output = exec_builtin(cmd, args) \
                    if cmd in BUILTIN_CMDS \
                    else exec_sh(cmd, args)

            sys.stdout.write(output + "\n")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

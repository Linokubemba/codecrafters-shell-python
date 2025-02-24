import os
import sys
import subprocess


class BuiltinHandler:
    def __init__(self):
        self.BUILTIN_CMDS = {
            "echo", "type", "exit", "pwd", "cd"
        }
        self.active_dir = os.getcwd()
    
    def echo(self, args):
        print(args)
    
    def exit(self, args):
        sys.exit(int(args))

    def pwd(self, _):
        print(self.active_dir)
    
    def cd(self, args):
        path_dirs = self.active_dir.split("/")
        target_dirs = args.split("/") if "/" in args else [args]
        for i, dir in enumerate(target_dirs):
            if dir == "" and i == 0:
                path_dirs = [""]
            elif dir == "~":
                path_dirs = [os.environ.get("HOME")]
            elif dir == "..":
                path_dirs.pop()
            elif dir != ".":
                path_dirs.append(dir)
        
        tmp = "/".join(path_dirs)
        if not os.path.exists(tmp):
            raise ValueError("cd: " + tmp + ": No such file or directory")
        self.active_dir = tmp.removesuffix("/")

    def type(self, args):
        if not (args in self.BUILTIN_CMDS):
            for path in os.environ.get("PATH").split(os.pathsep):
                cmd_path = os.path.join(path, args)
                if os.path.exists(cmd_path):
                    print(" ".join([args, "is", cmd_path]))
                    return
            
            raise ValueError(args + ": not found")
        print(args + " is a shell builtin")


def main():
    builtin_executor = BuiltinHandler()
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        sh_input = input()

        try:
            cmd, *args = sh_input.split(" ", 1)
            args = args[0] if args else ""
            if cmd in builtin_executor.BUILTIN_CMDS:
                run = getattr(builtin_executor, cmd)
                run(args)
            else:
                status, output = subprocess.getstatusoutput(sh_input)
                if status != 0:
                    raise ValueError(cmd + ": command not found")
                sys.stdout.write(output + "\n")

        except Exception as e:
            sys.stdout.write(e.__str__() + "\n")


if __name__ == "__main__":
    main()

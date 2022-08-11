# mdb by Emrecan Öksüm
# Debug Minecraft Datapack functions with ease

from pymchat.chat import Chat
from os import path
from time import sleep

version = "1.0"

def readFunction(dir):
    if not path.exists(dir):
        print("Cannot locate the functions file in {}!".format(dir))
        exit(0)
    with open(dir, "r") as fh:
        cmds = fh.readlines()
    return cmds

def runCommand(cmd):
    chat = Chat()
    chat.send(cmd)

def getCommand(limit=1):
    chat = Chat()
    data = chat.get_history(limit=limit)
    return data

def runAndGet(cmd):
    runCommand(cmd)
    sleep(1)
    data = getCommand()
    return data[0].content

def debugger(cmd):
    if cmd[0] != "/":
        cmd = "/" + cmd
    output = runAndGet(cmd)
    if output.find("<--[HERE]") != -1:
        return (0, output)
    return (1,)

def main():
    print("Welcome to mdb v{}".format(version))
    print("=" * 10)
    fPath = input("Please input the location of your .mcfunction file: ")
    cmds = readFunction(fPath)
    cmdsLen = len(cmds)
    print("Function loaded successfully! Loaded {} commands into mdb.".format(cmdsLen))
    
    # Debugger config
    id = 0
    breakpoints = [] # Make sure its empty
    isBreakpointHit = 0
    run = 0
    
    while id < cmdsLen:
        cmd = cmds[id]
        print("Cursor is currently at command {}".format(id))
        if id in breakpoints:
            isBreakpointHit = 1
            run = 0
            breakpoints.remove(id)
            print("Breakpoint hit at command: {}".format(id))
        
        if run == 0:
            print("({}) {}".format(id, cmd))
            icmd = input("(mdb) ")
            inputarg = icmd.split(" ")
            while True:
                if inputarg[0] == "hop":
                    out = debugger(cmd)
                    if out[0] == 0:
                        print("Exception detected at command {} !\n\nException is: {}".format(id, out[1]))
                        run = 0
                    id += 1
                    break
                elif inputarg[0] == "run":
                    run = 1
                    out = debugger(cmd)
                    if out[0] == 0:
                        print("Exception detected at command {} !\n\nException is: {}".format(id, out[1]))
                        run = 0
                    id += 1
                    break
                elif inputarg[0] == "+break":
                    breakpoints.append(int(inputarg[1]))
                    break
                elif inputarg[0] == "-break":
                    breakpoints.remove(int(inputarg[1]))
                    break
                elif inputarg[0] == "goto":
                    id = int(inputarg[1])
                    break
                else:
                    print("Invalid input! Please try again.")
        else:
            out = debugger(cmd)
            if out[0] == 0:
                print("Exception detected at command {} !\n\nException is: {}".format(id, out[1]))
                run = 0
            id += 1
        isBreakpointHit = 0
    print("Debugging complete.")

if __name__ == "__main__":
    main()
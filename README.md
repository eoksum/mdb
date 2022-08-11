# mdb
Minecraft Functions Debugger *(mdb)*

A tool which is for debugging Minecraft datapack functions in Minecraft: Java Edition. It is tested on version 1.19 successfully and probably be fully compatible with the upcoming releases.
I've developed this tool because there were no easy way to debug which command is failing in a .mcfunction file. This tool loads MCFUNCTION files and can execute commands one-by-one, letting you know which command fails. It is very useful if you're dealing with a function file that has 25000 Minecraft commands in it.

Dependencies:
Pymchat - It is used to interact with Minecraft: Java Edition client from Python backend.

*INSTALLATION STEPS:*

1-) To run mdb, you need to download and install Python 3 first. You can get it from <a href="https://www.python.org/downloads/">here</a>
2-) Once you install Python 3 to your computer, you need to install pymchat. To do that, open up Command Prompt on Windows, Terminal on Linux and type this:
pip3 install pymchat

It should download Pymchat dependency for mdb.

3-) Now, download mdb from GitHub. You can Download as ZIP or Git clone repository if you have Git installed.
Example: git clone https://github.com/eoksum/mdb

4-) Start Minecraft: Java Edition

5-) Fire up mdb
Windows: py mdb.py
Linux: python3 mdb.py

6-) Enjoy mdb!

*MDB BASICS*

- Hitting a breakpoint will automatically remove it
- run command will keep execution until it hits a exception and can still execute after hitting one
- Exception detection is based from Minecraft outputs. If mdb fails to detect a exception, create a issue

*MDB COMMANDS*

hop      - Step 1 command further
+break 2 - Add a breakpoint to line 2
-break 2 - Remove the breakpoint at line 2
?break   - Display all current breakpoints
run      - Execute the function until it hits a exception
goto 2   - Go to line 2
quit     - Quit mdb
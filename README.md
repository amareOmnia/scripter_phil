# scripter_phil
Generates script snippets onto the OSX clipboard, from any template

Python scripts ask for a variable name and template file. Simple find/replace command splices the new variable to all found placeholders. Placeholder and other options available in config.py

Script is still reliant on a local install of Python3 and a few dependencies... though you should already have these anyways

# Installation
Required Installs:
 - Python 3.7+
    - `brew install python3`
 - Tkinter
    - `pip3 install tkinter`
 - Pyperclip
    - `pip3 install pyperclip` <br> <br>
 
 <p><code>build.command</code> file is included for quick terminal usage, though permissions need to be granted for that file. <br>
To allow executing permissions of a single file: <code>chmod u+x /path/to/build.command</code> </p>

# Usage
You can either run the main script via terminal command `python3 /path/to/main.py` or double-click the `build.command` file. Results are identical.

1. The console will ask for the class/variable name you want to add. Extra spaces are stripped <br>
2. Pick the template to edit (non-destructively)<br>
3. If you use build.command, the terminal window will close automatically when completed<br>

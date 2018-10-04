# scripter_phil
Generates script snippets onto the OSX clipboard, from any template

<span>Python scripts ask for variable name/s and template file. 
Simple find/replace command splices the new variable/s to all found placeholders. 
Placeholder default and other options available in config.py. 
Generates unlimited number of ascending placeholders, 
based on the default name & quantity of arguments, 
and checks the template file for them. Finally, it copies to clipboard and asks to save file to mounted disk image.</span>

# Installation
<span>Script is still reliant on a local install 
of Python3 and a few dependencies... they are 
either installed to Python by default, or 
included in /dependencies</span> 

Required before use:
 - Python 3.7+
    - `brew install python3` <br> <br>
 
 <p><code>build.command</code> file is included for quick terminal usage, though permissions need to be granted for that file. <br>
To allow executing permissions of a single file: <br><code>chmod u+x /path/to/build.command</code> </p>

# Usage
You can either run the main script via terminal command `python3 /path/to/main.py` or double-click the `build.command` file. Results are identical.

1. The console will ask for the class/variable name you want to add. Extra spaces are stripped <br>
2. Pick the template to edit (non-destructively)<br>
3. If you use build.command, the terminal window will close automatically when completed<br>

# Upcoming additions
Listed by priority, striked when completed:
1. <strike>Allow for multiple variable arguments, with config.py defining multiple placeholders</strike>
2. <strike>Remove/hide Tk window during file selection</strike>
3. allow for settings/args at beginning of templates
4. <strike>Give dialogue warning before closing if placeholder is not found in file</strike>
5. turn config file into class, so placeholder can be changed if only variable is provided
6. create settings.config where config class grabs text
7. Create self-contained executable
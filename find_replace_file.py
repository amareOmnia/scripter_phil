from tkinter import filedialog as filer
from tkinter import *
import pyperclip


def prompt_name():
    var = input("Desired class name:").strip()
    return var


def prompt_file():
    # request file location
    file_import = Tk()
    file_import.filename = filer.askopenfilename(initialdir="/data", title="Select template\n")
    # write file to string
    with open(file_import.filename, 'r') as t:
        template = t.read().strip()
    return template


def replace_variable(template, var, placeholder):
    output = template.replace(placeholder, var)
    return output


def clipboard(output):
    pyperclip.copy(output)
    print('Successfully processed :)')
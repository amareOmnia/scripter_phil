from tkinter import filedialog as filer
from tkinter import *
import tkinter.messagebox
import pyperclip
import sys


def prompt_name():
    var = input("Desired class/variable name:").strip()
    return var


def prompt_file():

    # request file location
    file_import = Tk()
    file_import.withdraw()
    file_import.filename = filer.askopenfilename(initialdir="/data", title="Select template\n")

    # checks for empty file
    try:
        open(file_import.filename, 'r')
    except (FileNotFoundError):
        tkinter.messagebox.showinfo("Error", "File is empty/No file selected")
        sys.exit()

    # write file to string
    with open(file_import.filename, 'r') as t:
        template = t.read().strip()
    return template


def replace_variable(template, var, placeholder):
    if template.find(placeholder) == -1:
        tkinter.messagebox.showinfo("Error", "No placeholders found")
        sys.exit()
    output = template.replace(placeholder, var)
    return output


def clipboard(output):
    pyperclip.copy(output)
    print('Successfully processed :)')
from tkinter import filedialog as filer
from tkinter import *
import tkinter.messagebox as popup
from dependencies import pyperclip
import sys
from arg_lists import ArgLists as Arg

def prompt_name():
    var = input("List desired class/variable names, separated by commas (no spaces):").strip()
    return var


def split_variables(v):
    print("rendering chunk/s")
    var_list = v.split(",")
    # if len(var_list) == 1:
    #     return v
    print(var_list)
    return var_list


def determine_list(split_vars):
    try:
        split_vars.copy()
    except AttributeError:
        single = [split_vars]
        print('single variable detected: ', single)
        return single
    plc_list = Arg(len(split_vars))
    return plc_list


def prompt_file():
    # request file location
    file_import = Tk()
    file_import.withdraw()
    file_import.filename = filer.askopenfilename(initialdir="/data", title="Select template\n")

    # checks for empty file
    try:
        open(file_import.filename, 'r')
    except FileNotFoundError:
        popup.showinfo("Error", "File is empty/No file selected")
        sys.exit()
    # write file to string
    with open(file_import.filename, 'r') as t:
        template = t.read().strip()
    return template


def replace_variable(template, variables, placeholders):
    # if no placeholder exists in file, throw error
    # print(placeholders)
    if template.find(placeholders[0]) == -1:
        popup.showinfo("Error", "No placeholder found. Config and template have mismatched names")
        sys.exit()

    # replace placeholders with corresponding variables
    index = 0
    output = template
    while index <= (len(placeholders)-1):
        print('replacing...')
        output = output.replace(placeholders[index], variables[index])
        index += 1
    return output


def prompt_export():
    root = Tk()
    root.withdraw()
    mount = popup.askyesno("Export to Disk",
                           "Script saved to clipboard. Export file to Dump?")
    root.update()
    return mount


def prompt_filename():
    return input("Name the export file: ").strip(), ("." + input("File type: .").strip())


def clipboard(output):
    pyperclip.copy(output)
    print('Successfully copied!')

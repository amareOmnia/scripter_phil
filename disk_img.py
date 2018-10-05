import os
from config import Config
import subprocess
import find_replace_file as file
config = Config()


def mount_disk():
    cmd = "hdiutil attach " + config.get_dmg()
    os.system(cmd)


def prompt_export(data):
    mount = file.prompt_export()
    if mount:
        mount_disk()
        name, kind = file.prompt_filename()
        full_name = os.path.normpath(name + kind)
        full_dir = os.path.join(config.get_mount(), full_name)
        new_file = open(full_dir, "w")
        new_file.write(data)
        new_file.close()
        print("File created. Opening in finder, exiting in 3 secs...")
        subprocess.call(["open", "-R", full_dir])

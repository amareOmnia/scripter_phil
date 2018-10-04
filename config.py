import os
# CONFIG OPTIONS
# the string being replaced in file (not including index numbers)
placeholder = 'VARIABLE'
# directory of DMG to mount
dmg_dir = "~/Documents/Scripts/text_dump.dmg"
mount_dir = "/volumes/dump"

# choose to ignore (harmless) MacOS warning of duplicates.
# this doesn't actually do anything yet
#       ignore_macOs_warnings = True
#       def ignore_warnings():
#       return ignore_macOs_warnings


def get_placeholder():
    return placeholder


def get_dmg():
    return dmg_dir


def get_mount():
    return os.path.normpath(mount_dir)

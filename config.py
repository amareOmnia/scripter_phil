
# CONFIG OPTIONS
# the string being replaced in file
placeholder = 'VARIABLE'
# choose to ignore (harmless) MacOS warning of duplicates.
# this doesn't actually do anything yet
ignore_macos_warnings = True


def get_placeholder():
    return placeholder


def ignore_warnings():
    return ignore_macos_warnings

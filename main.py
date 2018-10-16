import time
import find_replace_file as f
import disk_img as disk
from config import Config

settings = Config()
settings.scan_config()

# get new variable
class_name = f.prompt_name()

# isolate different variables
class_vars = f.split_variables(class_name)
# build list of placeholders, based on amount of variables
plc_list = f.determine_list(class_vars)
# get file location and convert to string
text_input = f.prompt_file()
# creates list from arg_lists
placeholders = plc_list.get_arg_list()
# replace all instances of config.placeholder with new variable
text_output = f.replace_variable(text_input, class_vars, placeholders)
# copies to clipboard
f.clipboard(text_output)
# asks about and executes file save if "yes"
disk.prompt_export(text_output)
time.sleep(3)

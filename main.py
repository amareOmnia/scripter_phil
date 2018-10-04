import find_replace_file as f
import config

# get new variable
class_name = f.prompt_name()
# get file location and convert to string
text_input = f.prompt_file()
# replace all instances of config.placeholder with new variable
text_output = f.replace_variable(text_input, class_name, config.get_placeholder())
# copies to clipboard
f.clipboard(text_output)

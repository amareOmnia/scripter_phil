import find_replace_file as f
from arg_lists import ArgLists as Arg


# get new variable
class_name = f.prompt_name()
print('provided variables: ', class_name)

# isolate different variables
class_vars = f.split_variables(class_name)
quantity = len(class_vars)
if quantity > 1:
    arguments = Arg(quantity)
else:
    arguments = [class_vars]
# print(arguments.get_arg_list())

# get file location and convert to string
text_input = f.prompt_file()

# replace all instances of config.placeholder with new variable
text_output = f.replace_variable(text_input,
                                 class_vars,
                                 arguments.get_arg_list())

# copies to clipboard
f.clipboard(text_output)

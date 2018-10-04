import config


class ArgLists:
    # arg_list = []
    var_dict = {}

    # initialization: set amount, create and enumerate list
    def __init__(self, quantity):
        self.quantity = quantity
        self.arg_list = []
        self.set_arg_list()

    # builds array of {placeholder+index} based on quantity in the init
    def set_arg_list(self):
        print('building list...')
        placeholder = str(config.placeholder)
        self.arg_list = []
        i = 1
        while i <= self.quantity:
            index = str(i)
            self.arg_list.append(placeholder + index)
            i += 1
        print(config.placeholder, 'list built with ', len(self.arg_list), "variables")
        # print(self.arg_list)

    # may not be used
    def get_first_place(self):
        return self.arg_list[0]

    # returns array of placeholders
    def get_arg_list(self):
        return self.arg_list

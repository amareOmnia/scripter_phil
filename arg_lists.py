from config import Config


class ArgLists:
    # arg_list = []
    var_dict = {}

    # initialization: set amount, create and enumerate list
    def __init__(self, quantity):
        self.config = Config()
        self.quantity = quantity
        self.arg_list = [self.config.get_placeholder()]
        if quantity > 1:
            self.set_plc_list()

    # builds array of {placeholder+index} based on quantity in the init
    def set_plc_list(self):
        print('building list...')
        placeholder = str(self.config.get_placeholder())
        self.arg_list = []

        i = 1
        while i <= self.quantity:
            index = str(i)
            self.arg_list.append(placeholder + index)
            i += 1
        print(self.config.placeholder, 'list built with ', len(self.arg_list), "variables")
        # print(self.arg_list)

    # counts variable quantity and returns accurate list
    # def determine_list(self, split):

    # may not be used
    def get_first_place(self):
        return self.arg_list[0]

    # returns array of placeholders
    def get_arg_list(self):
        return self.arg_list

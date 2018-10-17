import os


class Config:
    def __init__(self):
        variables = self.scan_config()
        self.placeholder = variables['placeholder_name']
        self.dmg_dir = variables['directory_for_dmg']
        self.mount_dir = variables['directory_for_diskMount']
        self.use_args= variables['allow_file_settings']

    @staticmethod
    def scan_config():
        # open config text file, splits the lines into list
        with open("settings.config") as s:
            config_lines = s.read().strip().splitlines()

        # creates array of indexes, ready to mark which need removal
        remove_lines = []
        #
        for x in config_lines:
        # any line starting with # is removed
            if x.startswith("#"):
                remove_lines.append(config_lines.index(x))
        for y in remove_lines:
        # removes comment lines and changes index of removal line numbers
            del config_lines[int(y)]
            for q in remove_lines:
                remove_lines[remove_lines.index(q)] = q-1
        variables = dict()
        for z in config_lines:
            variables[z[0:z.find(" ")]] = z[(z.find(" ")+3):len(z)]
        return variables

    def get_arg_usage(self):
        return self.use_args

    def get_placeholder(self):
        return self.placeholder

    def get_dmg(self):
        return self.dmg_dir

    def get_mount(self):
        return os.path.normpath(self.mount_dir)

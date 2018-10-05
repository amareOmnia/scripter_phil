import os


class Config:
    def __init__(self):
        variables = self.scan_config()
        self.placeholder = variables['placeholder_name']
        self.dmg_dir = variables['directory_for_dmg']
        self.mount_dir = variables['directory_for_diskMount']

    @staticmethod
    def scan_config():
        with open("settings.config") as s:
            raw_settings = s.read().strip()
            config_lines = raw_settings.splitlines()
        remove_lines = []
        for x in config_lines:
            if x.startswith("#"):
                remove_lines.append(config_lines.index(x))
        for y in remove_lines:
            del config_lines[int(y)]
            for q in remove_lines:
                remove_lines[remove_lines.index(q)] = q-1
        variables = dict()
        for z in config_lines:
            variables[z[0:z.find(" ")]] = z[(z.find(" ")+3):len(z)]
        print(variables)
        return variables

    def get_placeholder(self):
        return self.placeholder

    def get_dmg(self):
        return self.dmg_dir

    def get_mount(self):
        return os.path.normpath(self.mount_dir)

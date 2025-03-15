class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent

    def get_var(self, name):
        return self.vars.get(name)

    def set_var(self, name, value):
        self.vars[name] = value

    def new_env(self):
        """Return new environment with self as parent"""
        return Environment(parent=self)
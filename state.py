# noinspection PyMethodFirstArgAssignment
class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.funcs = {}
        self.parent = parent

    def get_var(self, name):
        '''
        Search the current environment and all parent environments for a variable name (return None if we dont find any)
        '''
        while self:
            value = self.vars.get(name)
            if value is not None:
                return value
            else:
                self = self.parent  # Look in parent environments to see if variable is defined "above"
        return None

    # noinspection PyMethodFirstArgAssignment
    def set_var(self, name, value):
        '''
        Store a value in the environment (dynamically updating an existing name or creating a new entry in the dictionary)
        '''
        original_env = self
        while self:
            if name in self.vars:
                self.vars[name] = value
                return value
            self = self.parent
        # If we did not find the variable in the environments above, we create it in the original one
        original_env.vars[name] = value

    def get_func(self, name):
        pass

    def set_func(self, name, value):
        pass

    def new_env(self):
        """Return new environment with self as parent"""
        return Environment(parent=self)
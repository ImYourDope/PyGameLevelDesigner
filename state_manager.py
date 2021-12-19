class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.instance.__dict__['dom'] = {}
            cls.instance.__dict__['state'] = {}

            cls.instance.__dict__['data'] = {
                'object_in_focus': None
            }
        return cls.instance


class StateManager(Singleton):
    def __init_attr(self, key):
        self.state[key] = {}
        self.state[key]['callbacks'] = []

    def get(self, key):
        if key not in self.state:
            return None
        return self.state[key]['value']

    def set(self, key, value):
        if key not in self.state:
            self.__init_attr(key)

        self.state[key]['value'] = value

        for callback in self.state[key]['callbacks']:
            callback(value)

    def onchange(self, key, callback):
        if key not in self.state:
            self.__init_attr(key)

        self.state[key]['callbacks'].append(callback)

    def remove_callbacks(self, key):
        self.state[key]['callbacks'] = []


state_manager = StateManager()
state_manager.set('project created', False)
state_manager.set('project name', '')
state_manager.set('main_on', False)


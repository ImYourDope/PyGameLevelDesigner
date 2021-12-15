class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.instance.__dict__['dom'] = {}
            cls.instance.__dict__['dom_elements'] = {}

            cls.instance.__dict__['data'] = {
                'object_in_focus': None
            }
        return cls.instance


class StateManager(Singleton):
    def __init_attr(self, key):
        self.dom_elements[key] = {}
        self.dom_elements[key]['callbacks'] = []

    def __getattr__(self, key):
        if key not in self.dom_elements:
            return None
        return self.dom_elements[key]['value']

    def __setattr__(self, key, value):
        if key not in self.dom_elements:
            self.__init_attr(key)

        self.dom_elements[key]['value'] = value

        for callback in self.dom_elements[key]['callbacks']:
            callback(value)

    def onchange(self, key, callback):
        if key not in self.dom_elements:
            self.__init_attr(key)

        self.dom_elements[key]['callbacks'].append(callback)

    def remove_callbacks(self, key):
        self.dom_elements[key]['callbacks'] = []


state_manager = StateManager()
state_manager.project_created = False
state_manager.project_name = ''


class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.instance.__dict__['data'] = {}
        return cls.instance


class EventManager(Singleton):
    def __init_attr(self, key):
        self.data[key] = {}
        self.data[key]['callbacks'] = []

    def __getattr__(self, key):
        if key not in self.data:
            return None
        return self.data[key]['value']

    def __setattr__(self, key, value):
        if key not in self.data:
            self.__init_attr(key)

        self.data[key]['value'] = value

        for callback in self.data[key]['callbacks']:
            callback(value)

    def onchange(self, key, callback):
        if key not in self.data:
            self.__init_attr(key)

        self.data[key]['callbacks'].append(callback)

    def remove_callbacks(self, key):
        self.data[key]['callbacks'] = []


event_manager = EventManager()





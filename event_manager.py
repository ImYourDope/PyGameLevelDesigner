class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class EventManager(Singleton):
    def __init_attr(self, key):
        self.__dict__[key] = {}
        self.__dict__[key]['callbacks'] = []

    def __getattr__(self, key):
        return self.__dict__[key]['value']

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__init_attr(key)

        self.__dict__[key]['value'] = value

        for callback in self.__dict__[key]['callbacks']:
            callback(value)

    def onchange(self, key, callback):
        if key not in self.__dict__:
            self.__init_attr(key)

        self.__dict__[key]['callbacks'].append(callback)


def onchange_i(new_value):
    print('State var i changed. New value is:', new_value)


state = EventManager()
state.onchange('i', onchange_i)
state.i = 10
state.i = 20






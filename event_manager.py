import pygame


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


class DOMEventElement:
    def __init__(self, elem, props=None):
        if props is None:
            self.props = {'hover': False, 'focus': False}
        else:
            self.props = props

        self.id = elem.id
        self.elem = elem

        self.callbacks = {
            'click': [],
            'hover': [],
            'input': [],
            'focus': [],
            'unfocus': [],
            'change': []
        }

    def on(self, action, callback):
        self.callbacks[action].append(callback)

    def onclick(self, callback):
        self.on('click', callback)

    def onhover(self, callback):
        self.on('hover', callback)

    def oninput(self, callback):
        self.on('input', callback)

    def onfocus(self, callback):
        self.on('focus', callback)

    def onunfocus(self, callback):
        self.on('unfocus', callback)

    def onchange(self, callback):
        self.on('change', callback)

    def draw(self, screen):
        self.elem.draw(screen)

    def mouse_collision(self, cors):
        return self.elem.mouse_collision(cors)

    def process_event(self, event_name, event={}):
        if event_name == 'click':
            self.elem.onclick(event)
        elif event_name == 'hover':
            self.elem.onhover(event)
        elif event_name == 'input':
            self.elem.oninput(event)
        elif event_name == 'focus':
            self.elem.onfocus(event)
        elif event_name == 'unfocus':
            self.elem.onunfocus(event)

        for callback in self.callbacks[event_name]:
            callback(event)

        for callback in self.callbacks['change']:
            callback(event)



class EventManager(Singleton):
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


event_manager = EventManager()

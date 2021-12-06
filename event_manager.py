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


class DOMEventManager(Singleton):
    def init_dom(self, dom):
        for elem in dom:
            self.dom[elem.id] = DOMEventElement(elem)

    def on(self, action, id, callback):
        if id not in self.dom:
            raise Exception('Incorrect ID')
        self.dom[id].on(action, callback)

    def onclick(self, id, callback):
        self.on('click', id, callback)

    def onhover(self, id, callback):
        self.on('hover', id, callback)

    def oninput(self, id, callback):
        self.on('input', id, callback)

    def onchange(self, id, callback):
        self.on('change', id, callback)

    def infocus(self, id):
        return self.data['object_in_focus'] == id

    def ishovered(self, id):
        return self.dom[id].props['hover']

    def elem_collision(self, id, cors):
        return self.dom[id].mouse_collision(cors)

    def change_focus(self, new_focus):
        old_focus = self.data['object_in_focus']
        self.data['object_in_focus'] = new_focus

        if old_focus is not None:
            prev = self.dom[old_focus]
            prev.process_event('unfocus')

        if new_focus is not None:
            next = self.dom[new_focus]
            next.process_event('focus')

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.data['object_in_focus'] is not None:
                self.dom[self.data['object_in_focus']].process_event('input', event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for _, elem in self.dom.items():
                if elem.mouse_collision(pygame.mouse.get_pos()):
                    elem.process_event('click', event)
                    self.change_focus(elem.id)
                    break
            else:
                self.change_focus(None)
        elif event.type == pygame.MOUSEMOTION:
            for _, elem in self.dom.items():
                if elem.mouse_collision(pygame.mouse.get_pos()):
                    elem.props['hover'] = True
                    elem.process_event('hover', event)
                else:
                    elem.props['hover'] = False


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
dom_event_manager = DOMEventManager()

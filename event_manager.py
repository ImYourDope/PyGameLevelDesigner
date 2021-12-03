import pygame


class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.instance.__dict__['dom_elements'] = {}
            cls.instance.__dict__['data'] = {}
        return cls.instance


class DOMEventManager(Singleton):
    def init_dom(self, dom):
        for elem in dom:
            self.__init_attr(elem.id)
            self.dom_elements[elem.id]['elem'] = elem
            self.dom_elements[elem.id]['props'] = {
                'hover': False,
                'focus': False
            }

    def __init_attr(self, id):
        self.dom_elements[id] = {}
        self.dom_elements[id]['props'] = {}
        self.dom_elements[id]['click'] = []
        self.dom_elements[id]['hover'] = []
        self.dom_elements[id]['input'] = []
        self.dom_elements[id]['change'] = []

    # def __getattr__(self, id):
    #     if id not in self.dom_elements:
    #         return None
    #     return self.dom_elements[id]['elem']

    def on(self, action, id, callback):
        if id not in self.dom_elements:
            self.__init_attr(id)
        self.dom_elements[id][action].append(callback)

    def onclick(self, id, callback):
        self.on('click', id, callback)

    def onhover(self, id, callback):
        self.on('hover', id, callback)

    def onchange(self, id, callback):
        self.on('change', id, callback)

    def infocus(self, id):
        return self.data['object_in_focus'] == id

    def ishovered(self, id):
        return self.dom_elements[id]['props']['hover']

    def _callback(self, id, event_name, event):
        for callback in self.dom_elements[id][event_name]:
            callback(event)

    def elem_collision(self, id, cors):
        return self.dom_elements[id]['elem'].mouse_collision(cors)


    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.dom_elements[self.data['object_in_focus']]['elem'].oninput(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for id in self.dom_elements.keys():
                if self.elem_collision(id, pygame.mouse.get_pos()):
                    self.data['object_in_focus'] = id

                    self.dom_elements[id]['elem'].onclick(event)
                    self._callback(id, 'click', event)
        elif event.type == pygame.MOUSEMOTION:
            for id in self.dom_elements.keys():
                if self.elem_collision(id, pygame.mouse.get_pos()):
                    self.dom_elements[id]['props']['hover'] = True

                    self.dom_elements[id]['elem'].onhover(event)
                    self._callback(id, 'hover', event)
                else:
                    self.dom_elements[id]['props']['hover'] = False






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

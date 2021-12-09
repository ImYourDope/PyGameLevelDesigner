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


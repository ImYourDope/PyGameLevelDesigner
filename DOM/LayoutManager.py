from EventManager import Singleton


class LayoutManager(Singleton):
    layouts = []

    def push(self, layout):
        if self.last() is not None:
            self.last().disable()
        layout.init({})
        self.layouts.append(layout)

    def pop(self):
        layout = self.layouts.pop()
        layout.delete()

    def last(self):
        if len(self.layouts) > 0:
            return self.layouts[len(self.layouts) - 1]
        return None

    def cors_to_relative_pos(self, cors):
        new_cors = [*cors]
        for layout in self.layouts:
            new_cors[0] -= layout.properties['x']
            new_cors[1] -= layout.properties['y']
        return new_cors

    def process_event(self, event):
        self.last().process_event(event)

    def infocus(self, id):
        return self.last().infocus(id)

    def ishovered(self, id):
        return self.last().ishovered(id)

    def draw(self, screen):
        for layout in self.layouts:
            layout.draw(screen)


layout_manager = LayoutManager()

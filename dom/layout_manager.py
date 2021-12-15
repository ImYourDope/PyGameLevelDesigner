from state_manager import Singleton


class LayoutManager(Singleton):
    layouts = []

    def push(self, layout):
        if self.last() is not None:
            print(self.last())
            self.last().disable()
        self.layouts.append(layout)
        layout.init({})

    def pop(self):
        layout = self.layouts.pop()
        layout.delete()

    def last(self):
        if len(self.layouts) > 0:
            return self.layouts[len(self.layouts) - 1]
        return None

    def absolute_pos_to_relative_pos(self, pos):
        new_pos = [*pos]
        for layout in self.layouts:
            new_pos[0] -= layout.properties['x']
            new_pos[1] -= layout.properties['y']
        return new_pos

    def process_event(self, event):
        self.last().process_event(event)

    def infocus(self, element_id):
        return self.last().infocus(element_id)

    def ishovered(self, element_id):
        return self.last().ishovered(element_id)

    def draw(self, screen):
        for layout in self.layouts:
            layout.draw(screen)


layout_manager = LayoutManager()

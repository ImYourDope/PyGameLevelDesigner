from .button import Button


class Toggle(Button):
    def __init__(self, properties):
        super().__init__(properties)
        self.pressed = False

    def draw(self, screen):
        if not self.pressed:
            screen.blit(self.surface, (self.pos[0], self.pos[1]))
        else:
            screen.blit(self.surface, (self.shift_pos[0], self.shift_pos[1]))

    def onclick(self, e):
        self.pressed = not self.pressed

class Tile:
    def __init__(self, image, pos, name=''):
        self.image = image
        self.pos = pos
        self.name = ''

    def mouse_collision(self, pos):
        return self.image.get_rect(topleft=self.pos).collidepoint(pos)

    def draw(self, screen):
        screen.blit(self.image, self.pos)

class Tile:
    def __init__(self, image, pos):
        self.image = image
        self.pos = pos

    def mouse_collision(self, pos):
        return self.image.get_rect(topleft=self.pos).collidespoint(pos)

    def draw(self, screen):
        screen.blit(self.image, self.pos)

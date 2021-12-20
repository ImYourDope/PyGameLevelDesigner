class Tile:
    def __init__(self, image, pos, name=''):
        self.image = image
        self.pos = pos
        self.name = name

    def mouse_collision(self, pos):
        """Checks mouse collision with tiles."""
        return self.image.get_rect(topleft=self.pos).collidepoint(pos)

    def draw(self, screen):
        """Draws the tile."""
        screen.blit(self.image, self.pos)

from settings import *


class Grid:
    def __init__(self, tile_width, tile_height):
        self.tile_size = (tile_width, tile_height)
        self.size = (tile_width * tile_size, tile_height * tile_size)

        self.grid = pygame.Surface(self.size)

    def grid_pos(self, pos):
        return (pos[0] - pos[0] % tile_size + grid_thickness,
                pos[1] - pos[1] % tile_size + grid_thickness)

    def draw(self, screen, pos, mouse_pos=None, mouse_tile=None):
        self.grid.fill(grid_colorkey)
        for column in range(0, self.tile_size[0] + 1):
            pygame.draw.line(self.grid, grid_color, (column * tile_size, 0), (column * tile_size, self.size[1]),
                             grid_thickness)
        for row in range(0, self.tile_size[1] + 1):
            pygame.draw.line(self.grid, grid_color, (0, row * tile_size), (self.size[0], row * tile_size),
                             grid_thickness)
        if mouse_pos is not None:
            if mouse_tile is not None :
                self.grid.blit(mouse_tile, self.grid_pos(mouse_pos))
            else:
                pygame.draw.rect(self.grid, 'black', (self.grid_pos(mouse_pos), (tile_size - grid_thickness, tile_size - grid_thickness)))

        self.grid.set_colorkey(grid_colorkey)
        screen.blit(self.grid, (pos[0] - 1, pos[1] - 1))

    @staticmethod
    def toggle_grid(_):
        state_manager.set('grid on', not state_manager.get('grid on'))

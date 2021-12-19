from enum import Enum

from interface import Grid
from settings import *
from tile import Tile

right_arrow_cursor = None
left_arrow_cursor = None
top_arrow_cursor = None
bottom_arrow_cursor = None


class MouseScroll(Enum):
    Up = 0,
    Down = 1,
    Right = 2,
    Left = 3,
    No = 4


def create_scrolling_cursors():
    global right_arrow_cursor, left_arrow_cursor, top_arrow_cursor, bottom_arrow_cursor
    arrow_cursor = pygame.image.load('arrow_cursor.png').convert_alpha()
    arrow_cursor = pygame.transform.scale(arrow_cursor, (arrow_cursor_size, arrow_cursor_size))
    right_arrow_cursor = pygame.transform.rotate(arrow_cursor, 180)
    left_arrow_cursor = pygame.transform.rotate(arrow_cursor, 0)
    top_arrow_cursor = pygame.transform.rotate(arrow_cursor, -90)
    bottom_arrow_cursor = pygame.transform.rotate(arrow_cursor, 90)


def switch_canvas():
    a = state_manager.get('active_canvas')
    state_manager.get('inactive_canvas').pos = state_manager.get('active_canvas').pos
    state_manager.set('active_canvas', state_manager.get('inactive_canvas'))
    state_manager.set('inactive_canvas', a)
    state_manager.set('main_on', not state_manager.get('main_on'))


class Canvas:
    def __init__(self, screen, width_in_tiles, height_in_tiles):
        self.screen = screen
        self.pos = [left_margin, 0]
        self.width_in_tiles = width_in_tiles
        self.height_in_tiles = height_in_tiles
        self.width = self.width_in_tiles * tile_size + grid_thickness
        self.height = self.height_in_tiles * tile_size + grid_thickness
        self.canvas = pygame.Surface((self.width, self.height))
        self.canvas.fill(canvas_default_color)

        self.tiles = []
        self.grid = Grid(width_in_tiles, height_in_tiles)

    def relative_pos(self, pos):
        return (
            pos[0] - self.pos[0],
            pos[1] - self.pos[1]
        )

    def process_tile(self):
        tile = state_manager.get('DOM tile list').elem.selected_tile()
        mouse_pos = self.relative_pos(pygame.mouse.get_pos())
        tile_pos = (mouse_pos[0] - tile_size / 2, mouse_pos[1] - tile_size / 2)

        if state_manager.get('grid on'):
            tile_pos = Grid.tile_pos(mouse_pos)
        return tile, tile_pos

    def draw(self):
        self.canvas.fill(canvas_default_color)

        for tile in self.tiles:
            tile.draw(self.canvas)

        tile, tile_pos = self.process_tile()

        if tile is not None and self.get_scroll(pygame.mouse.get_pos()) == MouseScroll.No:
            self.canvas.blit(tile, tile_pos)

        if state_manager.get('grid on'):
            self.grid.draw(self.canvas)
        self.screen.blit(self.canvas, self.pos)

    def get_scroll(self, pos):
        if top_scrolling_rect.collidepoint(pos) and \
                self.pos[1] < editing_screen_rect.top + void_margin:
            return MouseScroll.Up
        if bottom_scrolling_rect.collidepoint(pos) and \
                self.pos[1] + self.height + void_margin > editing_screen_rect.bottom:
            return MouseScroll.Down

        if right_scrolling_rect.collidepoint(pos) and \
                self.pos[0] + self.width + void_margin > editing_screen_rect.right:
            return MouseScroll.Right

        if left_scrolling_rect.collidepoint(pos) and \
                self.pos[0] < editing_screen_rect.left + void_margin:
            return MouseScroll.Left

        return MouseScroll.No

    def scroll(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return
        if not pygame.mouse.get_pressed()[0]:
            return

        move = self.get_scroll(pygame.mouse.get_pos())
        if move == MouseScroll.Up:
            self.pos[1] += tile_size
        elif move == MouseScroll.Down:
            self.pos[1] -= tile_size
        elif move == MouseScroll.Right:
            self.pos[0] -= tile_size
        elif move == MouseScroll.Left:
            self.pos[0] += tile_size

    def draw_scrolling_cursor(self):
        move = self.get_scroll(pygame.mouse.get_pos())
        if move == MouseScroll.Up:
            self.screen.blit(top_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                                pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
        elif move == MouseScroll.Down:
            self.screen.blit(bottom_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                                   pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
        elif move == MouseScroll.Left:
            self.screen.blit(left_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                                 pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
        elif move == MouseScroll.Right:
            self.screen.blit(right_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                                  pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
        if move != MouseScroll.No:
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)

    def expand(self, left_in_tiles, right_in_tiles, top_in_tiles, bottom_in_tiles):
        left = left_in_tiles * tile_size
        right = right_in_tiles * tile_size
        top = top_in_tiles * tile_size
        bottom = bottom_in_tiles * tile_size
        self.height += top + bottom
        self.width += left + right
        canvas_new = pygame.Surface((self.width, self.height))
        canvas_new.fill(canvas_default_color)
        self.pos = [self.pos[0] - left, self.pos[1] - top]
        if top < 0:
            self.canvas = self.canvas.subsurface((0, -top, self.canvas.get_width(), self.canvas.get_height() + top))
            top = 0
        if bottom < 0:
            self.canvas = self.canvas.subsurface((0, 0, self.canvas.get_width(), self.canvas.get_height() + bottom))
        if left < 0:
            self.canvas = self.canvas.subsurface((-left, 0, self.canvas.get_width() + left, self.canvas.get_height()))
            left = 0
        if right < 0:
            self.canvas = self.canvas.subsurface((0, 0, self.canvas.get_width() + right, self.canvas.get_height()))
        canvas_new.blit(self.canvas, (left, top))
        self.canvas = canvas_new
        self.height = self.canvas.get_height()
        self.width = self.canvas.get_width()
        self.height_in_tiles = self.height // tile_size
        self.width_in_tiles = self.width // tile_size

    def onclick(self, event):
        del_tile = None
        tile, tile_pos = self.process_tile()
        if event.button == 1:
            print('no')
            if tile is not None:
                self.tiles.append(Tile(tile, tile_pos))
        elif event.button == 3:
            print('yes')
            for i in reversed(self.tiles):
                if tile.get_rect().collidepoint(self.relative_pos(pygame.mouse.get_pos())):
                    tile.get_rect().collidepoint(self.relative_pos(pygame.mouse.get_pos()))
                    if del_tile is None:
                        del_tile = len(self.tiles) - i - 1
                        break
            if del_tile is not None:
                self.tiles.pop(del_tile)

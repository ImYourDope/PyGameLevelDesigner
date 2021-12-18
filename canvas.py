from interface import Grid
from settings import *

right_arrow_cursor = None
left_arrow_cursor = None
top_arrow_cursor = None
bottom_arrow_cursor = None


def create_scrolling_cursors():
    global right_arrow_cursor, left_arrow_cursor, top_arrow_cursor, bottom_arrow_cursor
    arrow_cursor = pygame.image.load('arrow_cursor.png').convert_alpha()
    arrow_cursor = pygame.transform.scale(arrow_cursor, (arrow_cursor_size, arrow_cursor_size))
    right_arrow_cursor = pygame.transform.rotate(arrow_cursor, 180)
    left_arrow_cursor = pygame.transform.rotate(arrow_cursor, 0)
    top_arrow_cursor = pygame.transform.rotate(arrow_cursor, -90)
    bottom_arrow_cursor = pygame.transform.rotate(arrow_cursor, 90)


class Canvas:
    def __init__(self, screen, width_in_tiles, height_in_tiles):
        self.screen = screen
        self.pos = [left_margin, 0]
        self.width_in_tiles = width_in_tiles
        self.height_in_tiles = height_in_tiles
        self.width = self.width_in_tiles * tile_size
        self.height = self.height_in_tiles * tile_size
        self.canvas = pygame.Surface((self.width, self.height))
        self.canvas.fill(canvas_default_color)

        self.grid = Grid(width_in_tiles, height_in_tiles)
    def relative_pos(self, pos):
        return (
            pos[0] - self.pos[0],
            pos[1] - self.pos[1]
        )
    def draw(self):
        self.canvas.fill(canvas_default_color)
        self.grid.draw(self.canvas, (0, 0), self.relative_pos(pygame.mouse.get_pos()), state_manager.get('DOM tile list').elem.selected_tile())
        self.screen.blit(self.canvas, self.pos)


    def scroll(self, event):
        if top_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
                self.pos[1] < editing_screen_rect.top + void_margin:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.pos[1] += tile_size

        if bottom_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
                self.pos[1] + self.height + void_margin > editing_screen_rect.bottom:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.pos[1] -= tile_size

        if right_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
                self.pos[0] + self.width + void_margin > editing_screen_rect.right:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.pos[0] -= tile_size

        if left_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
                self.pos[0] < editing_screen_rect.left + void_margin:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.pos[0] += tile_size

    def draw_scrolling_cursor(self):
        if top_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
                self.pos[1] < editing_screen_rect.top + void_margin:
            pygame.mouse.set_visible(False)
            self.screen.blit(top_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                                pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
        elif bottom_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
                self.pos[1] + self.height + void_margin > editing_screen_rect.bottom:
            pygame.mouse.set_visible(False)
            self.screen.blit(bottom_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                                   pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
        elif left_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
                self.pos[0] < editing_screen_rect.left + void_margin:
            pygame.mouse.set_visible(False)
            self.screen.blit(left_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                                 pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
        elif right_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
                self.pos[0] + self.width + void_margin > editing_screen_rect.right:
            pygame.mouse.set_visible(False)
            self.screen.blit(right_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                                  pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
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
        self.height_in_tiles = self.height//tile_size
        self.width_in_tiles = self.width//tile_size

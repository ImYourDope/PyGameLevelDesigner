from userinput import *
from settings import *

canvas = pygame.Surface((canvas_width, canvas_height))
canvas.fill(canvas_default_color)
pygame.draw.rect(canvas, 'black', (tile_size * 4, tile_size * 4, tile_size, tile_size))
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


def draw_canvas(screen):
    screen.blit(canvas, (canvas_pos[0], canvas_pos[1]))


def scroll_canvas(event):
    if top_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
            canvas_pos[1] < editing_screen_rect.top + void_margin:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                canvas_pos[1] += tile_size

    if bottom_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
            canvas_pos[1] + canvas_height + void_margin > editing_screen_rect.bottom:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                canvas_pos[1] -= tile_size

    if right_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
            canvas_pos[0] + canvas_width + void_margin > editing_screen_rect.right:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                canvas_pos[0] -= tile_size

    if left_scrolling_rect.collidepoint(pygame.mouse.get_pos()) and \
            canvas_pos[0] < editing_screen_rect.left + void_margin:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                canvas_pos[0] += tile_size


def draw_scrolling_cursor(screen):
    if top_scrolling_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_visible(False)
        screen.blit(top_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                       pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
    elif bottom_scrolling_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_visible(False)
        screen.blit(bottom_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                          pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
    elif left_scrolling_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_visible(False)
        screen.blit(left_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                        pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
    elif right_scrolling_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.mouse.set_visible(False)
        screen.blit(right_arrow_cursor, (pygame.mouse.get_pos()[0] - arrow_cursor_size / 2,
                                         pygame.mouse.get_pos()[1] - arrow_cursor_size / 2))
    else:
        pygame.mouse.set_visible(True)

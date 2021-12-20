from settings import *
import pygame


def load_spritesheet(spritesheet_file, sprite_row_color=default_sprite_row_color,
                     sprite_starting_color=default_sprite_starting_color,
                     sprite_ending_color=default_sprite_ending_color):
    """Loads spritesheet and cuts it on surfaces."""
    spritesheet = pygame.image.load(spritesheet_file).convert()
    rows = []
    spritesheet_data = []

    for y in range(spritesheet.get_height()):
        pixel_color = spritesheet.get_at((0, y))
        if pixel_color == sprite_row_color:
            rows.append(y)

    for row in rows:
        row_data = []
        for x in range(spritesheet.get_width()):
            pixel_color = spritesheet.get_at((x, row))
            if pixel_color == sprite_starting_color:
                sprite_width = 0
                sprite_height = 0
                while True:
                    sprite_width += 1
                    pixel_color = spritesheet.get_at((x + sprite_width, row))
                    if pixel_color == sprite_ending_color:
                        break
                while True:
                    sprite_height += 1
                    pixel_color = spritesheet.get_at((x, row + sprite_height))
                    if pixel_color == sprite_ending_color:
                        break

                sprite_image = spritesheet.subsurface(x+1, row+1, sprite_width-1, sprite_height-1)
                sprite_image.set_colorkey(spritesheet_colorkey_color)
                row_data.append(sprite_image)
        spritesheet_data.append(row_data)

    spritesheets = []

    for row in spritesheet_data:
        spritesheets.extend(row)
    return spritesheets

import json
import os

import pygame.image

from state_manager import state_manager


def save_sprites(sprites):
    name = 'project/sprites'
    directory = os.path.join(os.curdir, name)
    if not os.path.isdir(directory):
        os.mkdir(directory)

    result = {}

    for i in range(len(sprites)):
        filename = 'sprite{:05d}.png'.format(i)
        path = os.path.join(os.curdir, name, filename)
        pygame.image.save(sprites[i][0], path)
        result[i] = {
            'path': filename,
            'name': sprites[i][1],
        }

    return result


def dump_tiles(tiles):
    tiles_raw = []
    for tile in tiles:
        tiles_raw.append({
            'pos': tile.pos,
            'name': tile.name
        })

    return tiles_raw


def save(_):
    name = 'project'
    directory = os.path.join(os.curdir, name)
    if not os.path.isdir(directory):
        os.mkdir(directory)

    if not state_manager.get('project created'):
        print('Project does not created')
        return
    canvas = state_manager.get('active_canvas')

    sprites = state_manager.get('DOM tile list').elem.list
    tiles = canvas.tiles

    sprites_data = save_sprites(sprites)

    project = {
        'name': state_manager.get('project name'),
        'canvas': {
            'width in tiles': canvas.width_in_tiles,
            'height in tiles': canvas.height_in_tiles,
        },
        'sprites': sprites_data,
        'tiles': dump_tiles(tiles)
    }
    path = os.path.join(directory, 'project.json')
    with open(path, 'w') as f:
        json.dump(project, f)

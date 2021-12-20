import json
import os

import pygame.image

from state_manager import state_manager
from canvas import Canvas
from tile import Tile


def save_sprites(sprites):
    name = 'project/sprites'
    directory = os.path.join(os.curdir, name)
    if not os.path.isdir(directory):
        os.mkdir(directory)

    result = []

    for i in range(len(sprites)):
        filename = 'sprite{:05d}.png'.format(i)
        path = os.path.join(os.curdir, name, filename)
        pygame.image.save(sprites[i][0], path)
        result.append({
            'path': path,
            'name': sprites[i][1],
        })

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


def load(_):
    name = 'project'
    directory = os.path.join(os.curdir, name)
    json_path = os.path.join(directory, 'project.json')
    with open(json_path, 'r') as f:
        project_raw = json.load(f)

    state_manager.set('project name', project_raw['name'])
    state_manager.set('project created', True)

    sprites = []
    for sprite in project_raw['sprites']:
        name = sprite['name']
        surface = pygame.image.load(sprite['path'])
        surface.set_colorkey('white')
        sprites.append([surface, name])

    tiles = []
    for tile in project_raw['tiles']:
        image = [image for image, name in sprites if name == tile['name']][0]
        tiles.append(Tile(
            image,
            tile['pos'],
            tile['name'],
        ))

    canvas = Canvas(state_manager.get('screen'), project_raw['canvas']['width in tiles'], project_raw['canvas']['height in tiles'])
    canvas.tiles = tiles
    state_manager.set('active_canvas', canvas)
    state_manager.get('DOM tile list').elem.list = sprites
    state_manager.get('DOM tile list').elem.update_surface()

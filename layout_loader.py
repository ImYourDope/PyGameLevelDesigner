import os


def init_layouts():
    """Initializes layouts"""
    modules = list(filter(lambda path: path[0] != '_', os.listdir("./layouts")))
    loader_file = open('layouts/__init__.py', 'w')

    for module in modules[::]:
        loader_file.write(f"from .{module} import layout as {module}\n".format(module=module))

    loader_file.close()

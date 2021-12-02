from inputlineclass import *


def create_popup_screen_inputlines(screen):
    test_popup_screen_inputlines.append(InputLine(screen, (0, 100, 200, 50), inputline_vocabulary))

def create_main_screen_inputlines(screen):
    main_screen_inputlines.append(InputLine(screen, (0, 500, 200, 50), inputline_vocabulary))
    main_screen_inputlines.append(InputLine(screen, (0, 600, 200, 50), inputline_vocabulary))
    state['active_inputlines'] = main_screen_inputlines


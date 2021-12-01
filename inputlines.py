from inputlineclass import *

main_screen_inputlines = []
popup_screen_inputlines = []
active_inputlines = main_screen_inputlines
test_popup_screen_inputlines = []


def create_inputlines(screen):
    main_screen_inputlines.append(InputLine(screen, (0, 500, 200, 50), inputline_vocabulary))
    main_screen_inputlines.append(InputLine(screen, (0, 600, 200, 50), inputline_vocabulary))
    test_popup_screen_inputlines.append(InputLine(screen, (0, 100, 200, 50), inputline_vocabulary))


def update_inputlines():
    global active_inputlines
    if state['main_screen']:
        active_inputlines = main_screen_inputlines
    elif state['popup_screen']:
        active_inputlines = popup_screen_inputlines

from abc import abstractmethod


class ElementInterface:
    @abstractmethod
    def mouse_collision(self, pos):
        """True if mouse inside object, False elsewhere"""

    def onclick(self, event):
        """Processes click on self"""

    def onhover(self, event):
        """Processes mouse hovering on self"""

    def oninput(self, event):
        """Processes input"""

    def onscroll(self, event):
        """Processes scroll event"""

    def onfocus(self, event):
        """Processes hover event"""

    def onunfocus(self, event):
        """Processes unfocus event"""

    def draw(self, screen):
        """Draws self on screen"""

    def __getattribute__(self, item):
        # print('Trying to get {0} from {1}'.format(item, self))
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        print('Trying to set {0} = {1} in {2}'.format(key, value, self.__dict__))
        return super().__setattr__(key, value)

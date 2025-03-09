import pyxel
from project_types import MyCircle, MyRectangle, UpdateHandler, DrawHandler


class View:
    def __init__(self, screen_height: int, screen_width: int):
        self._height = screen_height
        self._width = screen_width

    def start(self, updater: UpdateHandler, drawer: DrawHandler):
        # rely on abstractions to prevent circular imports
        pyxel.init(self._width, self._height)
        pyxel.run(updater.update, drawer.draw)

    def clear_screen(self):
        pyxel.cls(0)

    def draw_ball(self, c: MyCircle):
        x = c.x
        y = c.y
        radius = c.radius
        col = c.color
        pyxel.circ(x, y, radius, col)

    def draw_platform(self, c: MyRectangle):
        x = c.x
        y = c.y
        width = c.wid
        height = c.height
        col = c.clr
        pyxel.rect(x, y, width, height, col)

    def was_A_pressed(self) -> bool:
        return pyxel.btn(pyxel.KEY_A)
    
    def was_D_pressed(self) -> bool:
        return pyxel.btn(pyxel.KEY_D)
    
    def was_W_pressed(self) -> bool:
        return pyxel.btn(pyxel.KEY_W)
from model import Model
from view import View

class Controller:
    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view

    def start(self):

        self._view.start(self, self)

    def update(self):
        print('i am run')
        self._model.update(self._view.was_A_pressed(),
                           self._view.was_D_pressed(),
                           self._view.was_W_pressed())
        
    def draw(self):
        self._view.clear_screen()

        self._view.draw_ball(self._model.ball)
        self._view.draw_platform(self._model.platform)
        
from model import Model
from view import View
from controller import Controller
from project_types import MyCircle, MyRectangle

def main():
    screen_height = 200
    screen_width = 200
    grav_const = 9.8 / 500

    ball = MyCircle(6, screen_width / 2, 50, 0, 0, 10)
    platform = MyRectangle(30, 5, 3, screen_width / 2, 
                           175, 3)

    model = Model(screen_height, screen_width,
                  grav_const, ball, platform)
    view = View(screen_height, screen_width)

    controller = Controller(model, view)

    controller.start()

if __name__ == '__main__':
    main()
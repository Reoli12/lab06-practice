import pyxel
import math

SCREEN_LEN = 100
SCREEN_WIDTH = 100
SCREEN_MIDDLE_X = SCREEN_LEN // 2
SCREEN_MIDDLE_Y = SCREEN_WIDTH // 2    

ACCELERATION_CONSTANT: float = (9.8) / 500

class MyRectangle:
    def __init__(self, width: float, height: float, color: int,
                x0: float, y0: float, vx: float):
        self.wid = width
        self.height = height
        self.clr = color
        self.x = x0
        self.y = y0
        self.vx = vx

    def within_top_side(self, x: float) -> bool:
        return self.x <= x <= self.x + self.wid

    def has_collided_with_side(self):
        return self.x <= 0 or self.x >= SCREEN_LEN - self.wid

    def is_inside(self, x: float) -> bool:
        return not (x <= 0 or x >= SCREEN_LEN - self.wid)

    def return_to_within_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_LEN - self.wid:
            self.x = SCREEN_LEN - self.wid

    @property 
    def bottom(self) -> float:
        return self.y + self.height

class MyCircle:
    def __init__(self, radius: float, x0: float, y0: float,
                vx: float, vy: float):
        self.radius = radius
        self.x = x0
        self.y = y0
        self.vx = vx
        self. vy = vy

    def collision_side_boundaries(self):
        return self.leftmost <= 0 or self.rightmost >= SCREEN_WIDTH

    def collision_top_boundary(self):
        return self.top <= 0

    def collision_bottom_boundary(self):
        return self.bottom >= SCREEN_LEN

    @property
    def top(self):
        return self.y - self.radius
    
    @property
    def bottom(self):
        return self.y + self.radius

    @property
    def leftmost(self):
        return self.x - self.radius

    @property
    def rightmost(self):
        return self.x + self.radius

def collision_happened(c: MyCircle, r: MyRectangle) -> bool:
    return r.y <= c.bottom < r.bottom and r.within_top_side(c.x)




def zone_collision_identifier(c: MyCircle, r: MyRectangle) -> int:
    circle_dist_from_rect_left = c.x - r.x

    zone_length = r.wid / 5

    assert circle_dist_from_rect_left >= 0

    if circle_dist_from_rect_left < zone_length:
        return 1
    elif circle_dist_from_rect_left < 2 * zone_length:
        return 2
    elif circle_dist_from_rect_left < 3 * zone_length:
        return 3
    elif circle_dist_from_rect_left < 4 * zone_length:
        return 4
    elif circle_dist_from_rect_left <= 5 * zone_length:
        return 5
    else:
        raise ValueError
    
def set_angle_trajectory(c:  MyCircle, zone: int):
    
    assert 1 <= zone <= 5
    match zone:
        case 1:
            c.vx = -1 * math.cos(math.pi / 6)
            # c.vy *= math.sin(math.pi / 6)
        case 2:
            c.vx = -1 * math.cos(math.pi / 3)
            # c.vy *= math.sin(math.pi / 3)
        case 3:
            # c.vx *= math.cos(math.pi / 2)
            # c.vy *= math.sin(math.pi / 2)
            pass
        case 4:
            c.vx = 1 * math.cos(math.pi / 3)
            # c.vy *= math.sin(math.pi / 3)
        case 5:
            c.vx = 1 * math.cos(math.pi / 6)
            # c.vy *= math.sin(math.pi / 6)
        case _:
            raise ValueError

R = MyRectangle(15, 5, 1, SCREEN_MIDDLE_X, 75, 2)
C = MyCircle(2, SCREEN_MIDDLE_X, SCREEN_MIDDLE_Y - 30, 0, 0)

def update():

    if C.y >= 250:
        C.x = SCREEN_MIDDLE_X
        C.y = SCREEN_MIDDLE_Y - 30
        C.vx = 0
        C.vy = 0

    if pyxel.btn(pyxel.KEY_A):
        R.x -= R.vx
    if pyxel.btn(pyxel.KEY_D):
        R.x += R.vx
    R.return_to_within_bounds()

    C.vy += ACCELERATION_CONSTANT
    C.y += C.vy
    C.x += C.vx

    if collision_happened(C, R):
        C.y = R.y - (2 * C.radius) + 1

        match pyxel.btn(pyxel.KEY_W):
            case True:
                C.vy *= -2.5
            case _:
                C.vy *= -1

        zone = zone_collision_identifier(C, R)
        print(zone)
        set_angle_trajectory(C, zone)

    if C.collision_top_boundary():
        C.vy *= -1

    if C.collision_side_boundaries():
        C.vx *= -1

def draw():
    pyxel.cls(0)
    pyxel.rect(R.x, R.y, R.wid, R.height, 6)
    pyxel.circ(C.x, C.y, C.radius, 10)

pyxel.init(100, 100)
pyxel.run(update, draw)



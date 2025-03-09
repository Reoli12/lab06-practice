from typing import Protocol

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

    def has_collided_with_side(self, screen_max: float):
        return self.x <= 0 or self.x >= screen_max - self.wid

    def is_inside(self, x: float, screen_max: float) -> bool:
        return not (x <= 0 or x >= screen_max - self.wid)

    def return_to_within_bounds(self, screen_max: float):
        if self.x < 0:
            self.x = 0
        elif self.x > screen_max - self.wid:
            self.x = screen_max - self.wid

    @property 
    def bottom(self) -> float:
        return self.y + self.height
    
class UpdateHandler(Protocol):
    def update(self):
        ...

class DrawHandler(Protocol):
    def draw(self):
        ...

class MyCircle:
    def __init__(self, radius: float, x0: float, y0: float,
                vx: float, vy: float, col: int):
        self.radius = radius
        self.x = x0
        self.y = y0
        self.vx = vx
        self. vy = vy
        self.color = col

    def collision_side_boundaries(self, screen_max: float):
        return self.leftmost <= 0 or self.rightmost >= screen_max

    def collision_top_boundary(self):
        return self.top <= 0

    def collision_bottom_boundary(self, x_max: float):
        return self.bottom >= x_max

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
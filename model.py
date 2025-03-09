from project_types import MyCircle, MyRectangle
from math import pi, cos #sin commented out



class Model:

    def __init__(self, screen_height: int, screen_width: int,
                 grav_const: float,
                 ball: MyCircle, platform: MyRectangle):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.grav_constant = grav_const
        self.ball = ball
        self.platform = platform

    def update(self, A_pressed: bool, D_pressed: bool, W_pressed: bool):
        print('i am run')

        if self.ball.collision_bottom_boundary(self.screen_height):
            self.ball.y = self.screen_height / 4
            self.ball.x = self.screen_width / 2
            self.ball.vx = 0
            self.ball.vy = 0

        if A_pressed:
            self.platform.x -= self.platform.vx
        if D_pressed:
            self.platform.x += self.platform.vx
        self.platform.return_to_within_bounds(self.screen_width)

        if self.collision_happened():
            self.put_ball_on_top_of_platform()

            match W_pressed:
                case True:
                    self.ball.vy *= -2.5
                case _:
                    self.ball.vy *= -1

            zone = self.zone_collision_identifier()
            
            self.set_ball_angle_trajectory(zone)

        if self.ball.collision_top_boundary():
            self.ball.vy *= -1

        if self.ball.collision_side_boundaries(self.screen_width):
            self.ball.vx *= -1

        self.ball.vy += self.grav_constant
        self.ball.y += self.ball.vy
        self.ball.x += self.ball.vx



        

    def put_ball_on_top_of_platform(self):
        self.ball.y = self.platform.y - (2 * self.ball.radius) + 1

    def collision_happened(self) -> bool:
        return  (self.platform.y <= self.ball.bottom < self.platform.bottom 
                and self.platform.within_top_side(self.ball.x))

    def zone_collision_identifier(self) -> int:
        circle_dist_from_rect_left = self.ball.x - self.platform.x

        zone_length = self.platform.wid / 5

        assert circle_dist_from_rect_left >= 0

        for i in range(1, 5 + 1):
            if circle_dist_from_rect_left < i * zone_length:
                return i

        raise ValueError
        
    def set_ball_angle_trajectory(self, zone: int):
        
        assert 1 <= zone <= 5
        match zone:
            case 1:
                self.ball.vx = -1 * cos(pi / 6)
            case 2:
                self.ball.vx = -1 * cos(pi / 3)
            case 3:
                pass
            case 4:
                self.ball.vx = 1 * cos(pi / 3)
            case 5:
                self.ball.vx = 1 * cos(pi / 6)
            case _:
                raise ValueError
            

# self.ball.vy *= sin(pi / 6)
# self.ball.vy *= sin(pi / 3)
# self.ball.vx *= cos(pi / 2)
                # self.ball.vy *= sin(pi / 2)
# self.ball.vy *= sin(pi / 3)
# self.ball.vy *= sin(pi / 6)


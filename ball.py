import arcade

class Ball(arcade.Sprite):
    def __init__(
        self,
        image: str,
        distance: float,
        angle: float,
        x: float,
        y: float,
        color: str,
    ):
        super().__init__(image, 0.05)
        self.x = x
        self.y = y
        self.color = color

    def update(self):
        self.center_x = self.x
        self.center_y = self.y

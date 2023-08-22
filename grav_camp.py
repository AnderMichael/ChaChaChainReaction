import arcade

class GravCamp(arcade.Sprite):
    def __init__(
        self,
        filename: str = None,
        scale: float = 1,
        image_x: float = 0,
        image_y: float = 0,
        angle: float = 0,
        pos: list = [(20, 0), (0, 20), (0, -20), (-20, 0)],
        limitBalls: int = 4,
        v: list = [(50, 0), (0, 50), (0, -50), (-50, 0)],
    ):
        # El numero de bolas
        super().__init__(filename, scale=scale)
        self.balls = arcade.SpriteList()
        self.x = image_x
        self.y = image_y
        self.pos = pos
        self.limitBalls = limitBalls
        self.vmov = v
        self.colorBalls = None
        self.color = arcade.color.BLACK

    def update(self):
        self.center_x = self.x
        self.center_y = self.y
        
        if len(self.balls) == 0:
            self.colorBalls = None
        
        if len(self.balls) <= self.limitBalls:
            for b in self.balls:
                if b.color != self.colorBalls:
                    self.colorBalls = b.color
                    for bc in self.balls:
                       bc.color = b.color
            for i, ball in enumerate(self.balls):
                ball.x = self.center_x + self.pos[i][0]
                ball.y = self.center_y + self.pos[i][1]

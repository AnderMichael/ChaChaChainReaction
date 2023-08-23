from arcade.application import Window
from ball import Ball
from grav_camp import GravCamp
import arcade

WIDTH = 1800
HEIGHT = 800
TITLE = "Chain Reaction"


class Menu(arcade.View):
    def __init__(self, window: Window = None):
        super().__init__(window)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            "Cha-Cha-Chain Reaction",
            WIDTH / 2 - 100,
            HEIGHT / 2 + 100,
            arcade.color.CHOCOLATE,
            font_size=50,
            anchor_x="center",
        )

        arcade.draw_polygon_filled(
            [
                (600, 150),
                (600, 180),
                (1000, 180),
                (1000, 150),
            ],
            arcade.color.WHITE,
        )

        arcade.draw_polygon_filled(
            [
                (600, 200),
                (600, 230),
                (1000, 230),
                (1000, 200),
            ],
            arcade.color.WHITE,
        )

        arcade.draw_polygon_filled(
            [
                (600, 250),
                (600, 280),
                (1000, 280),
                (1000, 250),
            ],
            arcade.color.WHITE,
        )

        arcade.draw_polygon_filled(
            [
                (600, 300),
                (600, 330),
                (1000, 330),
                (1000, 300),
            ],
            arcade.color.WHITE,
        )

        arcade.draw_polygon_filled(
            [
                (600, 350),
                (600, 380),
                (1000, 380),
                (1000, 350),
            ],
            arcade.color.WHITE,
        )
        arcade.draw_text(
            "Two Players",
            800,
            365,
            arcade.color.BLACK,
            font_size=15,
            anchor_x="center",
        )

        arcade.draw_text(
            "Three Players",
            800,
            315,
            arcade.color.BLACK,
            font_size=15,
            anchor_x="center",
        )

        arcade.draw_text(
            "Four Players",
            800,
            265,
            arcade.color.BLACK,
            font_size=15,
            anchor_x="center",
        )

        arcade.draw_text(
            "Five Players",
            800,
            215,
            arcade.color.BLACK,
            font_size=15,
            anchor_x="center",
        )

        arcade.draw_text(
            "Close Game",
            800,
            165,
            arcade.color.BLACK,
            font_size=15,
            anchor_x="center",
        )

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if 600 < x < 1000:
            if 150 < y < 180:
                arcade.close_window()
            elif 200 < y < 230:
                self.window.show_view(App(player_count=5, window=self.window))
            elif 250 < y < 280:
                self.window.show_view(App(player_count=4, window=self.window))
            elif 300 < y < 330:
                self.window.show_view(App(player_count=3, window=self.window))
            elif 350 < y < 380:
                self.window.show_view(App(player_count=2, window=self.window))


class Winner(arcade.View):
    def __init__(self, window: Window = None, winner: str = arcade.color.BLACK):
        super().__init__(window)
        self.winner = winner

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            "Winner",
            WIDTH / 2 - 100,
            HEIGHT / 2 + 100,
            self.winner,
            font_size=50,
            anchor_x="center",
        )

        arcade.draw_polygon_filled(
            [
                (600, 300),
                (600, 330),
                (1000, 330),
                (1000, 300),
            ],
            arcade.color.WHITE,
        )

        arcade.draw_polygon_filled(
            [
                (600, 350),
                (600, 380),
                (1000, 380),
                (1000, 350),
            ],
            arcade.color.WHITE,
        )
        arcade.draw_text(
            "Play Again!",
            800,
            365,
            arcade.color.BLACK,
            font_size=15,
            anchor_x="center",
        )

        arcade.draw_text(
            "Close Game",
            800,
            315,
            arcade.color.BLACK,
            font_size=15,
            anchor_x="center",
        )

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if 600 < x < 1000:
            if 300 < y < 330:
                arcade.close_window()
            elif 350 < y < 380:
                self.window.show_view(Menu(window=self.window))


class App(arcade.View):
    def __init__(self, player_count: int = 5, window: Window = None):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)

        self.window = window

        listOfColors = [
            arcade.color.RED,
            arcade.color.YELLOW,
            arcade.color.BLUE,
            arcade.color.VIOLET,
            arcade.color.GREEN,
        ]

        self.listOfColors = listOfColors[0:player_count]

        self.turn = 0
        self.minBalls = 0
        self.start = False
        self.pointBall = arcade.Sprite("assets/ball_image.png", 0.001)
        self.balls = arcade.SpriteList()
        self.bgs = arcade.SpriteList()
        self.set_cells()

    def set_cells(self):
        self.bgs.append(
            GravCamp(
                "assets/fondo_casilla.jpg",
                0.22,
                image_x=150,
                image_y=100,
                pos=[(20, 0), (0, 20)],
                v=[(50, 0), (0, 50)],
                limitBalls=2,
            )
        )
        self.bgs.append(
            GravCamp(
                "assets/fondo_casilla.jpg",
                0.22,
                image_x=150,
                image_y=700,
                pos=[(20, 0), (0, -20)],
                v=[(50, 0), (0, -50)],
                limitBalls=2,
            )
        )
        self.bgs.append(
            GravCamp(
                "assets/fondo_casilla.jpg",
                0.22,
                image_x=1450,
                image_y=100,
                pos=[(-20, 0), (0, 20)],
                v=[(-50, 0), (0, 50)],
                limitBalls=2,
            )
        )
        self.bgs.append(
            GravCamp(
                "assets/fondo_casilla.jpg",
                0.22,
                image_x=1450,
                image_y=700,
                pos=[(-20, 0), (0, -20)],
                v=[(-50, 0), (0, -50)],
                limitBalls=2,
            )
        )

        for r in range(100, 600, 100):
            self.bgs.append(
                GravCamp(
                    "assets/fondo_casilla.jpg",
                    0.22,
                    image_x=150,
                    image_y=100 + r,
                    pos=[(20, 0), (0, -20), (0, 20)],
                    v=[(50, 0), (0, -50), (0, 50)],
                    limitBalls=3,
                )
            )

        for r in range(100, 600, 100):
            self.bgs.append(
                GravCamp(
                    "assets/fondo_casilla.jpg",
                    0.22,
                    image_x=1450,
                    image_y=100 + r,
                    pos=[(-20, 0), (0, -20), (0, 20)],
                    v=[(-50, 0), (0, -50), (0, 50)],
                    limitBalls=3,
                )
            )

        for c in range(200, 1400, 100):
            self.bgs.append(
                GravCamp(
                    "assets/fondo_casilla.jpg",
                    0.22,
                    image_x=50 + c,
                    image_y=100,
                    pos=[(0, 20), (-20, 0), (20, 0)],
                    v=[(0, 50), (-50, 0), (50, 0)],
                    limitBalls=3,
                )
            )

        for c in range(200, 1400, 100):
            self.bgs.append(
                GravCamp(
                    "assets/fondo_casilla.jpg",
                    0.22,
                    image_x=50 + c,
                    image_y=700,
                    pos=[(0, -20), (-20, 0), (20, 0)],
                    v=[(0, -50), (-50, 0), (50, 0)],
                    limitBalls=3,
                )
            )

        for r in range(100, 600, 100):
            for c in range(200, 1400, 100):
                self.bgs.append(
                    GravCamp(
                        "assets/fondo_casilla.jpg",
                        0.22,
                        image_x=50 + c,
                        image_y=100 + r,
                    )
                )

    def on_update(self, delta_time: float):
        for bg in self.bgs:
            bg.balls = arcade.check_for_collision_with_list(bg, self.balls)
            bg.update()
            if len(bg.balls) >= bg.limitBalls:
                self.explosion(bg)
        self.balls.update()
        if self.minBalls >= len(self.listOfColors):
            remain = [
                ball
                for ball in self.balls
                if ball.color == self.listOfColors[self.turn]
            ]

            if len(self.listOfColors) == 1:
                self.window.show_view(
                    Winner(winner=self.listOfColors[0], window=self.window)
                )

            if remain == []:
                self.listOfColors.pop(self.turn)
                self.turn = self.turn % len(self.listOfColors)
        self.pointBall.update()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.pointBall.center_x = x
        self.pointBall.center_y = y

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            grid = arcade.check_for_collision_with_list(self.pointBall, self.bgs)
            if grid != []:
                if self.minBalls < len(self.listOfColors):
                    self.minBalls += 1
                box = grid[0]
                if (
                    box.colorBalls == None
                    or box.colorBalls == self.listOfColors[self.turn]
                ):
                    if box.colorBalls == None:
                        box.colorBalls = self.listOfColors[self.turn]
                    ball = Ball(
                        image="assets/ball_image.png",
                        distance=1,
                        angle=1,
                        x=x,
                        y=y,
                        color=self.listOfColors[self.turn],
                    )
                    self.balls.append(ball)
                    box.balls.append(ball)
                    self.turn += 1
                    self.turn = self.turn % len(self.listOfColors)

    def explosion(self, box: GravCamp):
        v = box.vmov
        balls_to_move = box.balls[0 : box.limitBalls]
        if len(box.balls) > box.limitBalls:
            box.balls = box.balls[box.limitBalls + 1 :]
        else:
            box.balls = []
        for i, ball in enumerate(balls_to_move):
            ball.x += v[i][0]
            ball.y += v[i][1]
            ball.update()

    def on_draw(self):
        arcade.start_render()
        for bg in self.bgs:
            bg.draw()
        for x in range(100, 1700, 100):
            arcade.draw_line(
                x,
                50,
                x,
                750,
                self.listOfColors[self.turn],
                3,
            )
        for y in range(50, 850, 100):
            arcade.draw_line(
                100,
                y,
                1500,
                y,
                self.listOfColors[self.turn],
                3,
            )
        self.balls.draw()
        self.pointBall.draw()


def main():
    app = arcade.Window(WIDTH, HEIGHT, TITLE)
    app.show_view(Menu(app))
    arcade.run()


if __name__ == "__main__":
    main()

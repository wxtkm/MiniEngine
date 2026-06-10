from engine.core import Game
from engine.sprite import Sprite
from engine.static_object import StaticObject

game = Game()

player = Sprite(100, 100)
player.tag = "player"

wall = StaticObject(
    300,
    200,
    size=50,
    color=(255, 0, 0)
)

game.background_color = (20, 20, 40)

game.scene.add(player)
game.scene.add(wall)

game.run()
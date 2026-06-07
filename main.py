from engine.core import Game
from engine.sprite import Sprite
from engine.static_object import StaticObject

game = Game()

player = Sprite(50, 50)
wall = StaticObject(300, 300)

game.scene.add(player)
game.scene.add(wall)

game.run()
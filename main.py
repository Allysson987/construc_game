from ursina import *

from src.world.scene.building_world import BuildingWorld
from src.world.camera.camera import Camera
from src.controls.controls import Controls
from src.players.players import Player


class Orchestra:

    def __init__(self):

        self.app = Ursina()

        self.building_world = BuildingWorld(self.app)

        self.player = Player(
            position=(7, 2, -5)
        )

        self.camera = Camera()

        self.controls = Controls(
            self.player
        )

    def run(self):

        Sky()

        self.building_world.run()

        self.camera.run()

        self.app.run()


start = Orchestra()


def update():

    

    start.controls.update()

    start.camera.follow_player(start.player)


start.run()
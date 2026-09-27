from ursina import *

from src.world.scene.building_world import BuildingWorld
from src.world.camera.camera import Camera
from src.controls.controls import Controls
from src.controls.block_interaction import BlockInteraction
from src.players.players import Player


class Orchestra:

    def __init__(self):

        self.app = Ursina()

        self.building_world = BuildingWorld(
            self.app
        )

        self.player = Player(
            position=(7, 2, -5)
        )

        self.camera = Camera()

        self.controls = Controls(
            self.player
        )

        self.block_interaction = BlockInteraction(
            self.player
        )

    def run(self):

        Sky()

        self.building_world.run()

        self.camera.run()

        self.app.run()


start = Orchestra()

start = Orchestra()


def update():

    start.controls.update()

    start.camera.follow_player(
        start.player
    )

    start.camera.mouse_look()


def input(key):

    start.block_interaction.input(key)


# start.run()

start.run()
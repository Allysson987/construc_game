
from ursina import *

from src.world.scene.building_world import BuildingWorld
from src.world.camera.camera import Camera
from src.controls.controls import Controls
from src.players.players import Player


class Orchestra:

    def __init__(self):

        self.app = Ursina()

        # =========================
        # MUNDO
        # =========================

        self.building_world = BuildingWorld(
            self.app
        )

        # =========================
        # PLAYER
        # =========================

        self.player = Player(
            position=(7, 2, -5),
            building_world=self.building_world
        )

        # =========================
        # CAMERA
        # =========================

        self.camera = Camera()

        # =========================
        # CONTROLES
        # =========================

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

    start.camera.follow_player(
        start.player
    )

    start.camera.mouse_look()


def input(key):

    # Botão esquerdo = quebrar
    if key == 'left mouse down':

        start.player.break_block()

    # Botão direito = colocar
    if key == 'right mouse down':

        start.player.place_selected_item()


start.run()


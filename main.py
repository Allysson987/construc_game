
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
        # GERAR MUNDO
        # =========================

        self.building_world.run()

        # =========================
        # POSIÇÃO DO PLAYER
        # =========================

        player_x = 8
        player_z = 8

        # Descobre a altura do terreno
        player_y = self.building_world.get_terrain_height(
            player_x,
            player_z
        )

        # Coloca o Player acima do terreno
        player_position = (
            player_x,
            player_y + 1,
            player_z
        )

        # =========================
        # PLAYER
        # =========================

        self.player = Player(
            position=player_position,
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



from src.world.blocks.blocks import Grass, Stone
from src.world.blocks.construct_objetcs import Tree

from perlin_noise import PerlinNoise

import random


class BuildingWorld:

    def __init__(self, app):

        self.app = app

        # Todos os blocos existentes no mundo
        self.buildings = []

        # =========================
        # CONFIGURAÇÃO DO MUNDO
        # =========================

        self.width = 32
        self.depth = 32

        # Altura mínima do terreno
        self.min_height = 1

        # Altura máxima adicional
        self.max_height = 8

        # Seed do mundo
        self.seed = 12345

        # Noise utilizado para gerar o terreno
        self.terrain_noise = PerlinNoise(
            octaves=3,
            seed=self.seed
        )

        # Noise separado para vegetação
        self.tree_noise = PerlinNoise(
            octaves=2,
            seed=self.seed + 100
        )

    # =========================
    # ALTURA DO TERRENO
    # =========================

    def get_terrain_height(self, x, z):

        # Noise retorna aproximadamente
        # valores entre -1 e 1.

        noise_value = self.terrain_noise(
            [
                x * 0.08,
                z * 0.08
            ]
        )

        # Converte para 0 até 1
        normalized = (
            noise_value + 1
        ) / 2

        # Converte para altura
        height = int(
            self.min_height
            +
            normalized * self.max_height
        )

        return height

    # =========================
    # CRIAR TERRENO
    # =========================

    def create_terrain(self):

        for x in range(self.width):

            for z in range(self.depth):

                # Descobre a altura
                # daquela posição.
                height = self.get_terrain_height(
                    x,
                    z
                )

                # =========================
                # CAMADAS DO TERRENO
                # =========================

                for y in range(height):

                    # Último bloco = grama
                    if y == height - 1:

                        block = Grass(
                            position=(x, y, z)
                        )

                    # Restante = pedra
                    else:

                        block = Stone(
                            position=(x, y, z)
                        )

                    self.buildings.append(
                        block
                    )

    # =========================
    # CRIAR ÁRVORES
    # =========================

    def create_trees(self):

        tree_positions = set()

        for x in range(1, self.width - 1):

            for z in range(1, self.depth - 1):

                # Noise determina
                # onde existe vegetação.

                vegetation = self.tree_noise(
                    [
                        x * 0.15,
                        z * 0.15
                    ]
                )

                # Nem todo lugar recebe árvore
                if vegetation < 0.45:
                    continue

                # Evita muitas árvores
                if random.random() > 0.08:
                    continue

                # Evita duas árvores na mesma posição
                if (x, z) in tree_positions:
                    continue

                tree_positions.add(
                    (x, z)
                )

                # Descobre a altura do terreno
                height = self.get_terrain_height(
                    x,
                    z
                )

                # A árvore nasce em cima da grama
                tree = Tree(
                    (
                        x,
                        height,
                        z
                    )
                )

                tree.create_tree()

                self.buildings.extend(
                    tree.blocks
                )

    # =========================
    # CRIAR MUNDO
    # =========================

    def create_building(self):

        # Primeiro cria o terreno
        self.create_terrain()

        # Depois coloca as árvores
        self.create_trees()

    # =========================
    # EXECUTAR
    # =========================

    def run(self):

        self.create_building()

        print(
            f"BuildingWorld iniciado com "
            f"{len(self.buildings)} blocos."
        )


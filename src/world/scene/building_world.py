from src.world.blocks.block_controls import Block
from src.world.blocks.construct_objetcs import Tree

from ursina import color
import random


class BuildingWorld:

    def __init__(self, app):

        self.app = app
        self.buildings = []

    def create_building(self):

        # PEDRA - camada completamente preenchida
        for x in range(16):
            for z in range(16):

                block = Block(
                    name="Pedra",
                    resistance=100,
                    hardness=5,
                    color=color.gray,
                    position=(x, -1, z)
                )

                self.buildings.append(block)

        # GRAMA - camada completamente preenchida
        for x in range(16):
            for z in range(16):

                block = Block(
                    name="Grama",
                    resistance=20,
                    hardness=1,
                    color=color.green,
                    position=(x, 0, z)
                )

                self.buildings.append(block)

        # ÁRVORES - posições aleatórias
                # ÁRVORES - posições aleatórias
        tree_positions = set()

        for i in range(15):

            while True:

                x = random.randint(1, 14)
                z = random.randint(1, 14)

                if (x, z) not in tree_positions:
                    tree_positions.add((x, z))
                    break

            tree = Tree((x, 1, z))
            tree.create_tree()

            self.buildings.extend(tree.blocks)

    def run(self):

        self.create_building()

        print(
            f"BuildingWorld iniciado com "
            f"{len(self.buildings)} blocos."
        )
from src.world.blocks.block_controls import Block
from ursina import color


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
                    position=(x, -2, z)
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


        # MADEIRA - acima da grama, com espaço
        for x in range(0, 16, 3):
            for z in range(0, 16, 3):

                block = Block(
                    name="Madeira",
                    resistance=40,
                    hardness=2,
                    color=color.brown,
                    position=(x, 2, z)
                )

                self.buildings.append(block)


    def run(self):

        self.create_building()

        print(
            f"BuildingWorld iniciado com "
            f"{len(self.buildings)} blocos."
        )
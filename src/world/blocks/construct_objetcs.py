from src.world.blocks.blocks import Wood, Leaf


class Tree:

    def __init__(self, position):

        self.position = position
        self.blocks = []

    def create_tree(self):

        # Tronco
        for y in range(5):

            block = Wood()

            block.position = (
                self.position[0],
                self.position[1] + y,
                self.position[2]
            )

            self.blocks.append(block)

        # Folhas
        for x in range(-2, 3):

            for z in range(-1, 2):

                block = Leaf()

                block.position = (
                    self.position[0] + x,
                    self.position[1] + 3,
                    self.position[2] + z
                )

                self.blocks.append(block)
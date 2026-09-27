from src.world.blocks.block_controls import Block

class Wood(Block):

    def __init__(self):
        super().__init__(
            name="Madeira",
            resistance=40,
            hardness=2
        )
class Stone(Block):

    def __init__(self, **kwargs):

        super().__init__(
            name="Pedra",
            resistance=100,
            hardness=5,
            color=color.gray,
            **kwargs
        )
class Grass(Block):

    def __init__(self, **kwargs):

        super().__init__(
            name="Grama",
            resistance=20,
            hardness=1,
            color=color.green,
            **kwargs
        )
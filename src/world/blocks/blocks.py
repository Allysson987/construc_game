from ursina import color
from src.world.blocks.block_controls import Block


class Wood(Block):

    def __init__(self, **kwargs):
        super().__init__(
            name="Madeira",
            resistance=40,
            hardness=2,
            texture=rf'data\textures\wood.png',
            **kwargs
        )


class Leaf(Block):

    def __init__(self, **kwargs):
        super().__init__(
            name="Folha",
            resistance=10,
            hardness=1,
            color=color.rgb(0, 140, 0),
            **kwargs
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
            texture=rf'data\textures\grass.png',
            **kwargs
        )
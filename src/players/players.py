from ursina import Entity


class Player(Entity):

    def __init__(self, position=(0, 1, 0)):

        super().__init__(
            model='cube',
            scale=(0.8, 1.8, 0.8),
            position=position,
            collider='box',
            visible=False
        )
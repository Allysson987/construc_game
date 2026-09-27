from ursina import Entity


class Block(Entity):

    def __init__(
        self,
        name,
        resistance,
        hardness,
        **kwargs
    ):
        super().__init__(
            model='cube',
            collider='box',
            **kwargs
        )

        self.name = name
        self.max_resistance = resistance
        self.resistance = resistance
        self.hardness = hardness

    def damage(self, amount):
        self.resistance -= amount

        print(
            f"{self.name}: "
            f"{self.resistance}/{self.max_resistance}"
        )

        if self.resistance <= 0:
            self.break_block()

    def break_block(self):
        print(f"{self.name} quebrado!")
        self.disable()
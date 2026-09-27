from ursina import held_keys, time


class Controls:

    def __init__(self, player):

        self.player = player
        self.speed = 5

    def update(self):

        speed = self.speed * time.dt

        if held_keys['w']:
            self.player.z += speed

        if held_keys['s']:
            self.player.z -= speed

        if held_keys['a']:
            self.player.x -= speed

        if held_keys['d']:
            self.player.x += speed
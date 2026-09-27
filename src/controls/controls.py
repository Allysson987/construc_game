from ursina import held_keys, time


class Controls:

    def __init__(self, camera):
        self.camera = camera
        self.speed = 5

    def update_camera(self):

        speed = self.speed * time.dt

        if held_keys['w']:
            self.camera.z += speed

        if held_keys['s']:
            self.camera.z -= speed

        if held_keys['a']:
            self.camera.x -= speed

        if held_keys['d']:
            self.camera.x += speed
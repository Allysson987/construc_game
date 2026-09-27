from ursina import camera, mouse, held_keys, time


class Camera:

    def __init__(self):

        self.sensitivity = 40

        self.position = (7, 5, -14)

        self.pitch = 0
        self.yaw = 0

    def create_camera(self):

        camera.position = self.position

        camera.rotation_x = self.pitch
        camera.rotation_y = self.yaw

        return camera

    def follow_player(self, player):

        camera.position = (
            player.x,
            player.y + 0.8,
            player.z
        )

    def mouse_look(self):

        self.yaw += mouse.velocity[0] * self.sensitivity
        self.pitch -= mouse.velocity[1] * self.sensitivity

        self.pitch = max(-89, min(89, self.pitch))

        camera.rotation_x = self.pitch
        camera.rotation_y = self.yaw

    def run(self):

        self.create_camera()

        print("Camera is running")

        return camera
from ursina import camera


class Camera:

    def __init__(self):

        self.position = (7.5, 5, -14)
        self.rotation = (0, 0, 0)

    def create_camera(self):

        camera.position = self.position
        camera.rotation = self.rotation

        return camera

    def follow_player(self, player):

        camera.position = (
            player.x,
            player.y + 0.8,
            player.z
        )

    def run(self):

        self.create_camera()

        print("Camera is running")

        return camera
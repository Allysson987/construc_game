from ursina import camera


class Camera:
    def __init__(self):
        self.position = (7.5, 30, -14)
        self.rotation = (55, 0, 0)
        self.game_camera = None

    def create_camera(self):
        camera.position = self.position
        camera.rotation = self.rotation

        self.game_camera = camera

        return self.game_camera

    def run(self):
        self.create_camera()
        print("Camera is running")

        return self.game_camera
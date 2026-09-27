
from ursina import camera


class Camera:
    def __init__(self):
        self.position = (7.5, 30, -14)
        self.rotation = (55, 0, 0)

    def create_camera(self):
        camera.position = self.position
        camera.rotation = self.rotation

        return camera

    def run(self):
        game_camera = self.create_camera()
        print("Camera is running")
        return game_camera

from ursina import *
from src.world.scene.building_world import BuildingWorld
from src.world.camera.camera import Camera
from src.controls.controls import Controls


class Orchestra(Entity):

    def __init__(self, **kwargs):

        super().__init__(
            model='orchestra',
            texture='orchestra_texture',
            collider='box',
            **kwargs
        )

        self.app = Ursina()

        self.building_world = BuildingWorld(self.app)

        self.camera = Camera()
        self.game_camera = self.camera.run()

        self.controls = Controls(self.game_camera)

    def update(self):
        self.controls.update_camera()

    def run(self):

        print("Orchestra is running")

        Sky()

        self.building_world.run()

        self.app.run()


start = Orchestra()
start.run()
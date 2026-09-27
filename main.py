from ursina import *
from src.world.scene.building_world import BuildingWorld
from src.world.camera.camera import Camera
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
        
    def run(self):
        print("Orchestra is running")
        Sky()
        self.building_world.run()
        self.camera.run()
        self.app.run()

        

start= Orchestra()
start.run()

from ursina import Entity, color


class BuildingWorld:
    def __init__(self, app):
        self.app = app
        self.buildings = []

    def create_building(self):
        for x in range(16):
            for z in range(16):

                building = Entity(
                    model='cube',
                    color=color.green,
                    position=(x, 0, z),
                    scale=(1, 1, 1),
                    collider='box'
                )

                self.buildings.append(building)

    def run(self):
        self.create_building()
        print(f"BuildingWorld iniciado com {len(self.buildings)} prédios.")

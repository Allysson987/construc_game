from ursina import camera, raycast


class BlockInteraction:

    def __init__(self, player):

        self.player = player
        self.damage = 10
        self.distance = 20

    def input(self, key):

        print("TECLA:", key)

        if key == 'left mouse down':

            print("CLIQUE DETECTADO")

            self.break_block()

    def break_block(self):

        print("FAZENDO RAYCAST")

        print("CAMERA POSITION:", camera.world_position)
        print("CAMERA FORWARD:", camera.forward)

        hit = raycast(
            origin=camera.world_position,
            direction=camera.forward,
            distance=self.distance,
            ignore=[self.player]
        )

        print("HIT:", hit.hit)

        if hit.hit:

            entity = hit.entity

            print("========== BLOCO ==========")
            print("Tipo:", type(entity))
            print("Nome:", getattr(entity, 'name', 'SEM NOME'))
            print("Dano:", hasattr(entity, 'damage'))

            if hasattr(entity, 'damage'):
                entity.damage(self.damage)
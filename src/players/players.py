
from ursina import Entity, camera, raycast
from src.world.blocks.blocks import Wood


class Player(Entity):

    def __init__(
        self,
        position=(0, 1, 0),
        building_world=None
    ):

        super().__init__(
            model='cube',
            scale=(0.8, 1.8, 0.8),
            position=position,
            collider='box',
            visible=False
        )

        # Mundo
        self.building_world = building_world

        # =========================
        # INVENTÁRIO
        # =========================

        self.inventory = {}

        self.selected_item = None

        # =========================
        # INTERAÇÃO
        # =========================

        self.damage = 10
        self.interaction_distance = 20

    # =========================
    # INVENTÁRIO
    # =========================

    def add_item(self, item, quantity=1):

        if item not in self.inventory:
            self.inventory[item] = 0

        self.inventory[item] += quantity

        print(
            f"Adicionado: {item} x{quantity}"
        )

        print(
            f"Inventário: {self.inventory}"
        )

    def remove_item(self, item, quantity=1):

        if not self.has_item(item, quantity):

            print(
                f"Você não possui {item} x{quantity}."
            )

            return False

        self.inventory[item] -= quantity

        if self.inventory[item] <= 0:

            del self.inventory[item]

            if self.selected_item == item:
                self.selected_item = None

        print(
            f"Removido: {item} x{quantity}"
        )

        print(
            f"Inventário: {self.inventory}"
        )

        return True

    def has_item(self, item, quantity=1):

        return self.inventory.get(item, 0) >= quantity

    # =========================
    # SELECIONAR ITEM
    # =========================

    def select_item(self, item):

        if not self.has_item(item):

            print(
                f"Você não possui {item}."
            )

            return False

        self.selected_item = item

        print(
            f"Item selecionado: {item}"
        )

        return True

    # =========================
    # COLOCAR BLOCO
    # =========================

    def place_selected_item(self):

        if self.selected_item is None:

            print(
                "Nenhum item selecionado."
            )

            return

        if not self.has_item(
            self.selected_item
        ):

            print(
                "Você não possui esse item."
            )

            return

        if self.building_world is None:

            print(
                "BuildingWorld não foi conectado."
            )

            return

        hit = raycast(
            origin=camera.world_position,
            direction=camera.forward,
            distance=self.interaction_distance,
            ignore=[self]
        )

        if not hit.hit:

            print(
                "Nenhum bloco encontrado."
            )

            return

        # Posição da face do bloco atingido
        position = hit.entity.position + hit.normal

        # =========================
        # MADEIRA
        # =========================

        if self.selected_item == "Madeira":

            block = Wood(
                position=position
            )

            self.building_world.buildings.append(
                block
            )

            self.remove_item(
                "Madeira"
            )

            print(
                f"Madeira colocada em {position}"
            )

    # =========================
    # QUEBRAR BLOCO
    # =========================

    def break_block(self):

        hit = raycast(
            origin=camera.world_position,
            direction=camera.forward,
            distance=self.interaction_distance,
            ignore=[self]
        )

        if not hit.hit:
            return

        block = hit.entity

        if not hasattr(block, 'damage'):
            return

        item = block.damage(
            self.damage
        )

        if item:

            sif item:
    self.add_item(item)
    self.select_item(item)


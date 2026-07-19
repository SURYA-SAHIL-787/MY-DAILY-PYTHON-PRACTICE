class UrbanTree:
    def __init__(self, tree_id, water_level, pest_damage):
        self.tree_id = tree_id
        self.water_level = water_level
        self.pest_damage = pest_damage

    def calculate_health(self):
        return self.water_level - self.pest_damage


class RoadsideTree(UrbanTree):
    def __init__(
        self,
        tree_id,
        water_level,
        pest_damage,
        pollution_level
    ):
        super().__init__(tree_id, water_level, pest_damage)
        self.pollution_level = pollution_level

    def calculate_health(self):
        return (
            self.water_level
            - self.pest_damage
            - self.pollution_level
        )


class ParkTree(UrbanTree):
    def calculate_health(self):
        return (
            self.water_level * 1.2
            - self.pest_damage
        )


class HeritageTree(UrbanTree):
    def __init__(self, tree_id, water_level, pest_damage, age):
        super().__init__(tree_id, water_level, pest_damage)
        self.age = age

    def calculate_health(self):
        age_bonus = min(self.age / 20, 10)

        return (
            self.water_level
            - self.pest_damage
            + age_bonus
        )


trees = [
    RoadsideTree("TREE-11", 80, 15, 20),
    ParkTree("TREE-12", 70, 10),
    HeritageTree("TREE-13", 65, 8, 140)
]

for tree in trees:
    print(
        f"{tree.tree_id}: "
        f"Health score = {tree.calculate_health():.2f}"
    )

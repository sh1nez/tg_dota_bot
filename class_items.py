class BaseItem:
    def __init__(self, name: str, description: str, price: int, main_stat: int):
        self.name = name
        self.description = description
        self.price = price
        self.stat = main_stat

    def make_text(self, *args, **kwargs):
        pass

    def fight(self, *args, **kwargs):
        pass


class FarmItem(BaseItem):
    def __init__(self, name: str, description: str or None, price: int, main_stat: int, movespeed: int, farmspeed: int):
        super().__init__(name, description, price, main_stat)
        self.ms = movespeed
        self.farm = farmspeed   # от 0 до 100

    def make_text(self):
        text = f"это {self.name}, он стоит {self.price}\n{self.description if self.description else ''}" \
               f"{f'основной стат - {stats_arr[self.stat]}' if self.stat else 'нет основного атрибута'}\n" \
               f"даёт в фарме:\n{self.ms} скорости и {self.farm} эффективности"
        return text


class FightItem(BaseItem):
    def __init__(self, name: str, description: str, price: int, main_stat: int, damage: float, helth: int):
        super().__init__(name, description, price, main_stat)
        self.damage = damage
        self.hp = helth


stats_arr = ['ультимативный', 'сила', 'ловкость', 'интеллект']

midas = FarmItem('мидас', None, 2250, 0, 0, 70)
print(midas.make_text())

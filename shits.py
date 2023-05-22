class BaseHero:

    def __init__(self, name: str, price: int, ):
        self.name = name
        self.price = price
    # def __new__(cls, *args, **kwargs):

    def send_description(self, *args, **kwargs) -> Exception:
        return Exception('это BaseHero')

    def lvlup(self, *args, **kwargs) -> Exception:
        return Exception('это BaseHero')

    def local_dick(self):
        return dict(self.__dict__)


class HeroNew(BaseHero):
    def __init__(self, name: str, price: int, description: str or None, img: str, good_event: str, bad_event: str,
                 magic_damage_kef: float,  fiz_damage_kef: float, total_mag_d: int, total_fiz_d: int,
                 total_farm: int, farm: float, speed_farm: int,  hp: int, total_mag_hp: int, total_fiz_hp: int,
                 kef_mag_hp: float, kef_fiz_hp: float, base_exp:int, lvl_up: dict):
        super().__init__(name, price)
        self.description = description

        self.total_farm = total_farm  #любое число по хорошему 0-100
        self.kef_farm = farm  # 0-2
        self.ms = speed_farm  # просто мс, базовый 100-300 будет

        self.kef_mag_d = magic_damage_kef  # 0-2
        self.kef_fiz_d = fiz_damage_kef  # 0-2
        self.total_mag_d = total_mag_d  # любое число, желательно 0-100
        self.total_fiz_d = total_fiz_d  # любое число, желательно 0-100

        self.hp = hp  # любое число, желательно 100-1000
        self.total_mag_hp = total_mag_hp  #
        self.total_fiz_hp = total_fiz_hp
        self.kef_mag_hp = kef_mag_hp
        self.kef_fiz_hp = kef_fiz_hp

        self.exp =
        self.lvl_up = lvl_up  # dict farm, fiz_d, mag_d,

        self.img = img
        self.good = good_event
        self.bad = bad_event

    def send_description(self) -> str:
        desc = self.description+'\n' if self.description else ''
        text = f"Это {self.name}, он стоит {self.price}\n{desc}" \
               f"Базовые атрибуты:\nХп - {self.hp}, фрам - {self.total_farm}\n" \
               f"{int(self.total_fiz)} - физ, {int(self.total_mag)} - маг\n"\
               f"Потанцевал:\n" \
               f"Фрам - {int(self.kef_farm*50)}%, файт - {int((self.kef_fiz+self.kef_mag)*25)}%:\n" \
               f"{int(self.kef_fiz*50)}% - физ, {int(self.kef_mag*50)}% - маг"
        return text

    def lvlup(self, lvl) -> dict:  # magic, fiz damage, hp, farm
        """ Должен принимать в себя уровень и возвращать атрибуты в зависимости от lvl"""
        """ 'farm': float, 'fiz': float, 'mag': float,"""
        dick = {
            'fiz': int(self.total_fiz + self.lvl_up['fiz']*lvl),
            'magic': int(self.total_mag + self.lvl_up['mag']*lvl),
            'farm': int(self.total_farm + self.lvl_up['farm']*lvl)
        }
        return dick

    def item_buffs(self, *args) -> dict:
        """Должен принимать предметы и возвращать атрибуты в зависимости от предметов"""
        pass


class BaseItem:
    def __init__(self, name: str, description: str, price: int, main_stat: int or None):
        self.name = name
        self.description = description
        self.price = price
        self.stat = main_stat

    def make_text(self, *args, **kwargs):
        pass

    def stats(self, *args, **kwargs):
        pass




class FarmItem(BaseItem):
    def __init__(self, name: str, description: str or None, price: int, main_stat: int or None, movespeed: int, farm_num: int):
        super().__init__(name, description, price, main_stat)
        self.ms = movespeed
        self.farm_num = farm_num   # от 0 до 100

    def make_text(self, *args, **kwargs):
        des = f'{self.description}\n' if self.description else ''
        text = f"это {self.name}, он стоит {self.price},\n{des}" \
               f"{f'основной стат - {stats_arr[self.stat]}' if self.stat else 'нет основного атрибута'}\n" \
               f"даёт в фарме:\n{self.ms} скорости и {self.farm_num} эффективности"
        return text

    def stats(self, *args, **kwargs):
        return {'ms': self.ms, 'total_farm': self.farm_num}


class FightItem(BaseItem):
    def __init__(self, name: str, description: str or None, price: int, main_stat: int or None, magic_damage: int,
                 fiz_damage: int,  hp: int):
        super().__init__(name, description, price, main_stat)
        self.mag = magic_damage
        self.fiz = fiz_damage
        self.hp = hp

    def make_text(self, *args, **kwargs):
        des = f'{self.description}\n' if self.description else ''
        text = f"это {self.name}, он стоит {self.price},\n{des}" \
               f"{f'основной стат - {stats_arr[self.stat]}' if self.stat is not None else 'нет основного атрибута'}\n" \
               f"даёт в уроне:\n{self.mag} маг и {self.fiz} физ"
        return text

    def stats(self, *args, **kwargs):
        return {'total_mag': self.mag, 'total_fiz': self.fiz, 'hp': self.hp}


stats_arr = ['ультимативный', 'сила', 'ловкость', 'интеллект']

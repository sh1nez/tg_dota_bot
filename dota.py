class DifferentLens(Exception):
    """Нельзя использовать разные длины buffs"""
    def __init__(self, *args, **kwargs):
        print(*args, **kwargs)
        print('загляни в lvlup_hero, длины кортежей check')


class BaseHero:
    """def __init__(self, name: str, price: int, img1: str, img2: str, img3: str):"""
    def __init__(self, hp: int, farm_speed: int, total_farm: int, fiz_tuple: tuple, magic_tuple: tuple):
        # mag_hp: int, fiz_hp:int,
        self.hp = hp

        self.farm_speed = farm_speed
        self.total_farm = total_farm

        self.fiz_tuple = fiz_tuple
        self.mag_tuple = magic_tuple

    def __lt__(self, *args, **kwargs) -> Exception:
        return Exception('фигню сделал')

    @classmethod
    def local_dict(cls):
        return dict(cls.__dict__)

    def lvlup_hero(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')


class NewHero(BaseHero):
    def __init__(self, name: str, price: int, description: str or None, img1, img2, img3,  # интерфейс
                 hp: int, fiz_armor: float, mag_armor: float,  # базовые хп
                 farm_speed: int, total_farm: int, kef_farm: float,
                 fiz_tuple: tuple, fiz_buf: float,  # attack_speed: float,
                 magic_tuple: tuple, magic_buf: float,  # magic_tuple - (dmg, sec), (20, 0.57)
                 exp: int, lvl_up: dict):  # для lvl up
        """self, hp: int, farm_speed: int, total_farm: int,
                 fiz_damage: int, attack_speed: float, magic_damage: int, magic_speed: float):"""
        super().__init__(hp, farm_speed, total_farm,
                         fiz_tuple, magic_tuple)  # base dmg
        """интерфейс"""
        self.name = name
        self.price = price
        self.description = description
        self.img = img1
        self.good = img2
        self.bad = img3
        """Stats"""
        self.fiz_armor = fiz_armor  # 0-100
        self.mag_armor = mag_armor  # 0-100
        """коэффициенты"""
        self.kef_farm = kef_farm  # 0-n
        self.fiz_buf = fiz_buf  # 0-n
        self.magic_buf = magic_buf  # 0-n
        """лвл апы"""
        self.exp = exp  # ~300-500
        self.lvl_up = lvl_up  # tuple buffs

    def base_stats(self):
        return

    def lvlup_hero(self, lvl) -> tuple:
        """Прибавки за уровень локального героя"""
        """ exp, hp, fiz_armor, mag_armor, fiz_damage, attack_speed, (magic_damage, magic_speed)"""
        if len(self.lvl_up['magic_tuple']) != len(self.mag_tuple):
            raise DifferentLens('магия длины кортежей')
        if len(self.lvl_up['fiz_tuple']) != len(self.fiz_tuple):
            raise DifferentLens('физика длины кортежей')
        mag = ()
        for i in zip(self.mag_tuple, self.lvl_up['magic_tuple']):
            mag += ((i[0][0]+(i[1][0]*lvl), i[0][1]-(i[1][1]*lvl)),)
        fiz = ()
        for i in zip(self.fiz_tuple, self.lvl_up['fiz_tuple']):
            fiz += ((i[0][0]+(i[1][0]*lvl), i[0][1]+(i[1][1]*lvl)),)
        """все источники маг урона изменены"""
        print(self.fiz_armor, round((1 - self.fiz_armor), 5), self.lvl_up['fiz_armor'], lvl)
        fiz_armor = float(self.fiz_armor)
        magic_armor = float(self.mag_armor)
        for i in range(lvl):
            fiz_armor += (1 - fiz_armor) * self.lvl_up['fiz_armor']
            magic_armor += (1-fiz_armor) * self.lvl_up['mag_armor']
        tup_hp = int(self.hp + self.lvl_up['hp'] * lvl), fiz_armor, magic_armor
        tup_farm = self.farm_speed + self.lvl_up['farm_speed']*lvl,\
            self.total_farm + self.lvl_up['total_farm']*lvl,
        return tup_hp, tup_farm, fiz, mag

    def exp_up_lvl(self, lvl, exp):
        """Можем у героя вызвать этот класс, чтобы проверить эксп"""
        exp_lvl = self.exp + self.lvl_up['exp'] * lvl
        print(lvl, exp_lvl, exp)
        while exp >= exp_lvl:
            lvl += 1
            exp -= exp_lvl
            exp_lvl += + self.lvl_up['exp']
        return lvl, exp


class LocalHero(BaseHero):
    def __init__(self, hp: int, fiz_armor: float, magic_armor: float, farm_speed: int, total_farm: int,
                 fiz_tuple: tuple, magic_tuple: tuple,):
        """ hp: int, farm_speed: int, total_farm: int, fiz_tuple: tuple, magic_tuple: tuple):"""
        super().__init__(hp, farm_speed, total_farm, fiz_tuple, magic_tuple)
        self.magic_armor = magic_armor
        self.fiz_armor = fiz_armor

    def __lt__(self, other: object) -> bool or Exception:
        if not isinstance(other, LocalHero):
            return Exception('нужен LocalHero')
        return False


class BaseItem:
    def __init__(self, hp: int, fiz_armor: float, mag_armor: float,
                 fiz_dmg: int, attack_speed: float, mag_dmg: int, mag_speed: float,
                 farm_speed: int, total_farm: int,):
        self.hp = hp
        self.fiz_armor = fiz_armor
        self.mag_armor = mag_armor
        self.fiz_dmg = fiz_dmg
        self.attack_speed = attack_speed
        self.mag_dmg = mag_dmg
        self.mag_speed = mag_speed
        self.farm_speed = farm_speed
        self.total_farm = total_farm

    def __add__(self, other: LocalHero):
        if not isinstance(other, LocalHero):
            raise Exception('можно прибавлять только предметы к герою')
        print(LocalHero)

    def __radd__(self, other):
        self.__add__(other)
class ShopItem(BaseItem):
    def __init__(self, price: int, description: str or None, img1: str, img2: str,
                 main_stat: int,
                 hp: int, fiz_armor: float, mag_armor: float,
                 fiz_dmg: int, attack_speed: float, mag_dmg: int, mag_speed: float,
                 farm_speed: int, total_farm: int,
                 ):
        super().__init__(hp, fiz_armor, mag_armor, fiz_dmg, attack_speed, mag_dmg,
                         mag_speed, farm_speed, total_farm)
        self.main_stat = main_stat
        self.price = price
        self.description = description
        self.img1 = img1
        self.img2 = img2


class FightItems(BaseItem):
    def __init__(self, hp: int, fiz_armor: float, mag_armor: float,
                 fiz_dmg: int, attack_speed: float, mag_dmg: int, mag_speed: float,
                 farm_speed: int, total_farm: int,):
        super().__init__(hp, fiz_armor, mag_armor, fiz_dmg, attack_speed, mag_dmg,
                         mag_speed, farm_speed, total_farm)


def die_second1(hp: int, timers: list) -> int and float:
    """[[dmg, time, count],[10, 0.47, 0]]"""
    dmg = sum([i[0] for i in timers])
    seconds = 0
    timers.sort(key=lambda k: k[1])
    small = timers[0][1]
    while dmg < hp:
        for i in timers:
            if seconds // i[1] > i[2]:
                i[2] += 1
                dmg += i[0]
            else:
                break
        seconds = round(seconds+small, 5)
    return dmg, seconds


def die_second2(hp: int, timers: list) -> float:
    """test_arr = [[22, 0.47123, 0], [10, 0.3331212, 0], [100, 12.123123,  0], [321, 10.81283, 0]]"""
    speeds = [i[0]/i[1] for i in timers]
    return hp/sum(speeds)


# test_arr = [[22, 0.47123, 0], [10, 0.3331212, 0], [100, 12.123123,  0], [321, 10.81283, 0]]
# print(die_second1(999999, test_arr))
# print(die_second2(999999, test_arr))

class DifferentLens(Exception):
    """Нельзя использовать разные длины buffs"""

    def __init__(self, *args, **kwargs):
        print(*args, **kwargs)
        print('загляни в lvlup_hero, длины кортежей check')


class BaseHero:
    """def __init__(self, name: str, price: int, img1: str, img2: str, img3: str):"""

    def __init__(self, hp: int, farm_speed: int, total_farm: int, fiz_tuple: tuple, mag_tuple: tuple,
                 magic_buf: float):
        # mag_hp: int, fiz_hp:int,
        self.hp = hp

        self.farm_speed = farm_speed
        self.total_farm = total_farm

        self.fiz_tuple = fiz_tuple
        self.mag_tuple = mag_tuple
        self.mag_buf = magic_buf

    def __mul__(self, other) -> Exception:
        return Exception('фигню сделал')

    @classmethod
    def local_dict(cls):
        return dict(cls.__dict__)

    def lvlup_hero(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')

    def no_items(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')


class NewHero(BaseHero):
    def __init__(self, name: str, price: int, description: str or None, img1, img2, img3,  # интерфейс
                 hp: int, fiz_armor: float, mag_armor: float,  # базовые хп
                 farm_speed: int, total_farm: int, kef_farm: float,
                 fiz_tuple: tuple, fiz_buf: float,  # attack_speed: float,
                 mag_tuple: tuple, mag_buf: float,  # mag_tuple - (dmg, sec), (20, 0.57)
                 exp: int, lvl_up: dict):  # для lvl up
        """self, hp: int, farm_speed: int, total_farm: int,
                 fiz_damage: int, attack_speed: float, mag_damage: int, mag_speed: float):"""
        super().__init__(hp, farm_speed, total_farm,
                         fiz_tuple, mag_tuple, mag_buf)  # base dmg
        """Stats"""
        self.fiz_armor = fiz_armor  # 0-100
        self.mag_armor = mag_armor  # 0-100
        """интерфейс"""
        self.name = name
        self.price = price
        self.description = description
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        """коэффициенты"""
        self.kef_farm = kef_farm  # 0-n
        self.fiz_buf = fiz_buf  # 0-n
        """лвл апы"""
        self.exp = exp  # ~300-500
        self.lvl_up = lvl_up  # tuple buffs

    def lvlup_hero(self, lvl) -> tuple:
        """Прибавки за уровень локального героя"""
        """ exp, hp, fiz_armor, mag_armor, fiz_damage, attack_speed, (mag_damage, mag_speed)"""
        if len(self.lvl_up['mag_tuple']) != len(self.mag_tuple):
            raise DifferentLens('магия длины кортежей')
        if len(self.lvl_up['fiz_tuple']) != len(self.fiz_tuple):
            raise DifferentLens('физика длины кортежей')

        mag = ()
        for i in zip(self.mag_tuple, self.lvl_up['mag_tuple']):
            mag += ((i[0][0] + (i[1][0] * lvl), i[0][1] - (i[1][1] * lvl)),)
        fiz = ()
        for i in zip(self.fiz_tuple, self.lvl_up['fiz_tuple']):
            fiz += ((i[0][0] + (i[1][0] * lvl), i[0][1] + (i[1][1] * lvl)),)
        """все источники урона изменены в зависимости от lvl"""
        fiz_armor = float(self.fiz_armor)
        mag_armor = float(self.mag_armor)
        for i in range(lvl):
            fiz_armor = round(fiz_armor + (100 - fiz_armor)/100 * self.lvl_up['fiz_armor'], 5)
            mag_armor = round(mag_armor + (100 - fiz_armor)/100 * self.lvl_up['mag_armor'], 5)
        tup_hp = int(self.hp + self.lvl_up['hp'] * lvl), fiz_armor, mag_armor,
        tup_farm = self.farm_speed + self.lvl_up['farm_speed'] * lvl, self.total_farm + self.lvl_up['total_farm'] * lvl
        return tup_hp, tup_farm, fiz, mag, self.mag_buf


class LocalHero(BaseHero):
    def __init__(self, hp: int, fiz_armor: float, mag_armor: float, farm_speed: int, total_farm: int,
                 fiz_tuple: tuple, mag_tuple: tuple, magic_buf: float):
        """ hp: int, farm_speed: int, total_farm: int, fiz_tuple: tuple, mag_tuple: tuple):"""
        super().__init__(hp, farm_speed, total_farm, fiz_tuple, mag_tuple, magic_buf)
        self.mag_armor = mag_armor
        self.fiz_armor = fiz_armor

    def no_items(self):
        dick = {
            'hp': self.hp,
            'farm_speed': self.farm_speed,
            'total_farm': self.total_farm,
            'fiz_tuple': self.fiz_tuple,
            'mag_tuple': self.mag_tuple,
            'mag_buf': self.mag_buf,
            'mag_armor': self.mag_armor,
            'fiz_armor': self.fiz_armor,

        }
        return dick

    @staticmethod
    def battle(dick1, dick2):
        """быть"""
        # я хочу использовать die second, но мне нужны данные в формате проходящий урон
        print()
        # print(dick1['fiz_tuple'])
        # print(dick2['fiz_tuple'][0][0])
        # print(dick2['fiz_armor'])
        # print(dick2['fiz_tuple'][0][0] * (100-dick2['fiz_armor'])/100)
        fiz_dmg1 = [[dick2['fiz_tuple'][0][0] * (100-dick2['fiz_armor'])/100, i[1], 0] for i in dick1['fiz_tuple']]
        mag_dmg1 = [[round(i[0] * (100 - dick2['mag_armor']/100), 5), i[1], 0] for i in dick1['mag_tuple']]
        fiz_dmg2 = [[dick1['fiz_tuple'][0][0] * (100-dick1['fiz_armor'])/100, i[1], 0] for i in dick2['fiz_tuple']]
        mag_dmg2 = [[round(i[0] * (100 - dick1['mag_armor']/100), 5), i[1], 0] for i in dick2['mag_tuple']]
        print(dick2['hp'], fiz_dmg1+mag_dmg1)
        print(dick1['hp'], fiz_dmg2+mag_dmg2)
        seconds1 = die_second1(dick2['hp'], fiz_dmg1)  # + mag_dmg1)
        seconds2 = die_second1(dick1['hp'], fiz_dmg2)  # + mag_dmg2)
        return seconds1, seconds2


class BaseItem:
    def __init__(self, hp: int or None, fiz_armor: float or None, mag_armor: float or None,
                 fiz_tuple: tuple or None, mag_tuple: tuple or None, mag_buf: float or None,
                 farm_speed: int or None, total_farm: int or None, ):
        self.hp = hp
        self.farm_speed = farm_speed
        self.total_farm = total_farm
        self.fiz_tuple = fiz_tuple
        self.mag_tuple = mag_tuple
        self.mag_buf = mag_buf
        self.fiz_armor = fiz_armor
        self.mag_armor = mag_armor

    def __mul__(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')


class ShopItem(BaseItem):
    def __init__(self, price: int, name: str, description: str or None, img1: str or None, img2: str or None,
                 main_stat: int or None,
                 hp: int or None, fiz_armor: float or None, mag_armor: float or None,
                 fiz_tuple: tuple or None, mag_tuple: tuple or None, mag_buf: float or None,
                 farm_speed: int or None, total_farm: int or None,):
        super().__init__(hp, fiz_armor, mag_armor, fiz_tuple, mag_tuple, mag_buf, farm_speed, total_farm)
        self.main_stat = main_stat
        self.price = price
        self.description = description
        self.name = name
        self.img1 = img1
        self.img2 = img2

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other: dict) -> dict:
        end_fiz_tup = ()
        """Вернёт изменённую в зависимости от героя информацию для создания FightItem"""
        for i in other['fiz_tuple']:
            # print(i[0])
            fiz_damage = i[0] + self.fiz_tuple[0] if self.fiz_tuple[0] else i[0]
            fiz_speed = i[1] - self.fiz_tuple[1] if self.fiz_tuple[1] else i[1]
            end_fiz_tup += ((fiz_damage, fiz_speed),)

        end_mag_tup = ()
        """тут нельзя нечего умножать иначе когда будет 6 предметов будет *6 kef главного атрибута"""
        for i in other['mag_tuple']:
            mag_damage = (self.mag_tuple[0] + other['mag_tuple'][0]) \
                if self.mag_tuple[0] else i[0]
            mag_speed = self.mag_tuple[0] - other['mag_tuple'][0] if self.mag_tuple[1] else i[1]
            end_mag_tup += ((mag_damage, mag_speed),)

        dick = {
            'hp': other['hp'] + self.hp if self.hp else other['hp'],
            'farm_speed': other['farm_speed'] + self.farm_speed if self.farm_speed else other['farm_speed'],
            'total_farm': other['total_farm'] + self.total_farm if self.total_farm else other['total_farm'],
            'fiz_tuple': end_fiz_tup,
            'mag_tuple': end_mag_tup,
            'mag_buf': self.mag_buf + other['mag_buf'] if self.mag_buf else other['mag_buf'],
            'mag_armor': round(other['mag_armor'] + (self.mag_armor * (100 - other['fiz_armor']) / 100), 5)
            if self.mag_armor else other['mag_armor'],
            'fiz_armor': round(self.fiz_armor + (other['fiz_armor'] * (100 - other['fiz_armor']) / 100), 5)
            if self.fiz_armor else other['fiz_armor'],
        }
        return dick


def die_second1(hp: int, timers: list) -> int and float:
    """[[dmg, time, count],[10, 0.47, 0]]"""
    dmg = sum([i[0] for i in timers])
    seconds = 0
    timers.sort(key=lambda k: k[1])
    small = timers[0][1]
    a = len(str(small))
    b = len(str(int(small)))
    row = a-b-1

    while dmg < hp:
        for i in timers:
            if seconds // i[1] > i[2]:
                i[2] += 1
                dmg = round(dmg+i[0], 5)
            else:
                break
        seconds = round(seconds + small, row)
    return dmg, 5, round(seconds, 5)


def die_second2(hp: int, timers: list) -> float:
    """test_arr = [[22, 0.47123, 0], [10, 0.3331212, 0], [100, 12.123123,  0], [321, 10.81283, 0]]"""
    speeds = [i[0] / i[1] for i in timers]
    return round(hp / sum(speeds), 3)

import time


class BaseHero:
    """def __init__(self, name: str, price: int, img1: str, img2: str, img3: str):"""
    def __init__(self, hp: int, fiz_hp: int, mag_hp: int, farm_speed: int, total_farm: int,
                 fiz_damage: int, attack_speed: float, magic_damage: int, magic_speed: float):
        # mag_hp: int, fiz_hp:int,
        self.hp = hp
        self.fiz_hp = fiz_hp
        self.mag_hp = mag_hp

        self.farm_speed = farm_speed
        self.total_farm = total_farm

        self.fiz_dmg = fiz_damage
        self.attack_speed = attack_speed
        self.mag_dmg = magic_damage
        self.mag_speed = magic_speed

    def __lt__(self, *args, **kwargs) -> Exception:
        return Exception('фигню сделал')

    @classmethod
    def local_dict(cls):
        return dict(cls.__dict__)

    def lvlup_hero(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')

    def select_hp(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')


class NewHero(BaseHero):
    def __init__(self, name, price, description: str or None, img1, img2, img3, #интерфейс
                 hp: int, fiz_hp: int, mag_hp: int, # базовые хп
                 farm_speed: int, total_farm: int, kef_farm: float,
                 fiz_damage: int, attack_speed: float, fiz_buf: float,
                 magic_damage: int, magic_speed: float, magic_buf: float, # базовый fight
                 exp: int, lvl_up: dict): # для lvl up
        super().__init__(hp, # базовое здоровье
                         farm_speed, total_farm, # base farm
                         fiz_damage, magic_damage,) # base dmg
        """интерфейс"""
        self.name = name
        self.price = price
        self.description = description
        self.img = img1
        self.good = img2
        self.bad = img3
        """коэффициенты"""
        self.kef_farm = kef_farm
        self.fiz_buf = fiz_buf
        self.magic_buf = magic_buf
        """лвл апы"""
        self.exp = exp
        self.lvl_up = lvl_up

    def select_hp(self) -> tuple:
        mag_hp = self.hp * self.fiz_armor
        fiz_hp = self.hp * self.fiz_hp / 100
        tup = mag_hp, fiz_hp
        return tup

    def lvlup_hero(self, lvl) -> tuple:
        """ exp, hp, fiz_armor, mag_armor, fiz_damage, attack_speed, magic_damage, magic_speed"""
        '''прибавки за уровень локального героя'''
        # нужно узнать сколько сейчас лвл exp: базовый + сколько накапало за уровни
        # мы прибавили уровень и обнулили эксп, это нужно вернуть
        tup = int(self.hp + self.lvl_up['hp'] * lvl),\
            int(self.fiz_armor + self.lvl_up['fiz_armor'] * lvl),\
            int(self.mag_armor + self.lvl_up['mag_armor'] * lvl),\
            int(self.fiz_dmg + self.lvl_up['fiz_damage'] * lvl),\
            int(self.attack_speed + self.lvl_up['attack_speed'] * lvl),\
            int(self.mag_dmg + self.lvl_up['magic_damage'] * lvl),\
            int(self.mag_speed + self.lvl_up['magic_speed'] * lvl),

        return tup

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
    def __init__(self, hp: int, fiz_damage: int, attack_speed: float, magic_damage: int, magic_speed: float,
                 mag_hp: int, fiz_hp: int,):
        """hp: int, fiz_damage: int, attack_speed: float, magic_damage: int, magic_speed: float"""
        super().__init__(hp, fiz_damage, attack_speed, magic_damage, magic_speed)
        self.mag_hp = mag_hp
        self.fiz_hp = fiz_hp
        """физика"""

    def __lt__(self, other: object) -> bool or Exception:
        if not isinstance(other, LocalHero):
            return Exception('нужен LocalHero')
        print(self.select_hp())
        print(other.select_hp())
        return False


class BaseItem:
    pass


tup = (10, 0.5,), (30, 1)


def die_second1(hp: int, timers: list) -> float:
    """[[dmg, time, count],[10, 0.47, 0]]"""
    dmg = sum([i[0] for i in timers])
    seconds = 0
    # нужно найти самую маленькую единицу
    timers.sort(key=lambda k: k[1])
    small = timers[0][1]
    # small - 0.33 cek
    """"""
    while dmg < hp:
        for i in timers:
            #print(i, seconds // i[1], i[2])
            if seconds // i[1] > i[2]:
                #print(seconds)
                #print(i[2])
                i[2] += 1
                dmg += i[0]
        #print()
        seconds = round(seconds+small, 5)
    return dmg, seconds
def die_second2(hp: int, timers: list) -> float:
    """[[dmg, time, count],[10, 0.47, 0]]"""
    speeds = [i[0]/i[1] for i in timers]
    return hp/sum(speeds)

test_arr = [[2, 0.47, 0], [1, 0.33, 0], [999.0, 1,  0]]
#t = dat
print(die_second1(999999, test_arr))
#print(die_second2(1000, test_arr))

class Item:
    pass
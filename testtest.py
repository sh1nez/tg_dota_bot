class DifferentLens(Exception):
    """Нельзя использовать разные длины buffs"""

    def __init__(self, *args, **kwargs):
        print(*args, **kwargs)
        print('загляни в lvlup_hero, длины кортежей check')


class BaseHero:
    """def __init__(self, name: str, price: int, img1: str, img2: str, img3: str):"""
    __rd = 5
    __max_as = 1000
    __max_sec = 5
    __min_sec = 0.1

    def __init__(self, hp: int, farm_speed: int, total_farm: int, fiz_tuple: tuple, mag_tuple: tuple,
                 magic_buf: float, fiz_buf: float):
        # mag_hp: int, fiz_hp:int,
        self.hp = hp

        self.farm_speed = farm_speed
        self.total_farm = total_farm

        self.fiz_tuple = fiz_tuple
        self.mag_tuple = mag_tuple
        self.mag_buf = magic_buf
        self.fiz_buf = fiz_buf

    def __mul__(self, other) -> Exception:
        return Exception('фигню сделал')

    @classmethod
    def local_dict(cls):
        return dict(cls.__dict__)

    def lvlup_hero(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')

    def no_items(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')

    def battle(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')

    def die_second1(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')

    def die_second2(self, *args, **kwargs) -> Exception:
        return Exception('не тот класс')


class NewHero(BaseHero):
    __rd = 5
    __min_farm_time = 1800
    __max_farm_time = 3600 * 4
    __max_farm_speed = 550

    def __init__(self, name: str, price: int, description: str or None, img1, img2, img3,  # интерфейс
                 hp: int, fiz_armor: float, mag_armor: float,  # базовые хп
                 farm_speed: int, total_farm: int, kef_farm: float,
                 fiz_tuple: tuple, fiz_buf: float,  # attack_speed: float,
                 mag_tuple: tuple, mag_buf: float,  # mag_tuple - (dmg, sec), (20, 0.57)
                 exp: int, lvl_up: dict):  # для lvl up
        """self, hp: int, farm_speed: int, total_farm: int,
                 fiz_damage: int, attack_speed: float, mag_damage: int, mag_speed: float):"""
        super().__init__(hp, farm_speed, total_farm,
                         fiz_tuple, mag_tuple, mag_buf, fiz_buf)  # base dmg
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
        """лвл апы"""
        self.exp = exp  # ~300-500
        self.lvl_up = lvl_up  # tuple buffs

    def max_min_time(self): return self.__max_farm_time, self.__min_farm_time
    def max_farm_speed(self): return self.__max_farm_speed
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
            fiz_armor = round(fiz_armor + (100 - fiz_armor) / 100 * self.lvl_up['fiz_armor'], self.__rd)
            mag_armor = round(mag_armor + (100 - fiz_armor) / 100 * self.lvl_up['mag_armor'], self.__rd)
        tup_hp = int(self.hp + self.lvl_up['hp'] * lvl), fiz_armor, mag_armor
        tup_farm = self.farm_speed + self.lvl_up['farm_speed'] * lvl, self.total_farm + self.lvl_up['total_farm'] * lvl
        buffs = self.mag_buf, self.fiz_buf
        return tup_hp, tup_farm, fiz, mag, buffs

    def description(self) -> str:
        text = ''
        return str('a')


class LocalHero(BaseHero):
    __rd = 5
    __max_as = 1000
    __max_sec = 5
    __min_sec = 0.1

    def __init__(self, hp: int, fiz_armor: float, mag_armor: float, farm_speed: int, total_farm: int,
                 fiz_tuple: tuple, mag_tuple: tuple, magic_buf: float, fiz_buf: float):
        """ hp: int, farm_speed: int, total_farm: int, fiz_tuple: tuple, mag_tuple: tuple):"""
        super().__init__(hp, farm_speed, total_farm, fiz_tuple, mag_tuple, magic_buf, fiz_buf)
        self.mag_armor = mag_armor
        self.fiz_armor = fiz_armor

    def no_items(self) -> dict:
        dick = {
            'hp': self.hp,
            'farm_speed': self.farm_speed,
            'total_farm': self.total_farm,
            'fiz_tuple': self.fiz_tuple,
            'mag_tuple': self.mag_tuple,
            'mag_buf': self.mag_buf,
            'fiz_buf': self.fiz_buf,
            'mag_armor': self.mag_armor,
            'fiz_armor': self.fiz_armor,
        }
        return dick

    def battle(self, dick1: dict, dick2: dict) -> tuple:
        """Возвращает урон и секунды fight"""
        """первый
        __max_as = 1000
        __max_sec = 10
        __min_sec = 0.1
        """

        def num(n):
            if n >= self.__max_as:
                return self.__min_sec
            return round(self.__max_sec - ((self.__max_sec - self.__min_sec) * n / self.__max_as), self.__rd)

        fiz_dmg1 = [[round(i[0] * (100 - dick2['fiz_armor']) / 100 * dick1['fiz_buf'], self.__rd), num(i[1]), 0]
                    for i in dick1['fiz_tuple']]
        mag_dmg1 = [[round(i[0] * ((100 - dick2['mag_armor']) / 100 * dick1['mag_buf']), self.__rd), i[1], 0]
                    for i in dick1['mag_tuple']]
        """второй"""
        fiz_dmg2 = [[round(i[0] * (100 - dick1['fiz_armor']) / 100 * dick2['fiz_buf'], self.__rd), num(i[1]), 0]
                    for i in dick2['fiz_tuple']]
        mag_dmg2 = [[round(i[0] * (100 - dick1['mag_armor']) / 100 * dick2['mag_buf'], self.__rd), i[1], 0]
                    for i in dick2['mag_tuple']]
        # print(fiz_dmg1, 'пудж', fiz_dmg2, 'негр')
        # print(mag_dmg1, mag_dmg2)
        seconds1 = self.die_second1(dick2['hp'], fiz_dmg1 + mag_dmg1)  # + mag_dmg1)
        seconds2 = self.die_second1(dick1['hp'], fiz_dmg2 + mag_dmg2)  # + mag_dmg2)
        # seconds1_1 = self.die_second2(dick2['hp'], fiz_dmg1 + mag_dmg1)
        # seconds1_2 = self.die_second2(dick1['hp'], fiz_dmg2 + mag_dmg2)
        return seconds1, seconds2

    def die_second1(self, hp: int, timers: list) -> tuple:
        """[[dmg, time, count],[10, 0.47, 0]]"""
        dmg = sum([i[0] for i in timers])
        seconds = 0
        timers.sort(key=lambda k: k[1])
        small = timers[0][1]
        while dmg < hp:
            for i in timers:
                if seconds // i[1] > i[2]:
                    i[2] += 1
                    dmg = round(dmg + i[0], self.__rd)
                else:
                    break
            seconds = round(seconds + small, self.__rd)
        return dmg, round(seconds, self.__rd)

    def die_second2(self, hp: int, timers: list) -> float:
        """test_arr = [[22, 0.47123, 0], [10, 0.3331212, 0], [100, 12.123123,  0], [321, 10.81283, 0]]"""
        speeds = [i[0] / i[1] for i in timers]
        return round(hp / sum(speeds), self.__rd)


class BaseItem:
    __rd = 5

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

    def __rmul__(self, other):
        return self.__mul__(other)


class ShopItem(BaseItem):
    __rd = 5
    """индекс нужен для того чтобы при разделении предметов всёравно иметь возможность обращаться к общему словарю"""
    def __init__(self, index: int,  price: int, name: str, description: str or None, img1: str or None,
                 img2: str or None, main_stat: int or None,
                 hp: int or None, fiz_armor: float or None, mag_armor: float or None,
                 fiz_tuple: tuple or None, mag_tuple: tuple or None, mag_buf: float or None,
                 farm_speed: int or None, total_farm: int or None, ):
        super().__init__(hp, fiz_armor, mag_armor, fiz_tuple, mag_tuple, mag_buf, farm_speed, total_farm)
        self.index = index
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
            fiz_damage = round(i[0] + self.fiz_tuple[0] if self.fiz_tuple[0] else i[0], self.__rd)
            fiz_speed = round(i[1] + self.fiz_tuple[1] if self.fiz_tuple[1] else i[1])
            end_fiz_tup += ((fiz_damage, fiz_speed),)
        print(other['mag_tuple'])
        print(self.mag_tuple[0])
        end_mag_tup = other['mag_tuple']
        if self.mag_tuple[0]:
            end_mag_tup += self.mag_tuple
        """тут нельзя нечего умножать иначе когда будет 6 предметов будет *6 kef главного атрибута"""
        # for i in other['mag_tuple']:
        #     mag_damage = (self.mag_tuple[0] + other['mag_tuple'][0]) \
        #         if self.mag_tuple[0] else i[0]
        #     mag_speed = self.mag_tuple[0] - other['mag_tuple'][0] if self.mag_tuple[1] else i[1]
        #     end_mag_tup += ((mag_damage, mag_speed),)

        dick = {
            'hp': other['hp'] + self.hp if self.hp else other['hp'],
            'farm_speed': other['farm_speed'] + self.farm_speed if self.farm_speed else other['farm_speed'],
            'total_farm': other['total_farm'] + self.total_farm if self.total_farm else other['total_farm'],
            'fiz_tuple': end_fiz_tup,
            'mag_tuple': end_mag_tup,
            'mag_buf': self.mag_buf + other['mag_buf'] if self.mag_buf else other['mag_buf'],
            'fiz_buf': other['fiz_buf'],
            'mag_armor': round(other['mag_armor'] + (self.mag_armor * (100 - other['fiz_armor']) / 100), self.__rd)
            if self.mag_armor else other['mag_armor'],
            'fiz_armor': round(self.fiz_armor + (other['fiz_armor'] * (100 - other['fiz_armor']) / 100), self.__rd)
            if self.fiz_armor else other['fiz_armor'],
        }
        return dick


dagon = ShopItem(index=3, price=3000, name='дагон', description=None, img1=None, img2=None,
                 main_stat=None, hp=150,
                 fiz_armor=None, mag_armor=None, fiz_tuple=(None, None), mag_tuple=((500, 15),),
                 mag_buf=0.3, farm_speed=None, total_farm=None)

pudge_urls = ('https://cq.ru/storage/uploads/images/1530144/cri/1___media_library_original_1018_636.jpg',)
pudge_disc = 'тут и говорить нечего, имба'
pudge_dick = {'exp': 300, 'hp': 50, 'fiz_armor': 1, 'mag_armor': 1,
              'fiz_tuple': ((5, 2),), 'mag_tuple': ((1, 0),),
              'total_farm': 3, 'farm_speed': 1, }
pudge = NewHero(name='пудж', price=0, description=pudge_disc, img1=pudge_urls[0], img2=None, img3=None,
                hp=1000, fiz_armor=20, mag_armor=26,
                farm_speed=150, total_farm=80, kef_farm=1.5, fiz_tuple=((50, 50),), mag_tuple=((10, 0.5,),),
                fiz_buf=0.7, mag_buf=1.5, exp=1000, lvl_up=pudge_dick)
midas_urls = (
    'https://avatars.dzeninfra.ru/get-zen_doc/3126430/pub_604f9ae70a7d51654a5834d3_604f9b59011181447bd702d5/scale_1200',
)
midas = ShopItem(index=0, price=2250, name='мидас', description=None, img1=midas_urls[0], img2=None, main_stat=None, hp=None,
                 fiz_armor=None, mag_armor=None, fiz_tuple=(50, 30), mag_tuple=(None, None),
                 mag_buf=None, farm_speed=None, total_farm=150)

hp1, farm1, fiz_dmg1, mag_dmg1, buffs1 = pudge.lvlup_hero(10)
hero1 = LocalHero(*hp1, *farm1, fiz_dmg1, mag_dmg1, *buffs1)
print(hero1.__dict__)
print(a := hero1.__dict__*dagon)
print(a*midas)

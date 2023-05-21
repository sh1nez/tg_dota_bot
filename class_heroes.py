# class Hero:
#     def __init__(self, index, name):
#         self.index = index
#         self.name = name
#
#     def send_nudes(self):
#         return [self.name]
#
# class Test_Stats_hero(Hero):
# #ещё нужно добавить кэф маг и физ урона. Чтобы на дизрапторе не собирались в физ а на антимаге в маг
#     def __init__(self, index, name, hp, damage, lvl_up):
#         super().__init__(index, name)
#         self.hp = hp
#         self.damage = damage
#         self.up = lvl_up
#     def send_nudes(self):
#         return [self.hp, self.damage]
#     def lvl_up(self, lvl):
#         lvl = float(lvl)
#         return [self.hp+self.hp*self.up[0]*lvl,
#                 self.damage+self.damage+self.up[1]*lvl
#                 ]
# ##!!это сложно добавить потом
# # class Stats_hero(Hero):
# #     def __init__(self, index, name, main_stat, esc, fiz_damage, magic_gamage, farm, fiz_hp, mag_hp, lvl_up):
# #         super().__init__(index, name)
# #         self.stat = main_stat
# #         self.esc = esc
# #         self.fizik = fiz_damage
# #         self.magic = magic_gamage
# #         self.farm = farm
# #         self.mag_hp = mag_hp
# #         self.fiz_hp = fiz_hp
# #         self.up = lvl_up
# #     def send_nudes(self):
# #         return [self.index, self.stat, self.esc, self.fizik, self.magic, self.farm, self.mag_hp, self.fiz_hp]
# #     def lvl_up(self, lvl):
# #         lvl = float(lvl)
# #         return [self.index, self.stat,
# #                 int(float(self.esc)+(float(self.up[0])*lvl)),
# #                 int(float(self.fizik)+(float(self.up[1])*lvl)),
# #                 int(float(self.magic)+(float(self.up[2])*lvl)),
# #                 int(float(self.farm)+(float(self.up[3])*lvl)),
# #                 int(float(self.farm) + (float(self.up[3]) * lvl)),
# #                 int(float(self.farm) + (float(self.up[3]) * lvl)),
# #                 ]
# class Info_hero:
#     def __init__(self, price, name, description, stats, img, event_img):
#         self.price = price
#         self.name = name
#         self.description = description
#         self.stats = stats
#         self.img = img
#         self.event_img = event_img
#
# pudge = Info_hero(8800, 'пудж', 'самый секс перс доты имба покупай', 'много статов', r'https://cq.ru
# /storage/uploads/images/1530144/1.jpg',
#  https://hsto.org/getpro/habr/post_images/6fc/750/e38/6fc750e38c21f9dc6a777c15cbf4be43.jpg")

class BaseHero:
    def __init__(self, name: str, price: int, ):
        self.name = name
        self.price = price
    # def __new__(cls, *args, **kwargs):

    def send_description(self, *args, **kwargs) -> Exception:
        return Exception('это BaseHero')

    def send_text(self, *args, **kwargs) -> Exception:
        return Exception('это BaseHero')

    def calculate(self, *args, **kwargs) -> Exception:
        return ValueError('это BaseHero')

    def lvlup(self, *args, **kwargs):
        pass


class HeroNew(BaseHero):
    def __init__(self, name: str, price: int, description: str or None, img: str, good_event: str, bad_event: str,
                 magic_damage_kef: float,  fiz_damage_kef: float, total_mag_d: int, total_fiz_d: int,
                 farm: float, total_farm: int, hp: int, lvl_up: tuple):
        super().__init__(name, price)
        self.description = description
        self.farm_t = total_farm
        self.farm_k = farm  # 0-2
        self.kef_mag = magic_damage_kef  # 0-2
        self.kef_fiz = fiz_damage_kef  # 0-2
        self.total_mag = total_mag_d
        self.total_fiz = total_fiz_d
        self.hp = hp
        self.lvl_up = lvl_up
        self.img = img
        self.good = good_event
        self.bad = bad_event

    def send_description(self):
        desc = self.description+'\n' if self.description else ''
        text = f"Это {self.name}, он стоит {self.price}\n{desc}" \
               f"Базовые:\n Хп - {self.hp}, фрам\n" \
               f"Потанцевалы:\n" \
               f"Фрам - {int(self.farm_k*50)}%, файт - {int((self.fizd+self.magd)*25)}%\n" \
               f"Урон:\n{int(self.fizd*50)}% - физ, {int(self.magd*50)}% - маг"
        return text

    def send_text(self) -> str:
        text = f"это {self.name}, он стоит "  # {self.price}"
        text += f"{self.description}"
        return text

    def lvlup(self, lvl) -> str:  # magic, fiz damage, hp, farm
        pass  # return

    def calculate(self):
        return 1+1


pudge_lvlup = (1, 2, 3,)
pudge = HeroNew('пудж', 8800, 'имба', 'url', 'url2', 'url3', 0.9, 0.55, 0.9, 1000, pudge_lvlup)
sf_lvlup = ((3, 2, 1),)
sf_urls = ('url', 'url2', 'url3')
sf_stats = (1.5, 1.5, 50, 50, 1.0, 50, 500)  # 7 штук
'''   mag_k, fiz_k, t_mag,t_fiz,farm, t_farm, hp'''
sf = HeroNew('сф', 10000, None, *sf_urls, *sf_stats, *sf_lvlup)

"""name, price, description, img, good_event, bad_event, magic_damage_kef, fiz_damage_kef,
    total_mag_d, total_fiz_d, farm, total_farm, hp, lvl_up"""

print(pudge.send_description())
print()
print(sf.send_description())

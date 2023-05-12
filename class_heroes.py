class Hero:
    def __init__(self, index, main_stat, esc, fiz_damage, magic_gamage, farm, fiz_hp, mag_hp, lvl_up):
        self.index = index
        self.stat = main_stat
        self.esc = esc
        self.fizik = fiz_damage
        self.magic = magic_gamage
        self.farm = farm
        self.mag_hp = mag_hp
        self.fiz_hp = fiz_hp
        self.up = lvl_up
    def send_nudes(self):
        return [self.index, self.stat, self.esc, self.fizik, self.magic, self.farm, self.mag_hp, self.fiz_hp]
    def lvl_up(self, lvl):
        lvl = float(lvl)
        return [self.index, self.stat,
                int(float(self.esc)+(float(self.up[0])*lvl)),
                int(float(self.fizik)+(float(self.up[1])*lvl)),
                int(float(self.magic)+(float(self.up[2])*lvl)),
                int(float(self.farm)+(float(self.up[3])*lvl)),
                int(float(self.farm) + (float(self.up[3]) * lvl)),
                int(float(self.farm) + (float(self.up[3]) * lvl)),
                ]

class Test_hero:
    def __init__(self, hp, damage, lvl_up):
        self.hp = hp
        self.damage = damage
        self.up = lvl_up
    def send_nudes(self):
        return [self.hp, self.damage]
    def lvl_up(self, lvl):
        lvl = float(lvl)
        return [self.hp+self.hp*self.up[0]*lvl,
                self.damage+self.damage+self.up[1]*lvl
                ]


#пусть универсал - 0, сила - 1, ловкость -2, интеллект 3
pudge_lvl_up = [1,2]
pudge = Test_hero(10, 10, pudge_lvl_up)

test_heroes = [
    pudge
]

#слишком сложно для школяра, сначала проще сделаю
# pudge_lvl = 5
# pudge_lvl_up = [0, 1, 2, 2, 1, 1]
# pudge = Hero(index=0, main_stat=1, esc=5, fiz_damage=10, magic_gamage=15, farm=30, fiz_hp=10, mag_hp=10, lvl_up=pudge_lvl_up,)
# #тут у  меня будут заданы все герои с их базовым характеристиками
# #это мы не меняем, тут у нас всегда определённые статы (кроме патчей)
# #print(50/30)
# antimage_lvl_up = [5, 3, 1, 1.6]
# antimage = Hero(index=1, main_stat=2, esc=20, fiz_damage=5, magic_gamage=3, farm=50, fiz_hp=1, mag_hp=15, lvl_up=antimage_lvl_up)
# void_spirit_lvl_up = [1, 2.5, 2.5, 1]
# void_spirit = Hero(index=2,main_stat=3, esc=15, fiz_damage=25, magic_gamage=25, farm=10, lvl_up=void_spirit_lvl_up )
# heroes = [
#     pudge,
#     antimage
# ]
#
# print('пудж 0 лвл', heroes[0].send_nudes())
# print('пудж 5 лвл', heroes[0].lvl_up(5))
# asd = heroes[0].lvl_up(5)
# dick = {}
# #for i in asd:
    #dick.items()
#эта хуйня должна возвращать текущие значения героя. то есть например у пуджа васи будет 10 лвл.
#тогда мы берём данные с героя, помножаем их на кэф васи, и возвращаем текущие данные его героя
#самого героя мы никак не возвращаем и не меняем
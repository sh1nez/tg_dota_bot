class Hero:
    def __init__(self, index, main_stat, esc, fiz_damage, magic_gamage, farm, lvl_up):
        self.index = index
        self.stat = main_stat
        self.esc = esc
        self.fizik = fiz_damage
        self.magic = magic_gamage
        self.farm = farm
        self.up = lvl_up
    def send_nudes(self):
        return [self.index, self.stat, self.esc, self.fizik, self.magic, self.farm]
    def lvl_up(self, lvl):
        lvl = float(lvl)
        return [self.index, self.stat,
                int(float(self.esc)+(float(self.up[0])*lvl)),
                int(float(self.fizik)+(float(self.up[1])*lvl)),
                int(float(self.magic)+(float(self.up[2])*lvl)),
                int(float(self.farm)+(float(self.up[3])*lvl))
                ]
#пусть универсал - 0, сила - 1, ловкость -2, интеллект 3
pudge_lvl = 5
pudge_lvl_up = [0, 1, 3, 2]
pudge = Hero(index=0, main_stat=1, esc=5, fiz_damage=10, magic_gamage=15, farm=30, lvl_up=pudge_lvl_up,)
#тут у  меня будут заданы все герои с их базовым характеристиками
#это мы не меняем, тут у нас всегда определённые статы (кроме патчей)
#print(50/30)
antimage_lvl_up = [5, 7.5, 1, 1.6]
antimage = Hero(index=1, main_stat=2, esc=20, fiz_damage=5, magic_gamage=3, farm=50, lvl_up=antimage_lvl_up)
sf_lvl_up = []
sf = Hero()
heroes = [
    pudge,
    antimage
]

print('пудж 0 лвл', heroes[0].send_nudes())
print('пудж 5 лвл', heroes[0].lvl_up(5))
asd = heroes[0].lvl_up(5)
dick = {}
#for i in asd:
    #dick.items()
#эта хуйня должна возвращать текущие значения героя. то есть например у пуджа васи будет 10 лвл.
#тогда мы берём данные с героя, помножаем их на кэф васи, и возвращаем текущие данные его героя
#самого героя мы никак не возвращаем и не меняем
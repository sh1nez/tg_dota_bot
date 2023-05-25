from dota import *
from texts import hero_dick, all_items


def pvp(hero_id1: int, lvl1: int, items1: tuple or None, hero_id2: int, lvl2: int, items2: tuple[ShopItem] or None):
    hp1, farm1, fiz_dmg1, mag_dmg1, buffs1 = hero_dick[hero_id1].lvlup_hero(lvl1)
    hero1 = LocalHero(*hp1, *farm1, fiz_dmg1, mag_dmg1, *buffs1)

    if not items1:
        local_hero1 = hero1.no_items()
    else:
        local_hero1 = hero1.__dict__
        for i in items1:
            local_hero1 *= all_items[i]

    hp2, farm2, fiz_dmg2, mag_dmg2, buffs2 = hero_dick[hero_id2].lvlup_hero(lvl2)
    hero2 = LocalHero(*hp2, *farm2, fiz_dmg2, mag_dmg2, *buffs2)
    if not items2:
        local_hero2 = hero2.no_items()
    else:
        local_hero2 = hero2.__dict__
        for i in items2:
            local_hero2 *= all_items[i]

    return hero1.battle(local_hero1, local_hero2)


print(pvp(hero_id1=0, lvl1=10, items1=None, hero_id2=1, lvl2=10, items2=None))

class Item():
    def __init__(self, price, main_stat, index):
        self.stat = main_stat
        self.price = price
        self.index = index
    def send_item(self):
        return self.stat, self.price, self.index
    class Farm_Items():
        def __init__(self, farm, mobilit):
            self.farm = farm
            self.mobil_farm = mobilit
        def send_farm(self):
            return self.farm, self.mobil_farm
    class Fight_items():
        def __init__(self, helth, magic_damage, fiz_damage, esc, control):
            self.hp = helth
            self.mag_damage = magic_damage
            self.fiz_damage = fiz_damage
            self.esc = esc
            self.control = control
    class Ultimate_items():
        def __init__(self, farm, mobility, esc, helth, magic_damage, fiz_damage, control):
            self.hp = helth
            self.mag_damage = magic_damage
            self.fiz_damage = fiz_damage
            self.esc = esc
            self.farm = farm
            self.mobil_farm = mobility

topor =  Item(price=100, main_stat=0, index=0)\
    .Farm_Items(farm=10, mobilit=1.1)
midas = Item(price=2250, main_stat=0, index=1)\
    .Farm_Items(farm=100, mobilit=1)
test_class_items = [
    topor,
    midas
]

print(topor.send_farm())
#print(Item.Farm_Items.topor)


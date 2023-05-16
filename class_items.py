class Item:
    def __init__(self, name, description, price, main_stat, index,farm, fight, helth, damage):
        self.name = name
        self.description = description
        self.stat = main_stat
        self.price = price
        self.index = index
        self.farm = farm
        self.fight = fight
        self.helth = helth
        self.damage = damage
    def send_item(self):
        return self.stat, self.price, self.index
# class Farm_items(Item):
#     def __init__(self, name, description, price, main_stat, index, farm):
#         super().__init__(name, description, price, main_stat, index,)
#         self.farm = farm
#         #self.mobil_farm = mobilit
#     def send_item(self):
#         return self.farm, self.price, self.stat, self.index
# class Fight_items(Item):
#     def __init__(self, name, description, price, main_stat, index, helth, damage,): #magic_ fiz_damage):#, esc, control):
#         super().__init__(name, description, price, main_stat, index)
#         self.hp = helth
#         self.damage = damage
#         #self.fiz_damage = fiz_damage
#         # self.esc = esc
#         # self.control = control
# class Ultimate_items(Item):
#     def __init__(self,name, description,  price, main_stat, index, farm, helth, damage):#esc,, control, mobility,magic_damage, fiz_
#         super().__init__(name, description, price, main_stat, index)
#         self.hp = helth
#         self.damage = damage
#         #self.fiz_damage = fiz_damage
#         self.farm = farm
#(name, description, price, main_stat, index,farm, fight, helth, damage)
topor = Item(name='топор', description='да это мой топор', price='100',main_stat=0, index,farm, fight, helth, damage)
desolator = Item(index=1, price=3500,main_stat=0, damage=20, helth=0, description='', name='')
vetochka = Item(price=50, main_stat=0, damage=1, index=2, helth=1, farm=1, description='', name='')

test_class_items = [
    topor,
    desolator,
    vetochka
]
for i in test_class_items:
    print(i.__dict__)
    print(type(i))
#print(topor.send_farm())
#print(Item.Farm_Items.topor)


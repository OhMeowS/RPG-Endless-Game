
# coding: utf-8
import colorama
import random
import json
import jsonpickle
import time
from cryptography.fernet import Fernet
from types import SimpleNamespace
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import functools
from colorama import just_fix_windows_console
import curses
just_fix_windows_console()

#version
global version
global chicky
version = "0.1"
chicky = 0
class Item:
    def __init__(self, name, max_health, defence, damage, udamage, speed, critD, critC, Regen, Abs, StunC, Vampirism, hpdamage, Vampirism_hp, sety, c_type, price, upgrade, picture):
        self.name = name
        self.max_health = max_health
        self.defence = defence
        self.damage = damage
        self.udamage = udamage
        self.speed = speed
        self.critD = critD
        self.critC = critC
        self.Regen = Regen
        self.Abs = Abs
        self.StunC = StunC
        self.Vampirism = Vampirism
        self.hpdamage = hpdamage
        self.Vampirism_hp = Vampirism_hp
        self.sety = sety
        self.c_type = c_type
        self.price = price
        self.upgrade = upgrade
        self.picture = picture
#    def to_json(self):
#        return self.__str__()
    def __str__(self):
        return f"{self.name}"
#    @classmethod
#    def from_json(cls, data):
#        return cls(**data)
#    @staticmethod
#    def from_json(json_dct):
#      return Item(json_dct['name'],
#                  json_dct['max_health'], json_dct['defence'],
#                  json_dct['damage'], json_dct['udamage'],
#                  json_dct['speed'], json_dct['critD'],
#                  json_dct['critC'], json_dct['Regen'],
#                  json_dct['Abs'], json_dct['StunC'],
#                  json_dct['Vampirism'], json_dct['hpdamage'],
#                  json_dct['Vampirism_hp'], json_dct['sety'],
#                  json_dct['c_type'], json_dct['price'],
#                  json_dct['price'], json_dct['upgrade'],)
def menu(title, classes, color='white'):
  # define the curses wrapper
  def character(stdscr,):
    attributes = {}
    # stuff i copied from the internet that i'll put in the right format later
    icol = {
      4:'red',
      2:'green',
      3:'yellow',
      1:'blue',
      5:'magenta',
      6:'cyan',
      7:'white'
    }
    # put the stuff in the right format
    col = {v: k for k, v in icol.items()}

    # declare the background color

    bc = curses.COLOR_BLACK

    # make the 'normal' format
    curses.init_pair(1, 7, bc)
    attributes['normal'] = curses.color_pair(1)


    # make the 'highlighted' format
    curses.init_pair(2, col[color], bc)
    attributes['highlighted'] = curses.color_pair(2)


    # handle the menu
    c = 0
    option = 0
    while c != 10:

        stdscr.erase() # clear the screen (you can erase this if you want)

        # add the title
        stdscr.addstr(f"{title}\n", curses.color_pair(1))

        # add the options
        for i in range(len(classes)):
            # handle the colors
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            
            # actually add the options

            stdscr.addstr(f'> ', attr)
            stdscr.addstr(f'{classes[i]}' + '\n', attr)
        c = stdscr.getch()

        # handle the arrow keys
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(classes) - 1:
            option += 1
    return option
  return curses.wrapper(character)
def FileEncrypt(name):
    with open('key.key','rb') as file:
        key = file.read()
    with open(f'{name}','rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(f'{name}','wb') as f:
        f.write(encrypted)
def FileDecrypt(name):
    global chicky
    with open('key.key','rb') as file:
        key = file.read()
    with open(f'{name}','rb') as f:
        data = f.read()
    if chicky == 0:
        fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    string = decrypted.decode("UTF-8").replace("'", '"')
    data = f'{string}'
    data = json.loads(data)
    return data
def set_stats():
    global reward_game
    global phew_c
    global enemy_u
    global helmet
    global art
    global a_count
    global armor
    global armor_ad
    global boots
    global sword
    global souly
    global endless_game
    global secret1
    global elite_enemy
    global boss_enemy
    global max_health
    global damage
    global health
    global coins
    global speed
    global defence
    global udamage
    global critD
    global critC
    global Regen
    global Abs
    global StunC
    global Assassin_set
    global Vampire_set
    global Knight_set
    global Demigod_set
    global Vampirism
    global user_class
    global exp_cap
    global inventory
    global equip
    global block
    global local_dif
    global total_dif
    global level
    global exp
    global upgrade
    global step
    global enemy_hp
    global enemy_damage
    global endless_game
    global Knight_Vampire
    global Hell_set
    global elite_counter
    global boss
    global savee
    global Vampirism_hp
    global hpdamage
    global metal
    global magic_metal
    global leather
    global ori_metal
    global hell_metal
    global godly_metal
    global first_mat1
    global second_mat1
    global first_mat
    global second_mat
    global Item1
    global first_material_need
    global second_material_need
    global location
    global extra_dif
    extra_dif = 1
    location = "Лес"
    metal = 0
    leather = 0
    magic_metal = 0
    ori_metal = 0
    hell_metal = 0
    godly_metal = 0
    first_mat1 = "None"
    second_mat1 = "None"
    first_mat = "None"
    Item1 = "None"
    second_mat = "None"
    first_material_need = "None"
    second_material_need = "None"
    boss = 0
    elite_counter = 0
    elite_enemy = 0
    boss_enemy = 0
    endless_game = 0
    max_health = 20
    damage = 1
    health = 20
    coins = int(50)
    speed = 3
    defence = 0
    udamage = 0
    critD = 2
    critC = 20

    Regen = 0
    Abs = 0
    StunC = 0

    reward_game = 1

    Assassin_set = 0
    Vampire_set = 0
    Knight_set = 0
    Demigod_set = 0
    Hell_set = 0

    savee = 0

    phew_c = 0
    
    Vampirism = 0
    Vampirism_hp = 0
    hpdamage = 0

    Knight_Vampire = ["[36mРыцарь[0m", "[31mВампир[0m"]

    user_class = "[32mЧеловек[0m"

    exp_cap = int(50)

    bot_buy = 0
    kort_buy = 0

    enemy_u = 0

    inventory = [ ]
    equip = [ ]


    block = 0

    secret1 = 0


    local_dif = 1
    total_dif = 1

    level = 1
    exp = 0
    upgrade = 1

    autobattle = 0

    step = 0

    enemy_hp = 0
    enemy_damage = 0

    helmet = "Нету"
    armor = "Нету"
    armor_ad = "Нету"
    boots = "Нету"
    sword = "Нету"
    souly = "Нету"
    art = []
    a_count = 0

    
    ask = input("Вы хотите загрузить сохранение? (Д/Н): ")
    if ask == "Д" or ask == "д":
        reward_game = 0
        print("Вы не получите наградных монет за эту игру")
        load()
    else:
        create_maze()

#with open('shop.json', encoding='utf-8') as shop:
    #data = json.load(shop)
    #price = data[0][f'{buy}'][0]['price']
    #if coins <= price:
        #print("Вам не хватает денег")
    #else:
        #name = data[0][f'{buy}'][0]['name']
        #if name not in inventory:
            #coins = coins-price
            #name = data[0][f'{buy}'][0]['name']
            #print(f"Вы успешно купили {name} за {price}")
            #weapon = name
            #code_weapon = buy
            #inventory.append(name)
def load():
    global helmet
    global armor
    global armor_ad
    global art
    global a_count
    global boots
    global sword
    global souly
    global savee
    global endless_game
    global secret1
    global elite_enemy
    global boss_enemy
    global max_health
    global damage
    global health
    global coins
    global speed
    global defence
    global udamage
    global critD
    global critC
    global Regen
    global Abs
    global StunC
    global Assassin_set
    global Vampire_set
    global Knight_set
    global Demigod_set
    global Hell_set
    global Vampirism
    global user_class
    global exp_cap
    global inventory
    global equip
    global block
    global local_dif
    global total_dif
    global level
    global exp
    global upgrade
    global step
    global enemy_hp
    global enemy_damage
    global endless_game
    global Knight_Vampire
    global elite_counter
    global boss
    global inventory
    global equip
    global Vampirism_hp
    global hpdamage
    global a_count
    global leather
    global metal
    global magic_metal
    global ori_metal
    global hell_metal
    global godly_metal
    name = input("Укажите файл с сохранением: ")
    with open(f'{name}.json', 'r', encoding='utf-8') as f:
        data = f.read()
        json_data = json.loads(data)
        #inventory = (json_data[0][f'Player'][0]['inventory'])
        #inventory = Item.from_json(json.loads(data))
        #inventory = jsonpickle.decode(data)
        #inventory = json_data[0][f'Player'][0]['inventory']
        #inventory = jsonpickle.decode(inventory)
        #inventory = list(jsonpickle.decode(inventory))
        #print(inventory)
        health = json_data[0][f'Player'][0]['health']
        damage = json_data[0][f'Player'][0]['damage']
        udamage = json_data[0][f'Player'][0]['udamage']
        coins = json_data[0][f'Player'][0]['coins']
        user_class = json_data[0][f'Player'][0]['user_class']
        max_health = json_data[0][f'Player'][0]['max_health']
        speed = json_data[0][f'Player'][0]['speed']
        defence = json_data[0][f'Player'][0]['defence']
        critD = json_data[0][f'Player'][0]['critD']
        critC = json_data[0][f'Player'][0]['critC']
        elite_counter = json_data[0][f'Player'][0]['elite_counter']
        level = json_data[0][f'Player'][0]['level']
        exp = json_data[0][f'Player'][0]['exp']
        Regen = json_data[0][f'Player'][0]['Regen']
        a_count = json_data[0][f'Player'][0]['a_count']
        Abs = json_data[0][f'Player'][0]['Abs']
        StunC = json_data[0][f'Player'][0]['StunC']
        Vampire_set = json_data[0][f'Player'][0]['Vampire_set']
        Demigod_set = json_data[0][f'Player'][0]['Demigod_set']
        Knight_set = json_data[0][f'Player'][0]['Knight_set']
        Assassin_set = json_data[0][f'Player'][0]['Assassin_set']
        Hell_set = json_data[0][f'Player'][0]['Hell_set']
        Vampirism = json_data[0][f'Player'][0]['Vampirism']
        upgrade = json_data[0][f'Player'][0]['upgrade']
        step = json_data[0][f'Player'][0]['step']
        equip = json_data[0][f'Player'][0]['equip']
        total_dif = json_data[0][f'Player'][0]['total_dif']
        Vampirism_hp = json_data[0][f'Player'][0]['Vampirism_hp']
        hpdamage = json_data[0][f'Player'][0]['hpdamage']
        helmet = json_data[0][f'Player'][0]['helmet']
        armor = json_data[0][f'Player'][0]['armor']
        armor_ad = json_data[0][f'Player'][0]['armor_ad']
        boots = json_data[0][f'Player'][0]['boots']
        sword = json_data[0][f'Player'][0]['sword']
        souly = json_data[0][f'Player'][0]['souly']
        leather = json_data[0][f'Player'][0]['leather']
        metal = json_data[0][f'Player'][0]['metal']
        magic_metal = json_data[0][f'Player'][0]['magic_metal']
        ori_metal = json_data[0][f'Player'][0]['ori_metal']
        hell_metal = json_data[0][f'Player'][0]['hell_metal']
        godly_metal = json_data[0][f'Player'][0]['godly_metal']
        critD = critD/100
    with open(f'{name}I.json', 'r', encoding='utf-8') as f:
         data = f.read()
         try:
             inventory = jsonpickle.decode(data)
         except ValueError:
             inventory = []
         print(inventory)
    with open(f'{name}H.json', 'r', encoding='utf-8') as f:
         data = f.read()
         try:
             helmet = jsonpickle.decode(data)
         except ValueError:
             helmet = "Нету"
    with open(f'{name}A.json', 'r', encoding='utf-8') as f:
         data = f.read()
         try:
             armor = jsonpickle.decode(data)
         except ValueError:
             armor = "Нету"
    with open(f'{name}Ad.json', 'r', encoding='utf-8') as f:
         data = f.read()
         try:
             armor_ad = jsonpickle.decode(data)
         except ValueError:
             armor_ad = "Нету"
    with open(f'{name}B.json', 'r', encoding='utf-8') as f:
         data = f.read()
         try:
             boots = jsonpickle.decode(data)
         except ValueError:
             boots = "Нету"  
    with open(f'{name}S.json', 'r', encoding='utf-8') as f:
         data = f.read()
         try:
             sword = jsonpickle.decode(data)
         except ValueError:
             sword = "Нету"
    with open(f'{name}So.json', 'r', encoding='utf-8') as f:
         data = f.read()
         try:
             souly = jsonpickle.decode(data)
         except ValueError:
             souly = "Нету"
    with open(f'{name}Ar.json', 'r', encoding='utf-8') as f:
         data = f.read()
         try:
             art = jsonpickle.decode(data)
         except ValueError:
             art = [] 
    savee = 1
    create_maze()

def event():
    global enemy_u
    global damage
    global coins
    global speed
    global boss
    global udamage
    global phew_c
    print("Вы наткнулись на необычную комнату")
    ev = random.randint(1, 3)
    if ev == 1:
        a = menu(f'Вы нашли надгробие, что вы будете делать?', ['Бежать','Разбить','Зайти в дверь'], 'red')
        while True:
            if a == 0:
                ra = random.randint(1, 10)
                if ra > 4:
                    print("Вы успешно убежали от этого страшного места и с вами ничего не случилось")
                    time.sleep(1.5)
                    break
                else:
                    print("При попытке сбежать нечто схатило вас за ногу, это были вы...")
                    re = random.randint(1, 10)
                    if re > 6:
                        print("И вы начали тащить себя к себе... Начался бой...")
                        enemy_u = 1
                        time.sleep(1.5)
                        fight()
                        break
                    else:
                        print("Но вы отрубили мёртвому себе руку и убежали")
                        time.sleep(1.5)
                        break
            if a == 1:
                ra = random.randint(1, 10)
                if ra > 4:
                    r = random.randint(5, 15)
                    print(f"Вы разбили могилу и нашли {r} монет")
                    coins += r
                    time.sleep(1.5)
                    break
                else:
                    print("Вы разбили могилу, но тот кто в ней покоился был этому не рад... Начался бой")
                    enemy_u = 1
                    time.sleep(1.5)
                    fight()
                    break
            if a == 2:
                ra = random.randint(1, 10)
                if ra > 8:
                    r = random.randint(1,10)
                    if r > 5:
                        stats = ["Атака", "Уворот", "Усиление атаки"]
                        i = random.randint(0,2)
                        stat = stats[i]
                        sumy = random.randint(1,3)
                        print(f"Вы зашли в дверь и получили благословление, в виде {stat}:{sumy}")
                        time.sleep(1.5)
                        if stat == "Атака":
                            damage += sumy
                        elif stat == "Уворот":
                            speed += sumy
                        else:
                            udamage += sumy
                        break
                    else:
                        stats = ["Атака", "Уворот", "Усиление атаки"]
                        i = random.randint(0,2)
                        stat = stats[i]
                        sumy = random.randint(1,3)
                        print(f"Вы зашли в дверь и получили проклятие, которое понизило ваши характеристики {stat}:{sumy}")
                        time.sleep(1.5)
                        if stat == "Атака":
                            damage -= sumy
                        elif stat == "Уворот":
                            speed -= sumy
                        else:
                            udamage -= sumy
                        break
                    break
                else:
                    a = random.randint(15,50)
                    print(f"Вы открыли дверь и нашли чей-то кошелёк, в нём было: {a} монет")
                    time.sleep(1.5)
                    coins += a
                    break
            else:
                print("Попробуйте ещё раз ввести свой ответ")
                    
                
    elif ev == 2:
        a = menu(f'Вы встертили орду монстров...', ['Сражаться','Бежать'], 'red')
        while True:
            if a == 1:
                rn = random.randint(1, 4)
                if rn == 1:
                    print("Во время побега, вы всё же зацепили одного из них и начался бой")
                    time.sleep(1.5)
                    fight()
                    break
                else:
                    print("Вы успешно убежали как трус, поздравляем")
                    time.sleep(1.5)
                    break
            elif a == 0:
                f = random.randint(2, 8)
                print(f"Вы решили принять бой сразу с ордой? Смело, вас ждёт серия битв против {f} соперников")
                time.sleep(1.5)
                for i in range(f):
                    fight()
                break
    else:
        a = menu(f'Вы нашли фонтан с чистой водой, что вы будете делать?', ['Уйти','Сломать фонтан','Выпить','Плюнуть'], 'red')
        while True:
            if a == 0:
                print("Вы развернулись и ушли, и правильно, сильный мироходцам тру... фонтаны не нужны!")
                time.sleep(1.5)
                break
            if a == 1:
                print("Вы взглянули на фонтан, и он вам чем-то не понравился, после чего вы его разнесли")
                time.sleep(1.5)
                g = random.randint(1, 20)
                if g == 4:
                    print("Боги были недовольны вашим поступком, поэтому закрыли дверь и заставили вас сражаться с монстром!")
                    boss = 1
                    time.sleep(1.5)
                    fight()
                else:
                    xuy = random.randint(1,15)
                    print(f"В останках вы нашли чу-чуть золота... ({xuy})")
                    time.sleep(1.5)
                break
            if a == 2:
                if phew_c == 0:
                    print("Вы выпили эту жидкость и восполнили своё здоровье до максимума!")
                    health = max_health
                    time.sleep(1.5)
                elif phew_c == 1:
                    print("Когда вы выпили эту жидкость вам стало не по себе, и вы потеряли половину жизней")
                    health = int(health/2)
                    time.sleep(1.5)
                elif phew_c >= 2:
                    print("Когда вы выпили эту жидкость вам стало не по себе, и вы потеряли две трети жизней")
                    health -= int(health/3)*2
                    time.sleep(1.5)
                break
                    
            if a == 3:
                if phew_c <= 3:
                    print("Вы плюнули туда... Зачем, неизвестно...")
                    phew_c += 1
                    time.sleep(1.5)
                    break
                elif phew_c >= 3:
                    print("Вы надоели богам, умрите же.")
                    time.sleep(1.5)
                    phew_c = 1
                    for i in range(2):
                        boss = 1
                        fight()
                    break                   
def buy_item(buy):
            global savee
            global endless_game
            global secret1
            global elite_enemy
            global boss_enemy
            global max_health
            global damage
            global health
            global coins
            global speed
            global defence
            global udamage
            global critD
            global critC
            global Regen
            global Abs
            global StunC
            global Assassin_set
            global Vampire_set
            global Knight_set
            global Demigod_set
            global Vampirism
            global user_class
            global exp_cap
            global inventory
            global equip
            global block
            global local_dif
            global total_dif
            global level
            global exp
            global upgrade
            global step
            global enemy_hp
            global enemy_damage
            global endless_game
            global Knight_Vampire
            global elite_counter
            global boss
            global inventory
            global equip
            global Vampirism_hp
            global hpdamage
            global coins
            global art
            global a_count
            with open('items.json', encoding='utf-8') as shop:
                data = shop.read()
                json_data = json.loads(data)
                try:
                    price = json_data[0][f'{buy}'][0]['price']
                except KeyError:
                    print("Вы ввели не верное название")
                    visit(x, y)
                if coins <= price:
                    print("Вам не хватает денег")
                else:
                    name = json_data[0][f'{buy}'][0]['name']
                    c_type = json_data[0][f'{buy}'][0]['type']
                    coins = coins-price
                    print(f"Вы успешно купили {name} за {price}")
                    equip.append(c_type)
                            
                    current_damage = json_data[0][f'{buy}'][0]['damage']
                    current_udamage = json_data[0][f'{buy}'][0]['udamage']
                    current_defence = json_data[0][f'{buy}'][0]['defence']
                    current_speed = json_data[0][f'{buy}'][0]['speed']
                    current_max_health = json_data[0][f'{buy}'][0]['max_health']
                    current_critC = json_data[0][f'{buy}'][0]['critC']
                    current_critD = json_data[0][f'{buy}'][0]['critD']
                    current_Vamp = json_data[0][f'{buy}'][0]['Vamp']
                    current_Stun = json_data[0][f'{buy}'][0]['Stun']
                    current_Abs = json_data[0][f'{buy}'][0]['Abs']
                    current_Regen = json_data[0][f'{buy}'][0]['Regen']
                    current_Vampirism_hp = json_data[0][f'{buy}'][0]['VampHP']
                    current_hpdamage = json_data[0][f'{buy}'][0]['hpdamage']
                    current_set = json_data[0][f'{buy}'][0]['set']
                    Item1 = Item(name, current_max_health, current_defence, current_damage, current_udamage, current_speed, current_critD, current_critC, current_Regen, current_Abs, current_Stun, current_Vamp, current_hpdamage, current_Vampirism_hp, current_set, c_type, price, 0, name)
                    inventory.append(Item1)
def sell_item(buy, invy):
            global helmet
            global armor
            global armor_ad
            global boots
            global sword
            global souly
            global savee
            global art
            global a_count
            global endless_game
            global secret1
            global elite_enemy
            global boss_enemy
            global max_health
            global damage
            global health
            global coins
            global speed
            global defence
            global udamage
            global critD
            global critC
            global Regen
            global Abs
            global StunC
            global Assassin_set
            global Vampire_set
            global Knight_set
            global Demigod_set
            global Vampirism
            global user_class
            global exp_cap
            global inventory
            global equip
            global block
            global local_dif
            global total_dif
            global level
            global exp
            global upgrade
            global step
            global enemy_hp
            global enemy_damage
            global endless_game
            global Knight_Vampire
            global elite_counter
            global boss
            global inventory
            global equip
            global Vampirism_hp
            global hpdamage
            global coins
            with open('items.json', encoding='utf-8') as shop:
                    data = shop.read()
                    json_data = json.loads(data)
                    Item1 = inventory[buy]
                    name = Item1.name
                    price = Item1.price
                    inventory.pop(buy)
                    pricee = price/2
                    coins = int(coins+pricee)
                    print(f"Вы продали {name} за {pricee}")
                    invy.destroy()
                    inv()
def upgrade_item(buy, invy):
            global helmet
            global armor
            global armor_ad
            global boots
            global sword
            global souly
            global savee
            global art
            global a_count
            global endless_game
            global secret1
            global elite_enemy
            global boss_enemy
            global max_health
            global damage
            global health
            global coins
            global speed
            global defence
            global udamage
            global critD
            global critC
            global Regen
            global Abs
            global StunC
            global Assassin_set
            global Vampire_set
            global Knight_set
            global Demigod_set
            global Vampirism
            global user_class
            global exp_cap
            global inventory
            global equip
            global block
            global local_dif
            global total_dif
            global level
            global exp
            global upgrade
            global step
            global enemy_hp
            global enemy_damage
            global endless_game
            global Knight_Vampire
            global elite_counter
            global boss
            global inventory
            global equip
            global Vampirism_hp
            global hpdamage
            global coins
            Item1 = inventory[buy]
            price = Item1.price
            if user_class == "[35mДварф[0m":
                upg_price = price/5
                upg_price = int((upg_price/100)*7.5)
            else:
                upg_price = price/5
            if coins < upg_price:
                print("У вас недостаточно денег")
            else:
                with open('items.json', encoding='utf-8') as shop:
                        data = shop.read()
                        json_data = json.loads(data)
                        Item1 = inventory[buy]
                        Item1.name = (f"{Item1.picture} +{Item1.upgrade}")
                        price = Item1.price
                        Item1.damage = round((Item1.damage*1.1),1)
                        Item1.udamage = round((Item1.udamage*1.1),1)
                        Item1.defence = round((Item1.defence*1.1),1)
                        Item1.speed = round((Item1.speed*1.1),1)
                        Item1.max_health = round((Item1.max_health*1.1),1)
                        Item1.critC = round((Item1.critC*1.1),1)
                        Item1.critD = round((Item1.critD*1.1),1)
                        Item1.Vampirism = round((Item1.Vampirism*1.1),1)
                        Item1.StunC = round((Item1.StunC*1.1),1)
                        Item1.Abs = round((Item1.Abs*1.1),1)
                        Item1.Regen = round((Item1.Regen*1.1),1)
                        Item1.Vampirism_hp = round((Item1.Vampirism_hp*1.1),1)
                        Item1.hpdamage = round((Item1.hpdamage*1.1),1)
                        Item1.upgrade += 1
                        if user_class == "[35mДварф[0m":
                            upg_price = price/5
                            upg_price = int((upg_price/100)*7.5)
                        else:
                            upg_price = price/5
                        Item1.price = int(Item1.price+upg_price)
                        coins = int(coins-upg_price)
                        print("Улучшено")
                        invy.destroy()
                        inv()
def setting(current_set):
                            global Vampire_set
                            global Knight_set
                            global Assassin_set
                            global Demigod_set
                            global Hell_set
                            global critD
                            global critC
                            global damage
                            global udamage
                            global defence
                            global speed
                            global max_health
                            global critD
                            global Vampirism
                            global hpdamage
                            global user_class
                            global Regen
                            global Vampirism_hp
                            global Abs
                            if current_set == "Vampire":
                                Vampire_set += 1
                            elif current_set == "Knight":
                                Knight_set += 1
                            elif current_set == "Assassin":
                                Assassin_set += 1
                            elif current_set == "Godly":
                                Demigod_set += 1
                            elif current_set == "Hell":
                                Hell_set += 1
                            print(Hell_set)
                            if Vampire_set >= 3 and user_class == "[31mУбийца[0m":
                                user_class = "[31mВампир[0m"
                                damage += 5
                                udamage += 2
                                defence -= 10
                                max_health += 50
                                critD += 0.4
                                Vampirism += 20
                                hpdamage += 5
                                print("==Новый класс==")
                            elif Knight_set >= 3 and user_class == "[36mВоин[0m":
                                user_class = "[36mРыцарь[0m"
                                damage += 5
                                defence += 15
                                max_health += 40
                                critD += 0.2
                                hpdamage += 5
                                Vampirism_hp += 7
                                print("==Новый класс==")
                            elif Assassin_set >= 3 and user_class == "[32mВор[0m":
                                user_class = "[32mАссассин[0m"
                                damage += 10
                                defence += 5
                                max_health += 10
                                critD += 0.7
                                udamage += 3
                                critC += 20
                                print("==Новый класс==")
                            elif Demigod_set >= 3 and user_class == "[35mЧеловек[0m":
                                user_class = "[33mБожество[0m"
                                damage += 10
                                defence += 25
                                max_health += 60
                                critD += 0.5
                                udamage += 3
                                critC += 30
                                speed += 20
                                Vampirism_hp += 10
                                print("==Новый класс==")
                            elif Demigod_set >= 5 and user_class == "[33mБожество[0m":
                                user_class = "[33mПолуБог[0m"
                                damage += 40
                                defence += 10
                                max_health += 250
                                critD += 1.5
                                udamage += 10
                                critC += 25
                                speed += 20
                                Vampirism_hp += 15
                                print("==Новый класс==")                            
                            elif Demigod_set >= 3 and user_class == "[32mАссасин[0m":
                                user_class = "[33mКлинок Бога Смерти[0m"
                                damage += 30
                                defence += 10
                                max_health += 30
                                critD += 1.2
                                udamage += 5
                                critC += 10
                                speed += 10
                                hpdamage += 5
                                print("==Новый класс==")
                            elif Demigod_set >= 3 and user_class == "[36mРыцарь[0m":
                                user_class = "[33mРыцарь Света[0m"
                                damage += 10
                                defence += 30
                                max_health += 30
                                critD += 0.7
                                udamage += 5
                                critC += 10
                                speed += 10
                                hpdamage += 5
                                Regen += 15
                                Vampirism_hp += 5
                                Abs +=10
                                print("==Новый класс==")
                            elif Hell_set >= 3 and user_class == "[36mРыцарь[0m":
                                user_class = "[33mРыцарь Тьмы[0m"
                                damage += 15
                                defence += 20
                                max_health += 60
                                critD += 1.2
                                udamage += 10
                                critC -= 10
                                speed -= 10
                                hpdamage += 10
                                Regen += 25
                                Vampirism_hp -= 5
                                Abs +=10
                                print("==Новый класс==")
                            elif Demigod_set >= 3 and user_class == "[31mВампир[0m":
                                user_class = "[31mГраф Дракула[0m"
                                damage += 20
                                defence += 5
                                max_health += 80
                                critD += 0.2
                                udamage += 6
                                critC += 10
                                speed += 5
                                hpdamage += 2
                                Regen -= 5
                                Vampirism += 30
                                print("==Новый класс==")
                            elif Vampire_set >= 3 and user_class == "[36mРыцарь[0m":
                                user_class = "[35mРыцарь Крови[0m"
                                damage += 10
                                defence += 15
                                max_health += 50
                                critD += 0.2
                                udamage += 2
                                hpdamage += 2
                                Regen += 10
                                Vampirism += 30
                                Vampirism_hp += 10
                                print("==Новый класс==")
                            elif Knight_set >= 3 and user_class == "[31mВампир[0m":
                                user_class = "[35mРыцарь Крови[0m"
                                damage += 10
                                defence += 15
                                max_health += 50
                                critD += 0.2
                                udamage += 2
                                hpdamage += 2
                                Regen += 10
                                Vampirism += 30
                                Vampirism_hp += 10
                                print("==Новый класс==")
def unset(current_set):
                            global Vampire_set
                            global Knight_set
                            global Assassin_set
                            global Demigod_set
                            global Hell_set
                            global damage
                            global udamage
                            global defence
                            global speed
                            global max_health
                            global critD
                            global Vampirism
                            global hpdamage
                            global user_class
                            if current_set == "Vampire":
                                Vampire_set -= 1
                            elif current_set == "Knight":
                                Knight_set -= 1
                            elif current_set == "Assassin":
                                Assassin_set -= 1
                            elif current_set == "Godly":
                                Demigod_set -= 1
                            elif current_set == "Hell":
                                Hell_set -= 1
                            print(Hell_set)
def equip_item(buy, invy):
            global helmet
            global armor
            global armor_ad
            global boots
            global sword
            global souly
            global savee
            global endless_game
            global secret1
            global elite_enemy
            global boss_enemy
            global max_health
            global damage
            global health
            global coins
            global speed
            global defence
            global udamage
            global critD
            global critC
            global Regen
            global Abs
            global StunC
            global Assassin_set
            global Vampire_set
            global Knight_set
            global Demigod_set
            global Vampirism
            global user_class
            global exp_cap
            global inventory
            global equip
            global block
            global local_dif
            global total_dif
            global level
            global exp
            global upgrade
            global step
            global enemy_hp
            global enemy_damage
            global endless_game
            global Knight_Vampire
            global elite_counter
            global boss
            global inventory
            global equip
            global Vampirism_hp
            global hpdamage
            global coins
            global art
            global a_count
            with open('items.json', encoding='utf-8') as shop:
                    data = shop.read()
                    json_data = json.loads(data)
                    Item1 = inventory[buy]
                    name = Item1.name
                    current_price = Item1.price
                    current_damage = Item1.damage
                    current_udamage = Item1.udamage
                    current_defence = Item1.defence
                    current_speed = Item1.speed
                    current_max_health = Item1.max_health
                    current_critC = Item1.critC
                    current_critD = Item1.critD
                    current_Vamp = Item1.Vampirism
                    current_Stun = Item1.StunC
                    current_Abs = Item1.Abs
                    current_Regen = Item1.Regen
                    current_set = Item1.sety
                    c_type = Item1.c_type
                    current_Vampirism_hp = Item1.Vampirism_hp
                    current_hpdamage = Item1.hpdamage
                    print(f'Надето: {current_set}')
                    if c_type == "Helmet":
                        if helmet == "Нету":
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            setting(current_set)
                            helmet = Item1
                            inventory.pop(buy)
                            print("Надето")
                        elif helmet != Item1:
                            with open('items.json', encoding='utf-8') as shop:
                                Item1 = inventory[buy]
                                current_price = helmet.price
                                current_damage = helmet.damage
                                current_udamage = helmet.udamage
                                current_defence = helmet.defence
                                current_speed = helmet.speed
                                current_max_health = helmet.max_health
                                current_critC = helmet.critC
                                current_critD = helmet.critD
                                current_Vamp = helmet.Vampirism
                                current_Stun = helmet.StunC
                                current_Abs = helmet.Abs
                                current_Regen = helmet.Regen
                                current_type = helmet.c_type
                                current_Vampirism_hp = helmet.Vampirism_hp
                                current_hpdamage = helmet.hpdamage
                                current_set = helmet.sety
                            print(f"Снято: {current_set}")
                            damage = damage-current_damage
                            udamage = udamage-current_udamage
                            defence = defence-current_defence
                            speed = speed-current_speed
                            max_health = max_health-current_max_health
                            critC = critC-current_critC
                            critD = critD-(current_critD/100)
                            Vampirism = Vampirism-current_Vamp
                            Regen = Regen-current_Regen
                            Abs = Abs-current_Abs
                            StunC = StunC-current_Stun
                            hpdamage = hpdamage-current_hpdamage
                            Vampirism_hp = Vampirism_hp-current_Vampirism_hp
                            unset(current_set)
                            inventory.append(helmet)
                            inventory.pop(buy)
                            helmet = Item1
                            with open('items.json', encoding='utf-8') as shop:
                                    current_price = Item1.price
                                    current_damage = Item1.damage
                                    current_udamage = Item1.udamage
                                    current_defence = Item1.defence
                                    current_speed = Item1.speed
                                    current_max_health = Item1.max_health
                                    current_critC = Item1.critC
                                    current_critD = Item1.critD
                                    current_Vamp = Item1.Vampirism
                                    current_Stun = Item1.StunC
                                    current_Abs = Item1.Abs
                                    current_Regen = Item1.Regen
                                    current_type = Item1.c_type
                                    current_Vampirism_hp = Item1.Vampirism_hp
                                    current_hpdamage = Item1.hpdamage
                                    current_set = Item1.sety
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            setting(current_set)
                            print("Надето")
                            
                        else:
                            print("У вас уже надет данный предмет")
                    elif c_type == "Armor":
                        if armor == "Нету":
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            armor = Item1
                            setting(current_set)
                            inventory.pop(buy)
                            print("Надето")
                        elif armor != Item1:
                            inventory.append(armor)
                            with open('items.json', encoding='utf-8') as shop:
                                Item1 = inventory[buy]
                                current_price = armor.price
                                current_damage = armor.damage
                                current_udamage = armor.udamage
                                current_defence = armor.defence
                                current_speed = armor.speed
                                current_max_health = armor.max_health
                                current_critC = armor.critC
                                current_critD = armor.critD
                                current_Vamp = armor.Vampirism
                                current_Stun = armor.StunC
                                current_Abs = armor.Abs
                                current_Regen = armor.Regen
                                current_type = armor.c_type
                                current_Vampirism_hp = armor.Vampirism_hp
                                current_hpdamage = armor.hpdamage
                                current_set = armor.sety
                            damage = damage-current_damage
                            udamage = udamage-current_udamage
                            defence = defence-current_defence
                            speed = speed-current_speed
                            max_health = max_health-current_max_health
                            critC = critC-current_critC
                            critD = critD-(current_critD/100)
                            Vampirism = Vampirism-current_Vamp
                            Regen = Regen-current_Regen
                            Abs = Abs-current_Abs
                            StunC = StunC-current_Stun
                            hpdamage = hpdamage-current_hpdamage
                            Vampirism_hp = Vampirism_hp-current_Vampirism_hp
                            unset(current_set)
                            armor = Item1
                            inventory.pop(buy)
                            with open('items.json', encoding='utf-8') as shop:
                                    current_price = Item1.price
                                    current_damage = Item1.damage
                                    current_udamage = Item1.udamage
                                    current_defence = Item1.defence
                                    current_speed = Item1.speed
                                    current_max_health = Item1.max_health
                                    current_critC = Item1.critC
                                    current_critD = Item1.critD
                                    current_Vamp = Item1.Vampirism
                                    current_Stun = Item1.StunC
                                    current_Abs = Item1.Abs
                                    current_Regen = Item1.Regen
                                    current_type = Item1.c_type
                                    current_Vampirism_hp = Item1.Vampirism_hp
                                    current_hpdamage = Item1.hpdamage
                                    current_set = Item1.sety
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            setting(current_set)
                            print("Надето")
                        else:
                            print("У вас уже надет данный предмет")
                    elif c_type == "Armor-Ad":
                        if armor_ad == "Нету":
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            armor_ad = Item1
                            inventory.pop(buy)
                            setting(current_set)
                            print("Надето")
                        elif armor_ad != Item1:
                            with open('items.json', encoding='utf-8') as shop:
                                Item1 = inventory[buy]
                                current_price = armor_ad.price
                                current_damage = armor_ad.damage
                                current_udamage = armor_ad.udamage
                                current_defence = armor_ad.defence
                                current_speed = armor_ad.speed
                                current_max_health = armor_ad.max_health
                                current_critC = armor_ad.critC
                                current_critD = armor_ad.critD
                                current_Vamp = armor_ad.Vampirism
                                current_Stun = armor_ad.StunC
                                current_Abs = armor_ad.Abs
                                current_Regen = armor_ad.Regen
                                current_type = armor_ad.c_type
                                current_Vampirism_hp = armor_ad.Vampirism_hp
                                current_hpdamage = armor_ad.hpdamage
                                current_set = armor_ad.sety
                            damage = damage-current_damage
                            udamage = udamage-current_udamage
                            defence = defence-current_defence
                            speed = speed-current_speed
                            max_health = max_health-current_max_health
                            critC = critC-current_critC
                            critD = critD-(current_critD/100)
                            Vampirism = Vampirism-current_Vamp
                            Regen = Regen-current_Regen
                            Abs = Abs-current_Abs
                            StunC = StunC-current_Stun
                            hpdamage = hpdamage-current_hpdamage
                            Vampirism_hp = Vampirism_hp-current_Vampirism_hp
                            unset(current_set)
                            inventory.append(armor_ad)
                            inventory.pop(buy)
                            armor_ad = Item1
                            with open('items.json', encoding='utf-8') as shop:
                                    current_price = Item1.price
                                    current_damage = Item1.damage
                                    current_udamage = Item1.udamage
                                    current_defence = Item1.defence
                                    current_speed = Item1.speed
                                    current_max_health = Item1.max_health
                                    current_critC = Item1.critC
                                    current_critD = Item1.critD
                                    current_Vamp = Item1.Vampirism
                                    current_Stun = Item1.StunC
                                    current_Abs = Item1.Abs
                                    current_Regen = Item1.Regen
                                    current_type = Item1.c_type
                                    current_Vampirism_hp = Item1.Vampirism_hp
                                    current_hpdamage = Item1.hpdamage
                                    current_set = Item1.sety
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            setting(current_set)
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            print("Надето")
                        else:
                            print("У вас уже надет данный предмет")
                    elif c_type == "Boots":
                        if boots == "Нету":
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            setting(current_set)
                            boots = Item1
                            inventory.pop(buy)
                            print("Надето")
                        elif boots != Item1:
                            with open('items.json', encoding='utf-8') as shop:
                                Item1 = inventory[buy]
                                current_price = boots.price
                                current_damage = boots.damage
                                current_udamage = boots.udamage
                                current_defence = boots.defence
                                current_speed = boots.speed
                                current_max_health = boots.max_health
                                current_critC = boots.critC
                                current_critD = boots.critD
                                current_Vamp = boots.Vampirism
                                current_Stun = boots.StunC
                                current_Abs = boots.Abs
                                current_Regen = boots.Regen
                                current_type = boots.c_type
                                current_Vampirism_hp = boots.Vampirism_hp
                                current_hpdamage = boots.hpdamage
                                current_set = boots.sety
                            damage = damage-current_damage
                            udamage = udamage-current_udamage
                            defence = defence-current_defence
                            speed = speed-current_speed
                            max_health = max_health-current_max_health
                            critC = critC-current_critC
                            critD = critD-(current_critD/100)
                            Vampirism = Vampirism-current_Vamp
                            Regen = Regen-current_Regen
                            Abs = Abs-current_Abs
                            StunC = StunC-current_Stun
                            hpdamage = hpdamage-current_hpdamage
                            Vampirism_hp = Vampirism_hp-current_Vampirism_hp
                            unset(current_set)
                            inventory.append(boots)
                            inventory.pop(buy)
                            boots = Item1
                            with open('items.json', encoding='utf-8') as shop:
                                    current_price = Item1.price
                                    current_damage = Item1.damage
                                    current_udamage = Item1.udamage
                                    current_defence = Item1.defence
                                    current_speed = Item1.speed
                                    current_max_health = Item1.max_health
                                    current_critC = Item1.critC
                                    current_critD = Item1.critD
                                    current_Vamp = Item1.Vampirism
                                    current_Stun = Item1.StunC
                                    current_Abs = Item1.Abs
                                    current_Regen = Item1.Regen
                                    current_type = Item1.c_type
                                    current_Vampirism_hp = Item1.Vampirism_hp
                                    current_hpdamage = Item1.hpdamage
                                    current_set = Item1.sety
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            setting(current_set)
                            print("Надето")
                        else:
                            print("У вас уже надет данный предмет")
                    elif c_type == "Sword":
                        if sword == "Нету":
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            setting(current_set)
                            sword = Item1
                            inventory.pop(buy)
                            print("Надето")
                        elif sword != Item1:                            
                            inventory.append(sword)
                            with open('items.json', encoding='utf-8') as shop:
                                Item1 = inventory[buy]
                                current_price = sword.price
                                current_damage = sword.damage
                                current_udamage = sword.udamage
                                current_defence = sword.defence
                                current_speed = sword.speed
                                current_max_health = sword.max_health
                                current_critC = sword.critC
                                current_critD = sword.critD
                                current_Vamp = sword.Vampirism
                                current_Stun = sword.StunC
                                current_Abs = sword.Abs
                                current_Regen = sword.Regen
                                current_type = sword.c_type
                                current_Vampirism_hp = sword.Vampirism_hp
                                current_hpdamage = sword.hpdamage
                                current_set = sword.sety
                                inventory.pop(buy)
                            damage = damage-current_damage
                            udamage = udamage-current_udamage
                            defence = defence-current_defence
                            speed = speed-current_speed
                            max_health = max_health-current_max_health
                            critC = critC-current_critC
                            critD = critD-(current_critD/100)
                            Vampirism = Vampirism-current_Vamp
                            Regen = Regen-current_Regen
                            Abs = Abs-current_Abs
                            StunC = StunC-current_Stun
                            hpdamage = hpdamage-current_hpdamage
                            Vampirism_hp = Vampirism_hp-current_Vampirism_hp
                            unset(current_set)
                            sword = Item1
                            with open('items.json', encoding='utf-8') as shop:
                                    current_price = Item1.price
                                    current_damage = Item1.damage
                                    current_udamage = Item1.udamage
                                    current_defence = Item1.defence
                                    current_speed = Item1.speed
                                    current_max_health = Item1.max_health
                                    current_critC = Item1.critC
                                    current_critD = Item1.critD
                                    current_Vamp = Item1.Vampirism
                                    current_Stun = Item1.StunC
                                    current_Abs = Item1.Abs
                                    current_Regen = Item1.Regen
                                    current_type = Item1.c_type
                                    current_Vampirism_hp = Item1.Vampirism_hp
                                    current_hpdamage = Item1.hpdamage
                                    current_set = Item1.sety
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            setting(current_set)
                            print("Надето")
                        else:
                            print("У вас уже надет данный предмет")
                    elif c_type == "Soul":
                        if souly == "Нету":
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            souly = Item1
                            setting(current_set)
                            inventory.pop(buy)
                            print("Надето")
                        elif souly != Item1:
                            with open('items.json', encoding='utf-8') as shop:
                                Item1 = inventory[buy]
                                current_price = souly.price
                                current_damage = souly.damage
                                current_udamage = souly.udamage
                                current_defence = souly.defence
                                current_speed = souly.speed
                                current_max_health = souly.max_health
                                current_critC = souly.critC
                                current_critD = souly.critD
                                current_Vamp = souly.Vampirism
                                current_Stun = souly.StunC
                                current_Abs = souly.Abs
                                current_Regen = souly.Regen
                                current_type = souly.c_type
                                current_Vampirism_hp = souly.Vampirism_hp
                                current_hpdamage = souly.hpdamage
                                current_set = souly.sety
                            damage = damage-current_damage
                            udamage = udamage-current_udamage
                            defence = defence-current_defence
                            speed = speed-current_speed
                            max_health = max_health-current_max_health
                            critC = critC-current_critC
                            critD = critD-(current_critD/100)
                            Vampirism = Vampirism-current_Vamp
                            Regen = Regen-current_Regen
                            Abs = Abs-current_Abs
                            StunC = StunC-current_Stun
                            hpdamage = hpdamage-current_hpdamage
                            Vampirism_hp = Vampirism_hp-current_Vampirism_hp
                            unset(current_set)
                            inventory.append(souly)
                            inventory.pop(buy)
                            souly = Item1
                            with open('items.json', encoding='utf-8') as shop:
                                    current_price = Item1.price
                                    current_damage = Item1.damage
                                    current_udamage = Item1.udamage
                                    current_defence = Item1.defence
                                    current_speed = Item1.speed
                                    current_max_health = Item1.max_health
                                    current_critC = Item1.critC
                                    current_critD = Item1.critD
                                    current_Vamp = Item1.Vampirism
                                    current_Stun = Item1.StunC
                                    current_Abs = Item1.Abs
                                    current_Regen = Item1.Regen
                                    current_type = Item1.c_type
                                    current_Vampirism_hp = Item1.Vampirism_hp
                                    current_hpdamage = Item1.hpdamage
                                    current_set = Item1.sety
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            setting(current_set)
                            print("Надето")
                        else:
                            print("На вас уже надет данный предмет")
                    elif c_type == "Support":
                        print(a_count)
                        if a_count <= 2 and Item1 not in art:
                            with open('items.json', encoding='utf-8') as shop:
                                Item1 = inventory[buy]
                                current_price = Item1.price
                                current_damage = Item1.damage
                                current_udamage = Item1.udamage
                                current_defence = Item1.defence
                                current_speed = Item1.speed
                                current_max_health = Item1.max_health
                                current_critC = Item1.critC
                                current_critD = Item1.critD
                                current_Vamp = Item1.Vampirism
                                current_Stun = Item1.StunC
                                current_Abs = Item1.Abs
                                current_Regen = Item1.Regen
                                current_type = Item1.c_type
                                current_Vampirism_hp = Item1.Vampirism_hp
                                current_hpdamage = Item1.hpdamage
                                current_set = Item1.sety
                            damage = damage+current_damage
                            udamage = udamage+current_udamage
                            defence = defence+current_defence
                            speed = speed+current_speed
                            max_health = max_health+current_max_health
                            critC = critC+current_critC
                            critD = critD+(current_critD/100)
                            Vampirism = Vampirism+current_Vamp
                            Regen = Regen+current_Regen
                            Abs = Abs+current_Abs
                            StunC = StunC+current_Stun
                            hpdamage = hpdamage+current_hpdamage
                            Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                            art.append(Item1)
                            setting(current_set)
                            inventory.pop(buy)
                            a_count = a_count+1
                            print("Надето")
                        elif Item1 in art:
                            print("Данный предмет уже надет, нельзя  надевать 2 одинаковых предмета")
                        elif a_count > 3 or a_count == 3:
                            print("У вас надо максимум предметов, вы хотите сменить предмет?")
                            an = input("Д/Н")
                            if an == "Д":
                                a = len(art)
                                ann = input(f"Введите номер предмета 1-{a}: ")
                                ann = int(ann)
                                li = [1, 2, 3, 4]
                                if ann not in li:
                                    print("Вы ввели не верное значение")
                                else:
                                    ann = ann-1
                                    buy1 = art[ann]
                                    with open('items.json', encoding='utf-8') as shop:
                                        Item2 = art[ann]
                                        current_price = Item2.price
                                        current_damage = Item2.damage
                                        current_udamage = Item2.udamage
                                        current_defence = Item2.defence
                                        current_speed = Item2.speed
                                        current_max_health = Item2.max_health
                                        current_critC = Item2.critC
                                        current_critD = Item2.critD
                                        current_Vamp = Item2.Vampirism
                                        current_Stun = Item2.StunC
                                        current_Abs = Item2.Abs
                                        current_Regen = Item2.Regen
                                        current_type = Item2.c_type
                                        current_Vampirism_hp = Item2.Vampirism_hp
                                        current_hpdamage = Item2.hpdamage
                                        current_set = Item2.sety
                                    damage = damage-current_damage
                                    udamage = udamage-current_udamage
                                    defence = defence-current_defence
                                    speed = speed-current_speed
                                    max_health = max_health-current_max_health
                                    critC = critC-current_critC
                                    critD = critD-(current_critD/100)
                                    Vampirism = Vampirism-current_Vamp
                                    Regen = Regen-current_Regen
                                    Abs = Abs-current_Abs
                                    StunC = StunC-current_Stun
                                    hpdamage = hpdamage-current_hpdamage
                                    Vampirism_hp = Vampirism_hp-current_Vampirism_hp
                                    unset(current_set)
                                    art.pop(ann)
                                    inventory.append(Item2)
                                    print("Предмет снят")
                                    with open('items.json', encoding='utf-8') as shop:
                                        current_price = Item1.price
                                        current_damage = Item1.damage
                                        current_udamage = Item1.udamage
                                        current_defence = Item1.defence
                                        current_speed = Item1.speed
                                        current_max_health = Item1.max_health
                                        current_critC = Item1.critC
                                        current_critD = Item1.critD
                                        current_Vamp = Item1.Vampirism
                                        current_Stun = Item1.StunC
                                        current_Abs = Item1.Abs
                                        current_Regen = Item1.Regen
                                        current_type = Item1.c_type
                                        current_Vampirism_hp = Item1.Vampirism_hp
                                        current_hpdamage = Item1.hpdamage
                                        current_set = Item1.sety                                  
                                    art.append(Item1)
                                    inventory.pop(buy)
                                    damage = damage+current_damage
                                    udamage = udamage+current_udamage
                                    defence = defence+current_defence
                                    speed = speed+current_speed
                                    max_health = max_health+current_max_health
                                    critC = critC+current_critC
                                    critD = critD+(current_critD/100)
                                    Vampirism = Vampirism+current_Vamp
                                    Regen = Regen+current_Regen
                                    Abs = Abs+current_Abs
                                    StunC = StunC+current_Stun
                                    hpdamage = hpdamage+current_hpdamage
                                    Vampirism_hp = Vampirism_hp+current_Vampirism_hp
                                    setting(current_set)
                                    print("Надето")
                                    a_count = a_count+1
                            else:
                                print(" ")
                                    
                                
                        else:
                            print("У вас уже надет данный предмет")
            invy.destroy()
            inv()
def inv():
    global coins
    global inventory
    global helmet
    global armor
    global armor_ad
    global boots
    global sword
    global souly
    global art
    global a_count
    invy = Tk()
    invy.title("Инвентарь")
    invy.geometry("800x1000")
    points_l = Label(invy, text=f'Монеты: {coins} ', font=('Roboto Condensed', 15))
    points_l.place(relx=0, rely = 0)
    Tov = Label(invy, text=f'Предметы', font=('Roboto Condensed', 23))
    Tov.place(relx=0.4, rely = 0.05)
    if helmet == "Нету":
        Hel = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        Hel.place(relx=0.8, rely = 0.17, relwidth = 0.09, relheight = 0.075)
    else:
        try:
            image = Image.open(f'img/{helmet.picture}.png')
        except Exception:
            image = PhotoImage(Image.open("img/error.png"))
        image = image.resize((64, 64))
        c_btn = ImageTk.PhotoImage(image)
        Hel = Button(invy, image=c_btn, borderwidth=0)
        Hel.place(relx=0.8, rely = 0.17, relwidth = 0.09, relheight = 0.075)
        Hel.image = c_btn
        
    if armor == "Нету":
        Che = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        Che.place(relx=0.89, rely = 0.17, relwidth = 0.09, relheight = 0.075)
    else:
        try:
            image = Image.open(f'img/{armor.picture}.png')
        except Exception:
            image = PhotoImage(Image.open("img/error.png"))
        image = image.resize((64, 64))
        c_btn = ImageTk.PhotoImage(image)
        Che = Button(invy, image=c_btn, borderwidth=0)
        Che.place(relx=0.89, rely = 0.17, relwidth = 0.09, relheight = 0.075)
        Che.image = c_btn

    if armor_ad == "Нету":
        Pon = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        Pon.place(relx=0.8, rely = 0.27, relwidth = 0.09, relheight = 0.075)
    else:
        try:
            image = Image.open(f'img/{armor_ad.picture}.png')
        except Exception:
            image = PhotoImage(Image.open("img/error.png"))
        image = image.resize((64, 64))
        c_btn = ImageTk.PhotoImage(image)
        Pon = Button(invy, image=c_btn, borderwidth=0)
        Pon.place(relx=0.8, rely = 0.27, relwidth = 0.09, relheight = 0.075)
        Pon.image = c_btn

    if boots == "Нету":
        Boo = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        Boo.place(relx=0.89, rely = 0.27, relwidth = 0.09, relheight = 0.075)
    else:
        try:
            image = Image.open(f'img/{boots.picture}.png')
        except Exception:
            image = PhotoImage(Image.open("img/error.png"))
        image = image.resize((64, 64))
        c_btn = ImageTk.PhotoImage(image)
        Boo = Button(invy, image=c_btn, borderwidth=0)
        Boo.place(relx=0.89, rely = 0.27, relwidth = 0.09, relheight = 0.075)
        Boo.image = c_btn

    if sword == "Нету":
        Sw = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        Sw.place(relx=0.8, rely = 0.38, relwidth = 0.18, relheight = 0.15)
    else:
        try:
            image = Image.open(f'img/{sword.picture}.png')
        except Exception:
            image = PhotoImage(Image.open("img/error.png"))
        image = image.resize((128, 128))
        c_btn = ImageTk.PhotoImage(image)
        Sw = Button(invy, image=c_btn, borderwidth=0)
        Sw.place(relx=0.8, rely = 0.38, relwidth = 0.18, relheight = 0.15)
        Sw.image = c_btn

    if souly == "Нету":
        So = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        So.place(relx=0.8, rely = 0.56, relwidth = 0.18, relheight = 0.15)
    else:
        try:
            image = Image.open(f'img/{souly.picture}.png')
        except Exception:
            image = PhotoImage(Image.open("img/error.png"))
        image = image.resize((128, 128))
        c_btn = ImageTk.PhotoImage(image)
        So = Button(invy, image=c_btn, borderwidth=0)
        So.place(relx=0.8, rely = 0.56, relwidth = 0.18, relheight = 0.15)
        So.image = c_btn
    if art == []:
        Pon = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        Pon.place(relx=0.81, rely = 0.72, relwidth = 0.07, relheight = 0.05)
        Pon = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        Pon.place(relx=0.9, rely = 0.72, relwidth = 0.07, relheight = 0.05)
        Pon = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        Pon.place(relx=0.81, rely = 0.78, relwidth = 0.07, relheight = 0.05)
        Pon = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
        Pon.place(relx=0.9, rely = 0.78, relwidth = 0.07, relheight = 0.05)
    else:
        a = len(art)
        if a == 1:
            first = art[0]
            try:
                image = Image.open(f'img/{first.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn = ImageTk.PhotoImage(image)
            Pon = Button(invy, image=c_btn, borderwidth=0)
            Pon.place(relx=0.81, rely = 0.72, relwidth = 0.07, relheight = 0.05)
            Pon.image = c_btn
            Pon2 = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
            Pon2.place(relx=0.9, rely = 0.72, relwidth = 0.07, relheight = 0.05)
            Pon3 = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
            Pon3.place(relx=0.81, rely = 0.78, relwidth = 0.07, relheight = 0.05)
            Pon4 = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
            Pon4.place(relx=0.9, rely = 0.78, relwidth = 0.07, relheight = 0.05)
        if a == 2:
            first = art[0]
            second = art[1]
            try:
                image = Image.open(f'img/{first.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn1 = ImageTk.PhotoImage(image)
            Pon = Button(invy, image=c_btn1, borderwidth=0)
            Pon.place(relx=0.81, rely = 0.72, relwidth = 0.07, relheight = 0.05)
            Pon.image = c_btn1
            try:
                image = Image.open(f'img/{second.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn2 = ImageTk.PhotoImage(image)
            Pon2 = Button(invy, image=c_btn2, borderwidth=0)
            Pon2.place(relx=0.9, rely = 0.72, relwidth = 0.07, relheight = 0.05)
            Pon3 = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
            Pon3.place(relx=0.81, rely = 0.78, relwidth = 0.07, relheight = 0.05)
            Pon4 = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
            Pon4.place(relx=0.9, rely = 0.78, relwidth = 0.07, relheight = 0.05)
        if a == 3:
            first = art[0]
            second = art[1]
            third = art[2]
            try:
                image = Image.open(f'img/{first.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn = ImageTk.PhotoImage(image)
            Pon = Button(invy, image=c_btn, borderwidth=0)
            Pon.place(relx=0.81, rely = 0.72, relwidth = 0.07, relheight = 0.05)
            Pon.image = c_btn
            try:
                image = Image.open(f'img/{second.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn2 = ImageTk.PhotoImage(image)            
            Pon2 = Button(invy, image=c_btn2, borderwidth=0)
            Pon2.place(relx=0.9, rely = 0.72, relwidth = 0.07, relheight = 0.05)
            Pon2.image = c_btn2
            try:
                image = Image.open(f'img/{third.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn3 = ImageTk.PhotoImage(image)
            Pon3 = Button(invy, image=c_btn3, borderwidth=0)
            Pon3.place(relx=0.81, rely = 0.78, relwidth = 0.07, relheight = 0.05)
            Pon3.image = c_btn3
            Pon4 = Button(invy, text=f'Нету', font=('Roboto Condensed', 23))
            Pon4.place(relx=0.9, rely = 0.78, relwidth = 0.07, relheight = 0.05)
        if a == 4:
            first = art[0]
            second = art[1]
            third = art[2]
            fourth = art[3]
            try:
                image = Image.open(f'img/{first.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn = ImageTk.PhotoImage(image)
            Pon1 = Button(invy, image=c_btn, borderwidth=0)
            Pon1.place(relx=0.81, rely = 0.72, relwidth = 0.07, relheight = 0.05)
            Pon1.image = c_btn
            try:
                image = Image.open(f'img/{second.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn2 = ImageTk.PhotoImage(image)            
            Pon2 = Button(invy, image=c_btn2, borderwidth=0)
            Pon2.place(relx=0.9, rely = 0.72, relwidth = 0.07, relheight = 0.05)
            Pon2.image = c_btn2
            try:
                image = Image.open(f'img/{third.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn3 = ImageTk.PhotoImage(image)            
            Pon3 = Button(invy, image=c_btn3, borderwidth=0)
            Pon3.place(relx=0.81, rely = 0.78, relwidth = 0.07, relheight = 0.05)
            Pon3.image = c_btn3
            try:
                image = Image.open(f'img/{fourth.picture}.png')
            except Exception:
                image = PhotoImage(Image.open("img/error.png"))
            image = image.resize((50, 50))
            c_btn4 = ImageTk.PhotoImage(image)
            Pon4 = Button(invy, image=c_btn4, borderwidth=0)
            Pon4.place(relx=0.9, rely = 0.78, relwidth = 0.07, relheight = 0.05)
            Pon4.image = c_btn4
    btn2 = Button(invy, text="Закрыть инвентарь", font=('Roboto Condensed', 15), command=invy.destroy).place(relx=0, rely=0.9, relwidth = 1, relheight = 0.075)
    #Frame
    main_frame = Frame(invy)
    main_frame.place(relx=0, rely = 0.15, relwidth = 0.8, relheight = 0.7)
    #Canv
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #scroll
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    #Config
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    #another frame
    second_frame = Frame(my_canvas)
    #add new frame
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    listname = inventory
    b = len(listname)
    a = 0
    col = 0
    r = 0
    try:
        for i in range(b):
            l_name = listname[a].picture
            y=functools.partial(equipy, a, invy)
            a = a+1
            try:
                image = Image.open(f'./img/{l_name}.png')
                image = image.resize((128, 128))
                c_btn = ImageTk.PhotoImage(image)
            except Exception as e:
                c_btn = PhotoImage(file=f'./img/error.png')
                print(e)
                time.sleep(100)
            btn = Button(second_frame, image=c_btn, command=y, borderwidth=0)
            btn.image = c_btn
            btn.grid(row=r, column = col, pady= 10, padx=10)
            col = col+1
            if col == 4:
                col = 0
                r = r+1
        mainloop()
    except Exception as e:
        print(e)
        time.sleep(20)
def craft_menu():
    global coins
    global inventory
    global helmet
    global armor
    global armor_ad
    global boots
    global sword
    global souly
    global art
    global a_count
    global Res1
    global Res2
    global Res_text1
    global Res_text2
    invy = Tk()
    invy.title("Меню крафта")
    invy.geometry("800x1000")
    Tov = Label(invy, text=f'Предметы доступные для крафта', font=('Roboto Condensed', 23))
    Tov.place(relx=0.2, rely = 0.05)
    btn2 = Button(invy, text="Закрыть меню", font=('Roboto Condensed', 15), command=invy.destroy).place(relx=0, rely=0.9, relwidth = 1, relheight = 0.075)
    Hel = Button(invy, text=f'Выберите предмет', font=('Roboto Condensed', 17))
    Hel.place(relx=0.57, rely = 0.22, relwidth = 0.25, relheight = 0.21)
    Res1 = Button(invy, text=f'Материал 1', font=('Roboto Condensed', 17))
    Res1.place(relx=0.5, rely = 0.50, relwidth = 0.15, relheight = 0.11)
    Res2 = Button(invy, text=f'Материал 2', font=('Roboto Condensed', 17))
    Res2.place(relx=0.74, rely = 0.50, relwidth = 0.15, relheight = 0.11)
    Tov12 = Label(invy, text=f'Название предмета', font=('Roboto Condensed', 23))
    Tov12.place(relx=0.52, rely = 0.43)
    Res_text1 = Label(invy, text=f'Название материала', font=('Roboto Condensed', 8))
    Res_text1.place(relx=0.5, rely = 0.61)
    Res_text2 = Label(invy, text=f'Название материала', font=('Roboto Condensed', 8))
    Res_text2.place(relx=0.74, rely = 0.61)
    Craft_button = Button(invy, text=f'Создать предмет', font=('Roboto Condensed', 17), command=craft_item)
    Craft_button.place(relx=0.45, rely = 0.72, relwidth = 0.45, relheight = 0.11)
    #Frame
    main_frame = Frame(invy)
    main_frame.place(relx=0, rely = 0.15, relwidth = 0.4, relheight = 0.7)
    #Canv
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #scroll
    my_scrollbar = ttk.Scrollbar(my_canvas, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    #Config
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    #another frame
    second_frame = Frame(my_canvas)
    #add new frame
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    craft_items = ["Самодельный меч", "Обмотки на голову", "Вампирский меч", "Куртка простока","Шлем из магического железа", "Нагрудник из магического железа", "Ботинки из магического железа", "Меч из магического железа", "Шлем из орихалка", "Нагрудник из орихалка", "Ботинки из орихалка", "Меч из орихалка", "Шлем из адского металла", "Нагрудник из адского металла", "Ботинки из адского металла", "Меч из адского металла", "Шлем божественного света", "Нагрудник божественного света", "Ботинки божественного света", "Меч божественного света"]
    listname = craft_items
    b = len(listname)
    a = 0
    col = 0
    r = 0
    try:
        for i in range(b):
            l_name = listname[a]
            try:
                image = Image.open(f'./img/{l_name}.png')
                image = image.resize((128, 128))
                c_btn = ImageTk.PhotoImage(image)
            except Exception as e:
                c_btn = PhotoImage(file=f'./img/error.png')
                print(e)
                time.sleep(100)
            y=functools.partial(get_craft_resource, l_name, invy, Tov12, Hel, c_btn, Res1, Res2, Res_text1, Res_text2)
            a = a+1
            btn = Button(second_frame, image=c_btn, command=y, borderwidth=0)
            btn.image = c_btn
            btn.grid(row=r, column = col, pady= 10, padx=10)
            col = col+1
            if col == 2:
                col = 0
                r = r+1
        mainloop()
    except Exception as e:
        print(e)
        time.sleep(20)
def craft_item():
    global metal
    global magic_metal
    global ori_metal
    global hell_metal
    global godly_metal
    global leather
    global first_mat1
    global second_mat1 
    try:
        if first_mat1 >= first_material_need and second_mat1 >= second_material_need:
            if first_mat == "metal":
                metal -= first_material_need
                first_mat1 = metal
                Res_text1.config(text=f"Железо {metal}/{first_material_need}")
            elif first_mat == "leather":
                leather -= first_material_need
                first_mat1 = leather
                Res_text1.config(text=f"Кожа {leather}/{first_material_need}")
            elif first_mat == "magic_metal":
                magic_metal -= first_material_need
                first_mat1 = magic_metal
                Res_text1.config(text=f"Магический метал {magic_metal}/{first_material_need}")
            elif first_mat == "ori_metal":
                ori_metal -= first_material_need
                first_mat1 = ori_metal
                Res_text1.config(text=f"Орихалк {ori_metal}/{first_material_need}")
            elif first_mat == "hell_metal":
                hell_metal -= first_material_need
                first_mat1 = hell_metal
                Res_text1.config(text=f"Адский метал {hell_metal}/{first_material_need}")
            elif first_mat == "godly_metal":
                godly_metal -= first_material_need
                first_mat1 = godly_metal
                Res_text1.config(text=f"Металл божественного света {godly_metal}/{first_material_need}")
                
            if second_mat == "metal":
                metal -= second_material_need
                second_mat1 = metal
                Res_text2.config(text=f"Железо {metal}/{second_material_need}")
            elif second_mat == "leather":
                leather -= second_material_need
                second_mat1 = leather
                Res_text2.config(text=f"Кожа {leather}/{second_material_need}")
            elif second_mat == "magic_metal":
                magic_metal -= second_material_need
                second_mat1 = magic_metal
                Res_text2.config(text=f"Магический метал {magic_metal}/{second_material_need}")
            elif second_mat == "ori_metal":
                ori_metal -= first_material_need
                second_mat1 = ori_metal
                Res_text2.config(text=f"Орихалк {ori_metal}/{second_material_need}")
            elif second_mat == "hell_metal":
                hell_metal -= first_material_need
                second_mat1 = hell_metal
                Res_text2.config(text=f"Адский метал {hell_metal}/{second_material_need}")
            elif second_mat == "godly_metal":
                godly_metal -= first_material_need
                second_mat1 = godly_metal
                Res_text2.config(text=f"Металл божественного света {godly_metal}/{second_material_need}")
            with open('Items.json', 'r', encoding='utf-8') as f:
                data = f.read()
                json_data = json.loads(data)
                buy = Item1
                name = buy
                current_damage = json_data[0][f'{buy}'][0]['damage']
                current_udamage = json_data[0][f'{buy}'][0]['udamage']
                current_defence = json_data[0][f'{buy}'][0]['defence']
                current_speed = json_data[0][f'{buy}'][0]['speed']
                current_max_health = json_data[0][f'{buy}'][0]['max_health']
                current_critC = json_data[0][f'{buy}'][0]['critC']
                current_critD = json_data[0][f'{buy}'][0]['critD']
                current_Vamp = json_data[0][f'{buy}'][0]['Vamp']
                current_Stun = json_data[0][f'{buy}'][0]['Stun']
                current_Abs = json_data[0][f'{buy}'][0]['Abs']
                current_Regen = json_data[0][f'{buy}'][0]['Regen']
                current_Vampirism_hp = json_data[0][f'{buy}'][0]['VampHP']
                current_hpdamage = json_data[0][f'{buy}'][0]['hpdamage']
                current_set = json_data[0][f'{buy}'][0]['set']
                c_type = json_data[0][f'{buy}'][0]['type']
                price = json_data[0][f'{buy}'][0]['price']
                Item2 = Item(name, current_max_health, current_defence, current_damage, current_udamage, current_speed, current_critD, current_critC, current_Regen, current_Abs, current_Stun, current_Vamp, current_hpdamage, current_Vampirism_hp, current_set, c_type, price, 0, name)
                inventory.append(Item2)
                print(f"Вы успешно создали {Item1}")
        else:
            print("У вас недостаточно ресурсов")
    except Exception as e:
        print(e)
        time.sleep(20)
def get_craft_resource(a, invy, Tov12, Hel, c_btn, Res1, Res2, Res_text1, Res_text2):
     global first_material_need
     global second_material_need
     global first_mat
     global second_mat
     global first_mat1
     global second_mat1    
     global Item1
     global metal
     global magic_metal
     global leather
     with open('Crafts.json', 'r', encoding='utf-8') as f:
        data = f.read()
        json_data = json.loads(data)
        Item1 = a
        need = json_data[0][f'{Item1}'][0]['need']
        first_mat = need[0]
        second_mat = need[1]
        image = Image.open(f'./img/{first_mat}.png')
        image = image.resize((96, 96))
        first_icon = ImageTk.PhotoImage(image)
        Res1.config(image=first_icon)
        Res1.image = first_icon
        image = Image.open(f'./img/{second_mat}.png')
        image = image.resize((96, 96))
        second_icon = ImageTk.PhotoImage(image)
        Res2.config(image=second_icon)
        Res2.image = second_icon
        first_material_need = json_data[0][f'{Item1}'][0][f'{first_mat}']
        second_material_need = json_data[0][f'{Item1}'][0][f'{second_mat}']
        if first_mat == "metal":
            first_mat1 = metal
            Res_text1.config(text=f"Железо {metal}/{first_material_need}")
        elif first_mat == "leather":
            first_mat1 = leather
            Res_text1.config(text=f"Кожа {leather}/{first_material_need}")
        elif first_mat == "magic_metal":
            first_mat1 = magic_metal
            Res_text1.config(text=f"Магический метал {magic_metal}/{first_material_need}")
        elif first_mat == "ori_metal":
            first_mat1 = ori_metal
            Res_text1.config(text=f"Орихалк {ori_metal}/{first_material_need}")
        elif first_mat == "hell_metal":
            first_mat1 = hell_metal
            Res_text1.config(text=f"Адский метал {hell_metal}/{first_material_need}")
        elif first_mat == "godly_metal":
            first_mat1 = godly_metal
            Res_text1.config(text=f"Металл божественного света {godly_metal}/{first_material_need}")

        if second_mat == "metal":
            second_mat1 = metal
            Res_text2.config(text=f"Железо {metal}/{second_material_need}")
        elif second_mat == "leather":
            second_mat1 = leather
            Res_text2.config(text=f"Кожа {leather}/{second_material_need}")
        elif second_mat == "magic_metal":
            second_mat1 = magic_metal
            Res_text2.config(text=f"Магический метал {magic_metal}/{second_material_need}")
        elif second_mat == "ori_metal":
            second_mat1 = ori_metal
            Res_text2.config(text=f"Орихалк {ori_metal}/{second_material_need}")
        elif second_mat == "hell_metal":
            second_mat1 = hell_metal
            Res_text2.config(text=f"Адский метал {hell_metal}/{second_material_need}")
        elif second_mat == "godly_metal":
            second_mat1 = godly_metal
            Res_text2.config(text=f"Металл божественного света {godly_metal}/{second_material_need}")
        name = json_data[0][f'{Item1}'][0]['name']
        Tov12.config(text=f'{name}')
        Hel.config(image=c_btn)
        
        print("got")
def save():
    global critD
    global inventory
    global equip
    global user_class
    global helmet
    global armor
    global armor_ad
    global boots
    global sword
    global souly
    global art
    global a_count
    global leather
    global metal
    global magic_metal
    global ori_metal
    global hell_metal
    global godly_metal
    name = input("Укажите имя файла для сохранения: ")
    with open(f'{name}.json', 'w', encoding='utf-8') as f:
        critD = critD*100
        print(inventory)
        user_classA = json.dumps(user_class)
        equipA = json.dumps(equip)
        helmetA = helmet
        armorA = armor
        armor_adA = armor_ad
        bootsA = boots
        swordA = sword
        soulyA = souly
        artA = art
        leatherA = leather
        metalA = metal
        magic_metalA = metal
        ori_metalA = ori_metal
        hell_metalA = hell_metal
        godly_metalA = godly_metal
        
        try:
            helmetA = json.dumps(helmet.__dict__)
        except AttributeError:
            helmetA = json.dumps(helmet)
        try:
            armorA = json.dumps(armor.__dict__)
        except AttributeError:
            armorA = json.dumps(armor)
        try:
            armor_adA = json.dumps(armor_ad.__dict__)
        except AttributeError:
            armor_adA = json.dumps(armor_ad)
        try:
            bootsA = json.dumps(boots.__dict__)
        except AttributeError:
            bootsA = json.dumps(boots)
        try:
            swordA = json.dumps(sword.__dict__)
        except AttributeError:
            swordA = json.dumps(sword)
        try:
            soulyA = json.dumps(souly.__dict__)
        except AttributeError:
            soulyA = json.dumps(souly)
        f.write('[{"Player": [{"user_class": %s, "coins": %d, "health": %d, "max_health": %d, "damage": %d, "udamage": %d,"speed": %d ,"defence": %d,"critD": %d,"critC": %d, "elite_counter": %d,"level": %d,"exp": %d,"upgrade": %d,"step": %d, "equip": %s, "Regen": %d, "Abs": %d, "StunC": %d,"Vampire_set": %d,"Hell_set": %d, "Demigod_set": %d, "Knight_set": %d, "Assassin_set": %d, "total_dif": %d,"Vampirism": %d,"Vampirism_hp": %d,"hpdamage": %d, "helmet": %s, "armor": %s, "armor_ad": %s, "boots": %s, "sword": %s, "a_count": %d, "souly": %s, "leather": %d, "metal": %d, "magic_metal": %d, "ori_metal": %d, "hell_metal": %d, "godly_metal": %d}]'%(user_classA, coins, health, max_health, damage, udamage,speed, defence, critD,critC,elite_counter, level, exp, upgrade, step, equipA, Regen, Abs, StunC, Vampire_set,Hell_set,Demigod_set, Knight_set, Assassin_set,total_dif ,Vampirism, Vampirism_hp, hpdamage,helmetA, armorA, armor_adA, bootsA, swordA, a_count, soulyA, leather, metal, magic_metal, ori_metal, hell_metal, godly_metal)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
        f.write('}]')
        critD = critD/100
    with open(f'{name}I.json', 'w', encoding='utf-8') as f:
         inventoryA = jsonpickle.encode(inventory)
         print(inventoryA)
         f.write(inventoryA)
         #inventoryA = json.dumps([ob.__dict__ for ob in inventory])
    with open(f'{name}H.json', 'w', encoding='utf-8') as f:
         if helmetA == "Нету":
             print(" ")
         else:
             helmetA = jsonpickle.encode(helmet)
             print(helmet)
             f.write(helmetA)
    with open(f'{name}A.json', 'w', encoding='utf-8') as f:
         if armorA == "Нету":
             print(" ")
         else:
             armorA = jsonpickle.encode(armor)
             f.write(armorA)
    with open(f'{name}Ad.json', 'w', encoding='utf-8') as f:
         if armor_adA == "Нету":
             print(" ")
         else:
             armor_adA = jsonpickle.encode(armor_ad)
             f.write(armor_adA)
    with open(f'{name}B.json', 'w', encoding='utf-8') as f:
         if bootsA == "Нету":
             print(" ")
         else:
             bootsA = jsonpickle.encode(boots)
             f.write(bootsA)
    with open(f'{name}S.json', 'w', encoding='utf-8') as f:
         if swordA == "Нету":
             print(" ")
         else:
             swordA = jsonpickle.encode(sword)
             f.write(swordA)
    with open(f'{name}So.json', 'w', encoding='utf-8') as f:
         if soulyA == "Нету":
             print(" ")
         else:
             soulyA = jsonpickle.encode(souly)
             f.write(soulyA)
    with open(f'{name}Ar.json', 'w', encoding='utf-8') as f:
         artA = jsonpickle.encode(art)
         f.write(artA)           
def shope():
    global coins
    shoppy1 = Tk()
    shoppy1.title("Магазин")
    shoppy1.geometry("830x600")
    shoppy1.resizable(width=False, height=False)
    ima = Image.open("img/Exit.png")
    ima = ima.resize((920, 250))
    k_btn = ImageTk.PhotoImage(ima)
    bg = Image.open("img/BG.jpg")
    bg = bg.resize((830, 600))
    bgi = ImageTk.PhotoImage(bg)
    bga = Label(shoppy1, image = bgi)
    bga.place(rely = 0, relx = 0, relheight = 1, relwidth = 1)
    bga.image = bgi
    points_l = Label(shoppy1, text=f'Монеты: {coins} ', font=('Roboto Condensed', 15))
    points_l.place(relx=0, rely = 0)
    Tov = Label(shoppy1, text=f'Товар', font=('Roboto Condensed', 23))
    Tov.place(relx=0.4, rely = 0.05)
    btn2 = Button(shoppy1, image=k_btn, command=shoppy1.destroy, borderwidth=0).place(relx=0, rely=0.79, relwidth = 1, relheight = 0.2)
    #Frame
    main_frame = Frame(shoppy1)
    main_frame.place(relx=0, rely = 0.15, relwidth = 1, relheight = 0.64)
    #Canv
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #scroll
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    #Config
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    #another frame
    second_frame = Frame(my_canvas)
    bg = Image.open("img/BG.jpg")
    bgi = ImageTk.PhotoImage(bg)
    bga = Label(second_frame, image = bgi)
    bga.place(x=0, y=0, relwidth=1, relheight=1)
    bga.image = bgi
    #add new frame
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    listname = ["Шлем", "Куртка", "Плащ", "Поножи", "Ботинки",
                    "Капюшон Вампира", "Накидка Вампира", "Кровь Дракулы", "Душа Вампира",
                    "Капюшон Графа", "Накидка Графа",
                    "Капюшон Ассасина", "Плащ Ассасина", "Ботинки Ассасина", "Душа Ассасина",
                    "Капюшон Клинка бога", "Плащ Клинка бога", "Ботинки Клинка бога",
                    "Шлем Рыцаря", "Нагрудник Рыцаря", "Ботинки Рыцаря", "Душа Рыцаря","Щит Рыцаря",
                    "Шлем Рыцаря света", "Нагрудник Рыцаря света", "Ботинки Рыцаря света","Щит Рыцаря Света",
                    "Шлем Рыцаря крови", "Нагрудник Рыцаря крови", "Ботинки Рыцаря крови",
                    "Божественная частичка", "Божье знание", "ПерстеньЗащиты", "ПерстеньАтаки", "ПерстеньСкорости", "Кольцо Бога", "Щит", "Лук","Точило", "Заточка", "Тяжелый камень",
                    "Деревянный меч", "Каменный меч", "Железный меч", "Алмазный меч", "Вампирский меч", "Божественный меч", "Меч Графа", "Клинок Бога смерти", "Палаш Рыцаря света",]
    b = len(listname)
    a = 0
    col = 0
    r = 0
    for i in range(b):
        l_name = listname[a]
        y=functools.partial(buy,l_name)
        a = a+1
        imf = Image.open("img/Frame.png")
        imf = imf.resize((138, 138))
        ima = Image.open("img/BG.jpg")
        ima = imf.resize((136, 136))
        image = Image.open(f'img/{l_name}.png')
        image = image.resize((128, 128))
        j_img = ImageTk.PhotoImage(ima)
        a_img = ImageTk.PhotoImage(imf)
        c_btn = ImageTk.PhotoImage(image)
        ofc = Label(second_frame, image=a_img)
        ofc.image = a_img
        ofc.grid(row=r, column = col, pady= 10, padx=10)
        btn = Button(second_frame, image=c_btn, command=y, borderwidth=0)
        btn.image = c_btn
        btn.grid(row=r, column = col, pady= 10, padx=10)
        col = col+1
        if col == 5:
            col = 0
            r = r+1
    mainloop()
def equipy(name, invy):
    global helmet
    global armor
    global armor_ad
    global boots
    global sword
    global souly
    with open('items.json', 'r', encoding='utf-8') as f:
        a = 0
        data = f.read()
        json_data = json.loads(data)
        l_name = name
        Item1 = inventory[name]
        name1 = Item1.name
        current_price = Item1.price
        current_damage = Item1.damage
        current_udamage = Item1.udamage
        current_defence = Item1.defence
        current_speed = Item1.speed
        current_max_health = Item1.max_health
        current_critC = Item1.critC
        current_critD = Item1.critD
        current_Vamp = Item1.Vampirism
        current_Stun = Item1.StunC
        current_Abs = Item1.Abs
        current_Regen = Item1.Regen
        current_type = Item1.c_type
        current_Vampirism_hp = Item1.Vampirism_hp
        current_hpdamage = Item1.hpdamage
    top = Toplevel()
    top.title(name)
    top.geometry("250x400")
    Label(top, text =f"Названия: {name1}").pack()
    Label(top, text =f"Цена: {current_price}").pack()
    if current_type == "Helmet":
        typee = "Шлем"
    elif current_type == "Armor":
        typee = "Нагрудник"
    elif current_type == "Armor-Ad":
        typee = "Дополнение брони"
    elif current_type == "Boots":
        typee = "Ботинки"
    elif current_type == "Sword":
        typee = "Меч"
    elif current_type == "Support":
        typee = "Предмет"
    elif current_type == "Soul":
        typee = "Душа"
    Label(top, text =f"Часть: {typee}").pack()
    if current_max_health != 0:
        Label(top, text =f"Макс.Хп: {current_max_health}").pack()
    if current_damage != 0:
        Label(top, text =f"Урон: {current_damage}").pack()
    if current_udamage != 0:
        Label(top, text =f"Усиление урона: {current_udamage}").pack()
    if current_defence != 0:
        Label(top, text =f"Защита: {current_defence}").pack()
    if current_speed != 0:
        Label(top, text =f"Ловкость: {current_speed}").pack()
    if current_critC != 0:
        Label(top, text =f"Крит.Шанс: {current_critC}%").pack()
    if current_critD != 0:
        Label(top, text =f"Крит.Урон: {current_critD}%").pack()
    if current_Vamp != 0:
        Label(top, text =f"Вампиризм: {current_Vamp}%").pack()
    if current_Stun != 0:
        Label(top, text =f"Шанс оглушить: {current_Stun}%").pack()
    if current_Abs != 0:
        Label(top, text =f"Шанс усил.Защиты: {current_Abs}%").pack()
    if current_Regen != 0:
        Label(top, text =f"Регенерация: {current_Regen}").pack()
    if current_Vampirism_hp != 0:
        Label(top, text =f"Регенерация в %: {current_Vampirism_hp}").pack()
    if current_Abs != 0:
        Label(top, text =f"Урон от % хп: {current_hpdamage}%").pack()
    y=functools.partial(equip_item, name, invy)
    f=functools.partial(sell_item, name, invy)
    g=functools.partial(upgrade_item, name, invy)
    if user_class == "[35mДварф[0m":
        upg_price = current_price/5
        upg_price = int((upg_price/100)*7.5)
    else:
        upg_price = current_price/5
    btn1 = Button(top, text="Надеть", command=y).pack()
    btn3 = Button(top, text=f"Улучшить - {upg_price}$", command=g).pack()
    btn1 = Button(top, text="Продать", command=f).pack() 
    btn2 = Button(top, text="Закрыть", command=top.destroy).pack()
def buy(name):
    with open('items.json', 'r', encoding='utf-8') as f:
        a = 0
        data = f.read()
        json_data = json.loads(data)
        l_name = name
        current_price = json_data[0][f'{l_name}'][0]['price']
        current_damage = json_data[0][f'{l_name}'][0]['damage']
        current_udamage = json_data[0][f'{l_name}'][0]['udamage']
        current_defence = json_data[0][f'{l_name}'][0]['defence']
        current_speed = json_data[0][f'{l_name}'][0]['speed']
        current_max_health = json_data[0][f'{l_name}'][0]['max_health']
        current_critC = json_data[0][f'{l_name}'][0]['critC']
        current_critD = json_data[0][f'{l_name}'][0]['critD']
        current_Vamp = json_data[0][f'{l_name}'][0]['Vamp']
        current_Stun = json_data[0][f'{l_name}'][0]['Stun']
        current_Abs = json_data[0][f'{l_name}'][0]['Abs']
        current_Regen = json_data[0][f'{l_name}'][0]['Regen']
        current_type = json_data[0][f'{l_name}'][0]['type']
        current_Vampirism_hp = json_data[0][f'{l_name}'][0]['VampHP']
        current_hpdamage = json_data[0][f'{l_name}'][0]['hpdamage']
    top = Toplevel()
    top.title(name)
    top.geometry("250x400")
    Label(top, text =f"Названия: {name}").pack()
    Label(top, text =f"Цена: {current_price}").pack()
    if current_max_health != 0:
        Label(top, text =f"Макс.Хп: {current_max_health}").pack()
    if current_damage != 0:
        Label(top, text =f"Урон: {current_damage}").pack()
    if current_udamage != 0:
        Label(top, text =f"Усиление урона: {current_udamage}").pack()
    if current_defence != 0:
        Label(top, text =f"Защита: {current_defence}").pack()
    if current_speed != 0:
        Label(top, text =f"Ловкость: {current_speed}").pack()
    if current_critC != 0:
        Label(top, text =f"Крит.Шанс: {current_critC}%").pack()
    if current_critD != 0:
        Label(top, text =f"Крит.Урон: {current_critD}%").pack()
    if current_Vamp != 0:
        Label(top, text =f"Вампиризм: {current_Vamp}%").pack()
    if current_Stun != 0:
        Label(top, text =f"Шанс оглушить: {current_Stun}%").pack()
    if current_Abs != 0:
        Label(top, text =f"Шанс усил.Защиты: {current_Abs}%").pack()
    if current_Regen != 0:
        Label(top, text =f"Регенерация: {current_Regen}").pack()
    if current_Vampirism_hp != 0:
        Label(top, text =f"Регенерация в %: {current_Vampirism_hp}").pack()
    if current_Abs != 0:
        Label(top, text =f"Урон от % хп: {current_hpdamage}%").pack()
    y=functools.partial(buy_item, name)
    btn1 = Button(top, text="Купить предмет", command=y).pack()
    btn2 = Button(top, text="Закрыть", command=top.destroy).pack()
def create_maze():
    global WIDTH
    global HEIGHT
    global EMPTY
    global MARK
    global WALL
    global ENEMY
    global DEF_ENEMY
    global ELITE_ENEMY_DEF
    global BOSS_ENEMY_DEF
    global TREASURE
    global ROOM
    global NORTH, SOUTH, EAST, WEST
    global maze
    WIDTH = int(input("Введите пожалуйста длину лабиринта(Должна быть нечётным значением): ")) # Width of the maze (must be odd).
    HEIGHT = int(input("Введите пожалуйста ширину лабиринта(Должна быть нечётным значением): ")) # Height of the maze (must be odd).
    assert WIDTH % 2 == 1 and WIDTH >= 3
    assert HEIGHT % 2 == 1 and HEIGHT >= 3
    SEED = random.randint(1, 999)
    random.seed(SEED)

    # Use these characters for displaying the maze:
    EMPTY = ' '
    MARK = '@'
    WALL = chr(9608) # Character 9608 is '█'
    ENEMY = "#"
    DEF_ENEMY = "x"
    ELITE_ENEMY_DEF = "X"
    BOSS_ENEMY_DEF = "W"
    TREASURE = "D"
    ROOM = "R"
    NORTH, SOUTH, EAST, WEST = 'Вверх', 'Вниз', 'Вправо', 'Влево'

    # Create the filled-in maze data structure to start:
    maze = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            maze[(x, y)] = WALL # Every space is a wall at first.
    start()
def first_ask(secret1):
    waiting = input("Введите текст:")
    if waiting == "Магазин" or waiting == "магазин":
        #shoppy.append("Железный меч - 100$")
        shope()

    else:
        print("Ну нет же... Введи - 'Магазин'")
        secret1 += secret1+1
        if secret1 >= 5:
            print("Любишь прикалываться, да? \nТогда нам не по пути, прощай!\nЯ буду тебя игнорировать")
            return()
        first_ask(secret1)
def get_item_stat(buy):
                with open('items.json', encoding='utf-8') as shop:
                    data = shop.read()
                    json_data = json.loads(data)
                    price = json_data[0][f'{buy}'][0]['price']
                    name = json_data[0][f'{buy}'][0]['name']
                    tname = json_data[0][f'{buy}'][0]['name']
                    c_type = json_data[0][f'{buy}'][0]['type']                            
                    current_damage = json_data[0][f'{buy}'][0]['damage']
                    current_udamage = json_data[0][f'{buy}'][0]['udamage']
                    current_defence = json_data[0][f'{buy}'][0]['defence']
                    current_speed = json_data[0][f'{buy}'][0]['speed']
                    current_max_health = json_data[0][f'{buy}'][0]['max_health']
                    current_critC = json_data[0][f'{buy}'][0]['critC']
                    current_critD = json_data[0][f'{buy}'][0]['critD']
                    current_Vamp = json_data[0][f'{buy}'][0]['Vamp']
                    current_Stun = json_data[0][f'{buy}'][0]['Stun']
                    current_Abs = json_data[0][f'{buy}'][0]['Abs']
                    current_Regen = json_data[0][f'{buy}'][0]['Regen']
                    current_Vampirism_hp = json_data[0][f'{buy}'][0]['VampHP']
                    current_hpdamage = json_data[0][f'{buy}'][0]['hpdamage']
                    current_set = json_data[0][f'{buy}'][0]['set']
                    tier = random.randint(1,1010)
                    Item1 = Item(name, current_max_health, current_defence, current_damage, current_udamage, current_speed, current_critD, current_critC, current_Regen, current_Abs, current_Stun, current_Vamp, current_hpdamage, current_Vampirism_hp, current_set, c_type, price, 0, name)
                    if tier < 100:
                        price = int(price/2)
                        name = (f"Ужасный {Item1.picture}")                         
                        current_damage = int(current_damage/2)
                        current_udamage = int(current_udamage/2)
                        current_defence = int(current_defence/2)
                        current_speed = int(current_speed/2)
                        current_max_health = int(current_max_health/2)
                        current_critC = int(current_critC/2)
                        current_critD = int(current_critD/2)
                        current_Vamp = int(current_Vamp/2)
                        current_Stun = int(current_Stun/2)
                        current_Abs = int(current_Abs/2)
                        current_Regen = int(current_Regen/2)
                        current_Vampirism_hp = int(current_Vampirism_hp/2)
                        current_hpdamage = int(current_hpdamage/2)
                    elif 100 < tier < 300:
                        price = int(price/1.3)
                        name = (f"Плохой {Item1.picture}")                         
                        current_damage = int(current_damage/1.3)
                        current_udamage = int(current_udamage/1.3)
                        current_defence = int(current_defence/1.3)
                        current_speed = int(current_speed/1.3)
                        current_max_health = int(current_max_health/1.3)
                        current_critC = int(current_critC/1.3)
                        current_critD = int(current_critD/1.3)
                        current_Vamp = int(current_Vamp/1.3)
                        current_Stun = int(current_Stun/1.3)
                        current_Abs = int(current_Abs/1.3)
                        current_Regen = int(current_Regen/1.3)
                        current_Vampirism_hp = int(current_Vampirism_hp/1.3)
                        current_hpdamage = int(current_hpdamage/1.3)
                    elif 300 < tier < 700:
                        price = int(price*1)
                        name = (f"{Item1.picture}")                         
                        current_damage /= 1
                        current_udamage /= 1
                        current_defence /= 1
                        current_speed /= 1
                        current_max_health /= 1
                        current_critC /= 1
                        current_critD /= 1
                        current_Vamp /= 1
                        current_Stun /= 1
                        current_Abs /= 1
                        current_Regen /= 1.
                        current_Vampirism_hp /= 1
                        current_hpdamage /= 1
                    elif 700 < tier < 900:
                        price = int(price*1.4)
                        name = (f"Отличный {Item1.picture}")                         
                        current_damage = int(current_damage*1.4)
                        current_udamage = int(current_udamage*1.4)
                        current_defence = int(current_defence*1.4)
                        current_speed = int(current_speed*1.4)
                        current_max_health = int(current_max_health*1.4)
                        current_critC = int(current_critC*1.4)
                        current_critD = int(current_critD*1.4)
                        current_Vamp = int(current_Vamp*1.4)
                        current_Stun = int(current_Stun*1.4)
                        current_Abs = int(current_Abs*1.4)
                        current_Regen = int(current_Regen*1.4)
                        current_Vampirism_hp = int(current_Vampirism_hp*1.4)
                        current_hpdamage = int(current_hpdamage*1.4)
                    elif 900 < tier < 1000:
                        price = int(price*2)
                        name = (f"Легендарный {Item1.picture}")                         
                        current_damage = int(current_damage*2)
                        current_udamage = int(current_udamage*2)
                        current_defence = int(current_defence*2)
                        current_speed = int(current_speed*2)
                        current_max_health = int(current_max_health*2)
                        current_critC = int(current_critC*2)
                        current_critD = int(current_critD*2)
                        current_Vamp = int(current_Vamp*2)
                        current_Stun = int(current_Stun*2)
                        current_Abs = int(current_Abs*2)
                        current_Regen = int(current_Regen*2)
                        current_Vampirism_hp = int(current_Vampirism_hp*2)
                        current_hpdamage = int(current_hpdamage*2)
                    elif 1000 < tier < 1008:
                        price = int(price*3)
                        name = (f"Проклятый {Item1.picture}")                         
                        current_damage = int(current_damage*3)
                        current_udamage = int(current_udamage*3)
                        current_defence = int(current_defence*3)
                        current_speed = int(current_speed*3)
                        current_max_health = int(current_max_health*3)
                        current_critC = int(current_critC*3)
                        current_critD = int(current_critD*3)
                        current_Vamp = int(current_Vamp*3)
                        current_Stun = int(current_Stun*3)
                        current_Abs = int(current_Abs*3)
                        current_Regen = int(current_Regen*3)
                        current_Vampirism_hp = int(current_Vampirism_hp*3)
                        current_hpdamage = int(current_hpdamage*3)
                    elif tier > 1008:
                        price = int(price*4)
                        name = (f"Древний {Item1.picture}")                         
                        current_damage = int(current_damage*5)
                        current_udamage = int(current_udamage*5)
                        current_defence = int(current_defence*5)
                        current_speed = int(current_speed*5)
                        current_max_health = int(current_max_health*5)
                        current_critC = int(current_critC*5)
                        current_critD = int(current_critD*5)
                        current_Vamp = int(current_Vamp*5)
                        current_Stun = int(current_Stun*5)
                        current_Abs = int(current_Abs*5)
                        current_Regen = int(current_Regen*5)
                        current_Vampirism_hp = int(current_Vampirism_hp*5)
                        current_hpdamage = int(current_hpdamage*5)

                    Item1 = Item(name, current_max_health, current_defence, current_damage, current_udamage, current_speed, current_critD, current_critC, current_Regen, current_Abs, current_Stun, current_Vamp, current_hpdamage, current_Vampirism_hp, current_set, c_type, price, 0, tname)
                    return Item1
    
def reward():
                global metal
                global magic_metal
                global ori_metal
                global hell_metal
                global godly_metal
                global leather
                global exp
                global level
                global upgrade
                global inventory
                global coins
                global health
                global max_health
                global exp_cap
                if elite_enemy == 1:
                    if step < 1000:
                        a = int(2*(step/100)*(level/5))
                        b = int(4*(step/100)*(level/5))
                    else:
                        a = int(2*(step/200)*(level/4))
                        b = int(4*(step/200)*(level/4))
                    if a < 2:
                        a = 2
                    if b < 4:
                        b = 4
                    reward = random.randint(a, b)
                    exp_reward = random.randint(20, 75)
                elif boss_enemy == 1:
                    if step < 1000:
                        a = int(5*(step/100)*(level/5))
                        b = int(7*(step/100)*(level/5))
                    else:
                        a = int(5*(step/200)*(level/4))
                        b = int(7*(step/200)*(level/4))
                    if a < 4:
                        a = 4
                    if b < 6:
                        b = 6
                    reward = random.randint(a, b)
                    exp_reward = random.randint(50, 175)
                else:
                    if step < 1000:
                        a = int(1*(step/100)*(level/5))
                        b = int(1.5*(step/100)*(level/5))
                    else:
                        a = int(1*(step/200)*(level/4))
                        b = int(1.5*(step/200)*(level/4))                        
                    if a < 1:
                        a = 1
                    if b < 2:
                        b = 2
                    reward = random.randint(a, b)
                    exp_reward = random.randint(5, 50)
                print(f"====================================")
                print(f"===========ВЫ ПОБЕДИЛИ==============")
                print(f"===========ВЫ ПОЛУЧИЛИ {reward}©===========")
                print(f"========ВЫ ПОЛУЧИЛИ {exp_reward} опыта=========")
                print(f"====================================")
                #adding drop
                with open('units.json', encoding='utf-8') as e_stat:
                    data = e_stat.read()
                    json_data = json.loads(data)
                    enemy_name = json_data[0][f'{enemy}'][0]['name']
                    enemy_drop = json_data[0][f'{enemy}'][0]['drop']
                    with open('drop.json', encoding='utf-8') as e_drop:
                        data = e_drop.read()
                        json_data = json.loads(data)
                        drop_chance = json_data[0][f'{enemy_drop}'][0]['chance']
                        drop_item = json_data[0][f'{enemy_drop}']
                        rand = random.randint(1, 100)
                        if rand > drop_chance:  #Общий шанс на выпадение
                            drop1 = list(drop_item[0].keys())
                            drop2 = list(drop_item[0].values())
                            drop1 = drop1[:-1]
                            drop2 = drop2[:-1]
                            a = len(drop2)
                            get = []

                            ran = random.randint(1, 100)
                            try:
                                for i in range(a):
                                    ran = random.randint(1, 100)
                                    if drop2[i] > ran: #Шанс каждой вещи
                                        if drop1[i] == "metal":
                                            metal = metal+1
                                            get.append("Метал")
                                        elif drop1[i] == "leather":
                                            leather += 1
                                            get.append("Кожа")
                                        elif drop1[i] == "magic_metal":
                                            magic_metal += 1
                                            get.append("Магический металл")
                                        elif drop1[i] == "ori_metal":
                                            ori_metal += 1
                                            get.append("Орихалк")
                                        elif drop1[i] == "hell_metal":
                                            hell_metal += 1
                                            get.append("Адский металл")
                                        elif drop1[i] == "godly_metal":
                                            godly_metal += 1
                                            get.append("Божественный металл")
                                        else:
                                            drop3 = get_item_stat(drop1[i])
                                            inventory.append(drop3)
                                            get.append(drop3)
                                get = (', '.join(str(el) for el in get))      
                                if get == " " or get == "":
                                    og = 1
                                else:
                                    print(f"====================================")
                                    print(f"=========ВЫ ПОБЕДИЛИ {enemy}========")
                                    print(f"====ВЫ ПОЛУЧИЛИ {get}====")
                                    print(f"====================================")
                                get =[]
                            except Exception as e:
                                print(e)
                                time.sleep(20)
                exp = exp+exp_reward
                exp_cap = 50*(level*1.2)
                if exp >= exp_cap:
                    level = level + 1
                    if level > 5:
                        upgrade = upgrade + 2
                    elif level > 10:
                        upgrade = upgrade + 3
                    else:
                        upgrade = upgrade + 1
                    exp = exp-exp_cap
                    print("-------НОВЫЙ УРОВЕНЬ!-------")
                    if health < max_health:
                        health = max_health
                        print("---ЗДОРОВЬЕ ВОССТАНОВЛЕНО---")
                    else:
                        print("---ЗДОРОВЬЕ НА МАКСИМУМЕ---")
                coins = coins+reward
def fight():
    global enemy_u
    global enemy
    global elite_counter
    global Vampirism
    global elite_enemy
    global boss_enemy
    global defence
    global udamage
    global exp
    global level
    global upgrade
    global total_dif
    global local_dif
    global health
    global enemy_hp
    global enemy_damage
    global speed
    global damage
    global boss
    global Regen
    global hpdamage
    global Vampirism_hp
    global enemy_def
    global tdefence
    global shield
    global max_health
    global r_coins
    global location
    if total_dif == 1:
        dif = 1
    elif total_dif == 2:
        dif = 1.3
    elif total_dif == 3:
        dif = 1.7
    elif total_dif == 4:
        dif = 2.2
    local_dif = step*0.02
    if local_dif <= 1:
        local_dif = 1
    elite = random.randint(1, 100)
    if elite > 95:
        elite_counter = elite_counter+1
        if elite_counter == 6:
            boss = 1     
    enemy_random = random.randint(1, 5)
    # "Лес"
    # "Ущелье"
    # "Преисподня"
    # "Высшее королевство"
    # "Олимп" "WIP"
    # "Долина Конца"
    if location == "Лес" and elite < 95 and boss != 1:
        if enemy_random == 1:
            enemy = "Паук"
        elif enemy_random == 2:
            enemy = "Нежить"
        elif enemy_random == 3:
            enemy = "Костлявый волк"
        elif enemy_random == 4:
            enemy = "Вепрь"
        elif enemy_random == 5:
            enemy = "Упырь"
    elif location == "Лес" and elite > 95 and boss != 1:
        if enemy_random == 1:
            enemy = "Тарантул"
        elif enemy_random == 2:
            enemy = "Нежить некроманта"
        elif enemy_random == 3:
            enemy = "Душа Цербера"
        elif enemy_random == 4:
            enemy = "Зомби-Вепрь"
        elif enemy_random == 5:
            enemy = "Вампир-Переросток"
    elif location == "Лес" and boss == 1:
        if enemy_random == 1:
            enemy = "Голем"
        elif enemy_random == 2:
            enemy = "Крупный Зомби"
        elif enemy_random == 3:
            enemy = "Альфа-Оборотень"
        elif enemy_random == 4:
            enemy = "Зомби-Убийца"
        elif enemy_random == 5:
            enemy = "Вампир"
    elif location == "Ущелье" and elite < 95 and boss != 1:
        if enemy_random == 1:
            enemy = "Маленький Голем"
        elif enemy_random == 2:
            enemy = "Зомби"
        elif enemy_random == 3:
            enemy = "Оборотень"
        elif enemy_random == 4:
            enemy = "Чудище"
        elif enemy_random == 5:
            enemy = "Слабый Вампир"
    elif location == "Ущелье" and elite > 95 and boss != 1:
        if enemy_random == 1:
            enemy = "Голем"
        elif enemy_random == 2:
            enemy = "Крупный Зомби"
        elif enemy_random == 3:
            enemy = "Альфа-Оборотень"
        elif enemy_random == 4:
            enemy = "Зомби-Убийца"
        elif enemy_random == 5:
            enemy = "Вампир"
    elif location == "Ущелье" and boss == 1:
        if enemy_random == 1:
            enemy = "Древний Демон"
        elif enemy_random == 2:
            enemy = "Адский Голем"
        elif enemy_random == 3:
            enemy = "Цербер"
        elif enemy_random == 4:
            enemy = "Некромант"
        elif enemy_random == 5:
            enemy = "Граф Дракула"
    elif location == "Преисподня" and elite < 95 and boss != 1:
        if enemy_random == 1:
            enemy = "Демон"
        elif enemy_random == 2:
            enemy = "Ифрит"
        elif enemy_random == 3:
            enemy = "Адская Гончая"
        elif enemy_random == 4:
            enemy = "Инкуб"
        elif enemy_random == 5:
            enemy = "Древний Вампир"
    elif location == "Преисподня" and elite > 95 and boss != 1:
        if enemy_random == 1:
            enemy = "Древний Демон"
        elif enemy_random == 2:
            enemy = "Адский Голем"
        elif enemy_random == 3:
            enemy = "Цербер"
        elif enemy_random == 4:
            enemy = "Некромант"
        elif enemy_random == 5:
            enemy = "Граф Дракула"
    elif location == "Преисподня" and boss == 1:
        if enemy_random == 1:
            enemy = "Маммон"
        elif enemy_random == 2:
            enemy = "Титан Преисподни"
        elif enemy_random == 3:
            enemy = "Адский Цербер"
        elif enemy_random == 4:
            enemy = "Великий Некромант"
        elif enemy_random == 5:
            enemy = "Царь Вампиров"
    elif location == "Высшее королевство" and elite < 95 and boss != 1:
        if enemy_random == 1:
            enemy = "Рыцарь"
        elif enemy_random == 2:
            enemy = "Ассасин"
        elif enemy_random == 3:
            enemy = "Вор"
        elif enemy_random == 4:
            enemy = "Воин"
        elif enemy_random == 5:
            enemy = "Убийца"
    elif location == "Высшее королевство" and elite > 95 and boss != 1:
        if enemy_random == 1:
            enemy = "Рыцарь Крови"
        elif enemy_random == 2:
            enemy = "Рыцарь Света"
        elif enemy_random == 3:
            enemy = "Клинок Бога Смерти"
        elif enemy_random == 4:
            enemy = "Низшее Божество"
        elif enemy_random == 5:
            enemy = "Элитный Убийца"
    elif location == "Высшее королевство" and boss == 1:
        if enemy_random == 1:
            enemy = "Божество"
        elif enemy_random == 2:
            enemy = "Верховный Рыцарь Света"
        elif enemy_random == 3:
            enemy = "Бог Смерти"
        elif enemy_random == 4:
            enemy = "Верховый Рыцарь Крови"
        elif enemy_random == 5:
            enemy = "Глава Гильдии Убийц"
    elif location == "Долина конца":
        if enemy_random == 1:
            enemy = "Божество"
        elif enemy_random == 2:
            enemy = "Верховный Рыцарь Света"
        elif enemy_random == 3:
            enemy = "Бог Смерти"
        elif enemy_random == 4:
            enemy = "Верховый Рыцарь Крови"
        elif enemy_random == 5:
            enemy = "Глава Гильдии Убийц"
    boss = 0
    if enemy_u == 1:
        enemy_name = "Ты"
        hp = health/1.4
        dmg = damage/1.4
        prot = defence*1.5
        e_speed = speed
        piercing = 5
    else:
        with open('units.json', encoding='utf-8') as e_stat:
            data = e_stat.read()
            json_data = json.loads(data)
            enemy_name = json_data[0][f'{enemy}'][0]['name']
            hp = json_data[0][f'{enemy}'][0]['hp']
            dmg = json_data[0][f'{enemy}'][0]['dmg']
            prot = json_data[0][f'{enemy}'][0]['prot']
            e_speed = json_data[0][f'{enemy}'][0]['speed']
            piercing = json_data[0][f'{enemy}'][0]['piercing']
    print(":::НАЧАЛО БОЯ:::")
    if elite > 95:
        if elite_counter == 6:
            print(":::::БОСС!:::::")
            elite_counter = 0
            boss_enemy = 1
        else:
            print("::::ЭЛИТНЫЙ ПРОТИВНИК!::::")
            elite_enemy = 1
        
    enemy_hp = (hp*local_dif*(level/4)*dif*extra_dif)
    enemy_damage = (dmg*local_dif*(level/6)*dif*extra_dif)
    prot = ((prot*local_dif*(level/6)*dif)/2*extra_dif)
    print(prot)
    if prot < 50:
        enemy_def = prot
    elif 100 > prot > 50:
        cdef = prot
        b = cdef-50
        a = b/2
        enemy_def = round((a+50), 1)
    elif 250 > prot > 100:
        cdef = prot
        b = cdef-100
        a = b/10
        enemy_def = round((a+75), 1)
    elif 500 > prot > 250:
        cdef = prot
        b = cdef-250
        a = b/25
        enemy_def = round((a+90), 1)
    elif prot > 500:
        enemy_def = 99
    enemy_pie = piercing
    enemy_speed = int(e_speed*local_dif*(level/10)*dif)
    hpd = (hp/100)*hpdamage
    gdamage = 0
    if user_class == "[32mГоблин[0m":
        gdamage = int(coins/3)
    tdamage = int(damage+udamage+hpd+gdamage)
    if defence < 50:
        tdefence = defence
    elif 100 >= defence > 50:
        cdef = defence
        b = cdef-50
        a = b/2
        tdefence = round((a+50), 1)
    elif 250 >= defence > 100:
        cdef = defence
        b = cdef-100
        a = b/10
        tdefence = round((a+75), 1)
    elif 500 >= defence > 250:
        cdef = defence
        b = cdef-250
        a = b/25
        tdefence = round((a+90), 1)
    elif defence > 500:
        tdefence = 99
    shield = 0
    if user_class == "[35mГолем[0m":
        shield = int(max_health*defence/50)
    lives = 1
    if user_class == "[35mФеникс[0m":
        lives = 2
    show_dif = ("%.2f" % local_dif)
    enemy_hp = round(enemy_hp, 1)
    enemy_damage = round(enemy_damage, 1)
    enemy_pdamage = round((enemy_damage/100)*enemy_pie, 2)
    enemy_def = round(enemy_def, 1)
    if user_class == "[36mТолстяк[0m":
        health += defence*5
        health = int(health)
        tdefence = 0
    if user_class == "[31mЭлитный Убийца[0m":
        if speed > 100:
            tdamage = int(tdamage*(speed/100))
    if enemy_u == 1:
        enemy_name = "Ты"
        enemy_hp = int(health/1.4)
        enemy_damage = int(damage/1.4)
        enemy_speed = int(speed*1.2)
        piercing = 5
        enemy_u = 0
    enemy_powerlevel = round((enemy_hp/10)+(enemy_damage/5)+(enemy_speed/3)+(enemy_def/5), 2)
    fdefence = defence
    print(f"::ЛОКАЦИЯ: {location}::")
    print(f"::ВАШ ПРОТИВНИК: {enemy_name}::")
    print(f"::Уровень силы противника: {enemy_powerlevel}::")
    print(f"::Усиление противника:{show_dif}x::")
    print(f"::ЗДОРОВЬЕ ПРОТИВНИКА: {enemy_hp}::")
    print(f"::АТАКА ПРОТИВНИКА: {enemy_damage}::")
    print(f"::ЛОВКОСТЬ ПРОТИВНИКА: {enemy_speed}::")
    print(f"::ЗАЩИТА ПРОТИВНИКА: {enemy_def}%::")
    print(" ")
    print(f"::ВАШЕ ЗДОРОВЬЕ: {health}::")
    print(f"::ВАША ЗАЩИТА: {tdefence}%::")
    print(f"::ВАША АТАКА: {tdamage}::")
    print(f"::ВАША ЛОВКОСТЬ: {speed}::")
    if shield != 0:
        print(f"::ВАШ БАРЬЕР: {shield}::")
    print("========================")
    time.sleep(2)
    ph = 1
    while True:
        if fdefence < 50:
            tdefence = fdefence
        elif 100 >= fdefence > 50:
            cdef = fdefence
            b = cdef-50
            a = b/2
            tdefence = round((a+50), 1)
        elif 250 >= fdefence > 100:
            cdef = fdefence
            b = cdef-100
            a = b/10
            tdefence = round((a+75), 1)
        elif 500 >= fdefence > 250:
            cdef = fdefence
            b = cdef-250
            a = b/25
            tdefence = round((a+90), 1)
        elif fdefence > 500:
            tdefence = 99
        enemy_ddamage = round((enemy_damage/100*(100-tdefence)), 1)
        if autobattle == 0:
            di = ["Атаковать", "Защититься", "Стоять как мужик", "Парировать"]
            your_move = menu(f'Здоровье врага: ♥{enemy_hp}\nВаше здоровье: ♥{health}\nВыберите действие', di, 'red')
            if your_move == "Атаковать":
                your_move = 1
            if your_move == "Защититься":
                your_move = 2
            if your_move == "Стоять как мужик":
                your_move = 3
            if your_move == "Парировать":
                your_move = 4
        elif autobattle == 1:
            your_move = 0

        if your_move == 0:
            #Атака
            
            stun = random.randint(1, 100)
            crit = random.randint(1, 100)
            e_evadeD = ((enemy_speed/100)*10)
            m_evadeD = ((speed/100)*10)
            if enemy_speed > speed:
                a = int(speed-m_evadeD)
                b = int(enemy_speed+e_evadeD)
                c = int(enemy_speed-e_evadeD)
                m_evade = random.randint(a, b)
                e_evade = random.randint(c, b)
            else:
                a = int(speed-m_evadeD)
                b = int(speed+m_evadeD)
                c = int(enemy_speed-e_evadeD)
                m_evade = random.randint(a, b)
                e_evade = random.randint(c, b)
            sc = 1
            if user_class == "[32mОхотник[0m":
                sc = random.randint(1, 2)
            tdamage = tdamage+udamage
            mdamage = damage
            hb = 0
            if user_class == "[31mБерсерк[0m":
                ab = max_health-health
                hb = ab*(level/3)
            hede = 0
            if user_class == "[31mДемон[0m":
                hede = health/10
            critmdamage = int(mdamage*critD)
            ttdamage = round(((tdamage*sc*ph+hb)/100*(100-enemy_def)), 1)
            critdamage = int(ttdamage*critD)
            ph = 1
            if m_evade >= e_evade: #Атака
                if crit < critC:
                    print("*КРИТИЧЕСКИЙ УРОН*")
                    if user_class != "[36mМаг[0m":
                        critdamage_d = critdamage+hede
                        tdamage_d = ttdamage+hede
                    else:
                        critdamage_d = critmdamage+hede
                        tdamage_d = mdamage+hede
                    if tdamage_d < 0:
                        critdamage_d = critdamage/10
                        print("Вы ПРОБИЛИ броню противника")
                    enemy_hp = round((enemy_hp-critdamage_d), 1)
                    print(f"Вы нанесли {critdamage_d} урона врагу!")
                    if Vampirism != 0:
                        crit_v = int(critdamage_d/100*Vampirism)
                        if health < max_health:
                            health = health+crit_v
                            if health > max_health:
                                health = max_health     
                            print(f"Вы излечились на {crit_v} здоровья благодаря вампиризму")
                        else:
                            print("Вы полны жизненной энергией и не может больше исцеляться")
                    
                    
                else:
                    if user_class == "[31mБерсерк[0m":
                        ab = max_health-health
                        hb = hb*(level/3)
                    if user_class != "[36mМаг[0m":
                        critdamage_d = critdamage+hede
                        tdamage_d = ttdamage+hede
                    else:
                        critdamage_d = critmdamage+hede
                        tdamage_d = mdamage+hede
                    if tdamage_d < 0:
                        print("Вы не пробили броню противника")
                        tdamage_d = 0
                    else:
                        enemy_hp = round((enemy_hp-tdamage_d), 1)
                        print(f"Вы нанесли {tdamage_d} урона врагу!")
                    if Vampirism != 0:
                        tdamage_d -= hede
                        dmg_v = int(tdamage_d/100*Vampirism)
                        if health < max_health:
                            health = health+dmg_v
                            print(f"Вы излечились на {dmg_v} здоровья благодаря вампиризму")
                        else:
                            print("Вы полны жизненной энергией и не может больше исцеляться")
            else:    #Уворот
                print("Враг увернулся от атаки!")

                #Атака врага
            if stun <= StunC:
                        print("Противник получил оглушение и не нанёс урона")
                        if Regen != 0 and health < max_health:
                            dmg_v = int(max_health/100*Vampirism_hp)
                            health = health+Regen+dmg_v
                            theal = Regen+dmg_v           
                            print(f"Вы излечились на {theal} хп, благодаря регенерации")
            else:
                e_evadeD = ((enemy_speed/100)*5)
                m_evadeD = ((speed/100)*5)
                if enemy_speed > speed:
                            a = int(speed-m_evadeD)
                            b = int(enemy_speed+e_evadeD)
                            c = int(enemy_speed-e_evadeD)
                            m_evade = random.randint(a, b)
                            e_evade = random.randint(c, b)
                else:
                            a = int(speed-m_evadeD)
                            b = int(speed+m_evadeD)
                            c = int(enemy_speed-e_evadeD)
                            m_evade = random.randint(a, b)
                            e_evade = random.randint(c, b)

                if e_evade <= m_evade:
                            print("Вы увернулись от удара")
                            if Regen != 0 and health < max_health:
                                dmg_v = int(max_health/100*Vampirism_hp)
                                health = health+Regen+dmg_v
                                theal = Regen+dmg_v
                                print(f"Вы излечились на {theal} хп, благодаря регенерации")
                else:
                                    absc = random.randint(1, 100)
                                    if absc < Abs:
                                        print("Вы успешно защитились и поглотили 90% урона")
                                        if shield >= 1:
                                            shield = int(shield-round((enemy_ddamage/100*10), 1))
                                            if shield < 0:
                                                shieldd = 0-shield
                                                health = health-shieldd
                                                if fdefence > 50:
                                                    fdefence -= 1
                                                print(f"Вы потеряли {shieldd} жизней после удара врага")
                                                print("Щит разрушен")
                                            else:
                                                print(f"Осталось прочности барьера: {shield}")
                                        else:   
                                            r_damage = round((enemy_ddamage/100*10), 1)                  
                                            print(f"Вы потеряли {r_damage} жизней после удара врага")
                                            health = health-r_damage
                                            if fdefence > 50:
                                                fdefence -= 1
                                        if Regen != 0 and health < max_health:
                                            dmg_v = int(max_health/100*Vampirism_hp)
                                            health = health+Regen+dmg_v
                                            theal = Regen+dmg_v
                                            print(f"Вы излечились на {theal} хп, благодаря регенерации")
                                    else:
                                            if shield >= 1:
                                                shield = int(shield-enemy_ddamage)
                                                if shield < 0:
                                                    shieldd = 0-shield
                                                    health = health-shieldd
                                                    print(f"Вы потеряли {shieldd} жизней после удара врага")
                                                    print("Щит разрушен")
                                                    if fdefence > 50:
                                                        fdefence -= 1
                                                else:
                                                    print(f"Осталось прочности барьера: {shield}")
                                            else:
                                                health = health-enemy_ddamage
                                                print(f"Вы потеряли {enemy_ddamage} жизней после удара врага")
                                                if fdefence > 50:
                                                    fdefence -= 1
                                                if Regen != 0 and health < max_health:
                                                    dmg_v = int(max_health/100*Vampirism_hp)
                                                    health = health+Regen+dmg_v
                                                    theal = Regen+dmg_v
                                                    print(f"Вы излечились на {theal} хп, благодаря регенерации")
                                            
        elif your_move == 1:
                    e_evadeD = ((enemy_speed/100)*5)
                    m_evadeD = ((speed/100)*5)
                    if enemy_speed > speed:
                        a = int(speed-m_evadeD)
                        b = int(enemy_speed+e_evadeD)
                        c = int(enemy_speed-e_evadeD)
                        m_evade = random.randint(a, b)
                        e_evade = random.randint(c, b)
                    else:
                        a = int(speed-m_evadeD)
                        b = int(speed+m_evadeD)
                        c = int(enemy_speed-e_evadeD)
                        m_evade = random.randint(a, b)
                        e_evade = random.randint(c, b)

                    if e_evade <= m_evade:
                        print("Вы увернулись от удара")
                        if Regen != 0 and health < max_health:
                            dmg_v = int(max_health/100*Vampirism_hp)
                            health = health+Regen+dmg_v
                            theal = Regen+dmg_v
                            print(f"Вы излечились на {theal} хп, благодаря регенерации")
                        if shield == 0:                 
                            shield = max_health/10
                            print(f"Вы получили щит в виде {shield} щита")
                        else:
                            print("У вас уже есть щит!")
                    else:
                                if shield == 0:                 
                                    shield = max_health/10
                                    print(f"Вы получили щит в виде {shield} щита")
                                else:
                                    print("У вас уже есть щит!")
                                absc = random.randint(1, 100)
                                if absc < Abs:
                                    print("Вы успешно защитились и поглотили 90% урона")
                                    if shield >= 1:
                                        shield = int(shield-round((enemy_ddamage/100*10), 1))
                                        if shield < 0:
                                            shieldd = 0-shield
                                            health = health-shieldd
                                            print(f"Вы потеряли {shieldd} жизней после удара врага")
                                            print("Щит разрушен")
                                        else:
                                            print(f"Осталось прочности барьера: {shield}")
                                    else:   
                                        r_damage = round((enemy_ddamage/100*10), 1)                  
                                        print(f"Вы потеряли {r_damage} жизней после удара врага")
                                        health = health-r_damage
                                    if Regen != 0 and health < max_health:
                                        dmg_v = int(max_health/100*Vampirism_hp)
                                        health = health+Regen+dmg_v
                                        theal = Regen+dmg_v
                                        print(f"Вы излечились на {theal} хп, благодаря регенерации")
                                else:
                                        if shield >= 1:
                                            shield = int(shield-enemy_ddamage)
                                            if shield < 0:
                                                shieldd = 0-shield
                                                health = health-shieldd
                                                print(f"Вы потеряли {shieldd} жизней после удара врага")
                                                print("Щит разрушен")
                                            else:
                                                print(f"Осталось прочности барьера: {shield}")
                                        else:
                                            health = health-enemy_ddamage
                                            print(f"Вы потеряли {enemy_ddamage} жизней после удара врага")
                                            if Regen != 0 and health < max_health:
                                                dmg_v = int(max_health/100*Vampirism_hp)
                                                health = health+Regen+dmg_v
                                                theal = Regen+dmg_v
                                                print(f"Вы излечились на {theal} хп, благодаря регенерации")
        elif your_move == 2:
                    e_evadeD = ((enemy_speed/100)*5)
                    m_evadeD = ((speed/100)*5)
                    if enemy_speed > speed:
                        a = int(speed-m_evadeD)
                        b = int(enemy_speed+e_evadeD)
                        c = int(enemy_speed-e_evadeD)
                        m_evade = random.randint(a, b)
                        e_evade = random.randint(c, b)
                    else:
                        a = int(speed-m_evadeD)
                        b = int(speed+m_evadeD)
                        c = int(enemy_speed-e_evadeD)
                        m_evade = random.randint(a, b)
                        e_evade = random.randint(c, b)

                    if e_evade <= m_evade:
                        print("Вы увернулись от удара")
                        if Regen != 0 and health < max_health:
                            dmg_v = int(max_health/100*Vampirism_hp)
                            health = health+Regen+dmg_v
                            theal = Regen+dmg_v
                            print(f"Вы излечились на {theal} хп, благодаря регенерации")
                        if health < max_health:
                            health += max_health/20
                            c = max_health/20
                            print(f"Вы излечились на {c} хп")
                        else:
                            print("У вас и так максимум хп")
                    else:
                                if health < max_health:
                                    health += max_health/20
                                    c = max_health/20
                                    print(f"Вы излечились на {c} хп")
                                else:
                                    print("У вас и так максимум хп")
                                absc = random.randint(1, 100)
                                if absc < Abs:
                                    print("Вы успешно защитились и поглотили 90% урона")
                                    if shield >= 1:
                                        shield = int(shield-round((enemy_ddamage/100*10), 1))
                                        if shield < 0:
                                            shieldd = 0-shield
                                            health = health-shieldd
                                            print(f"Вы потеряли {shieldd} жизней после удара врага")
                                            print("Щит разрушен")
                                        else:
                                            print(f"Осталось прочности барьера: {shield}")
                                    else:   
                                        r_damage = round((enemy_ddamage/100*10), 1)                  
                                        print(f"Вы потеряли {r_damage} жизней после удара врага")
                                        health = health-r_damage
                                    if Regen != 0 and health < max_health:
                                        dmg_v = int(max_health/100*Vampirism_hp)
                                        health = health+Regen+dmg_v
                                        theal = Regen+dmg_v
                                        print(f"Вы излечились на {theal} хп, благодаря регенерации")
                                else:
                                        if shield >= 1:
                                            shield = int(shield-enemy_ddamage)
                                            if shield < 0:
                                                shieldd = 0-shield
                                                health = health-shieldd
                                                print(f"Вы потеряли {shieldd} жизней после удара врага")
                                                print("Щит разрушен")
                                            else:
                                                print(f"Осталось прочности барьера: {shield}")
                                        else:
                                            health = health-enemy_ddamage
                                            print(f"Вы потеряли {enemy_ddamage} жизней после удара врага")
                                            if Regen != 0 and health < max_health:
                                                dmg_v = int(max_health/100*Vampirism_hp)
                                                health = health+Regen+dmg_v
                                                theal = Regen+dmg_v
                                                print(f"Вы излечились на {theal} хп, благодаря регенерации")
        elif your_move == 3: #Парирование
                    tspeed = speed*1.05
                    e_evadeD = ((enemy_speed/100)*5)
                    m_evadeD = ((tspeed/100)*5)
                    if enemy_speed > tspeed:
                        a = int(speed-m_evadeD)
                        b = int(enemy_speed+e_evadeD)
                        c = int(enemy_speed-e_evadeD)
                        m_evade = random.randint(a, b)
                        e_evade = random.randint(c, b)
                    else:
                        a = int(tspeed-m_evadeD)
                        b = int(tspeed+m_evadeD)
                        c = int(enemy_speed-e_evadeD)
                        m_evade = random.randint(a, b)
                        e_evade = random.randint(c, b)

                    if e_evade <= m_evade:
                        print("Вы увернулись от удара")
                        if Regen != 0 and health < max_health:
                            dmg_v = int(max_health/100*Vampirism_hp)
                            health = health+Regen+dmg_v
                            theal = Regen+dmg_v
                            print(f"Вы излечились на {theal} хп, благодаря регенерации")
                    else:
                                absc = random.randint(1, 100)
                                if absc < Abs:
                                    print("Вы успешно защитились и поглотили 90% урона")
                                    if shield >= 1:
                                        shield = int(shield-round((enemy_ddamage/100*10), 1))
                                        if shield < 0:
                                            shieldd = 0-shield
                                            health = health-shieldd
                                            print(f"Вы потеряли {shieldd} жизней после удара врага")
                                            print("Щит разрушен")
                                        else:
                                            print(f"Осталось прочности барьера: {shield}")
                                    else:   
                                        r_damage = round((enemy_ddamage/100*10), 1)                  
                                        print(f"Вы потеряли {r_damage} жизней после удара врага")
                                        health = health-r_damage
                                    if Regen != 0 and health < max_health:
                                        dmg_v = int(max_health/100*Vampirism_hp)
                                        health = health+Regen+dmg_v
                                        theal = Regen+dmg_v
                                        print(f"Вы излечились на {theal} хп, благодаря регенерации")
                                else:
                                        if shield >= 1:
                                            shield = int(shield-enemy_ddamage)
                                            if shield < 0:
                                                shieldd = 0-shield
                                                health = health-shieldd
                                                print(f"Вы потеряли {shieldd} жизней после удара врага")
                                                print("Щит разрушен")
                                            else:
                                                print(f"Осталось прочности барьера: {shield}")
                                        else:
                                            health = health-enemy_ddamage
                                            print(f"Вы потеряли {enemy_ddamage} жизней после удара врага")
                                            if Regen != 0 and health < max_health:
                                                dmg_v = int(max_health/100*Vampirism_hp)
                                                health = health+Regen+dmg_v
                                                theal = Regen+dmg_v
                                                print(f"Вы излечились на {theal} хп, благодаря регенерации")
        health = int(health)
        
        print(f"Осталось {health} жизней")
        print(f"Осталось жизней у противника: {enemy_hp}")
        print(" ")
        if autobattle == 0:
            time.sleep(1.5)
        if enemy_hp <= 0:
            if user_class == "[36mТолстяк[0m":
                max_health += 5
                print("Максимальное здоровье повышено")
            reward()
            if autobattle == 0:
                time.sleep(1.5)
            elif autobattle == 1:
                time.sleep(3.5)
            return
        elif health <= 0:
            if lives == 1:
                print("Вы проиграли, попробуй начать сначала!")
                if reward_game >= 1:
                    if reward_game == 2:
                        reward_points = int(((step/3)/2))
                        r_coins += reward_points
                    else:
                        reward_points = int((step/3))
                        r_coins += reward_points
                    print(f"Вы получили {reward_points} наградных монет")
                    with open('profile.json', 'w', encoding='utf-8') as p:
                        p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                        p.write('}]')
                    FileEncrypt('profile.json')
                a = input("Вы хотите начать сначала? (Д/Н): ")
                if a == "Д" or a == "д":
                    set_stats()
                else:
                    print("Ну нет так нет :)  ")
                    power_points = round((max_health/5)+udamage+(speed/3)+(defence/3)+(critC/5)+(critD*5)+(damage/3)+(StunC/3)+(Abs/3)+(Vampirism/2)+(Regen/2)+(hpdamage/2)+(Vampirism_hp/2), 2)
                    critty = int(critD*100)
                    exp = int(exp)
                    print(f"[36mВаш класс: {user_class}[0m")
                    print(f"[36mВаш уровень силы: [33m{power_points}[0m")
                    print(f"[36mВаш уровень: [33m{level}[0m")
                    print(f"[36mВаш опыт: [33m{exp}/{exp_cap}[0m")
                    print(f"[36mВаши очки улучшений: [33m{upgrade}[0m")
                    print(f"[36mВаше здоровье: [33m{health}/{max_health}[0m")
                    print(f"[36mВаша регенерация: [33m{Regen}[0m")
                    print(f"[36mВаша атака: [33m{damage}[0m")
                    print(f"[36mВаш шанс увернуться: [33m{speed}%[0m")
                    print(f"[36mВаш шанс оглушения: [33m{StunC}%[0m")
                    print(f"[36mВаша защита: [33m{defence}")
                    print(f"[36mВаш шанс усил.защиты: [33m{Abs}%[0m")
                    print(f"[36mВаше усиление атаки: [33m{udamage}[0m")
                    print(f"[36mВаш крит.урон: [33m{critty}%[0m")
                    print(f"[36mВаш крит.шанс: [33m{critC}%[0m")
                    if Vampirism != 0:
                        print(f"[36mВампиризм: [33m{Vampirism}%[0m")
                    print(" ")
                    time.sleep(1000000)
            else:
                lives -= 1
                health = max_health/2
                ph = 5
                print("Вы воскресли!")
    print("========================")
def tutor(secret1):
    print("Приветствую тебя в игре таинственный лабиринт!")
    time.sleep(0.2)
    print("Тут совсем нет графики, а только текст. Игра-Квиз")
    time.sleep(0.2)
    print("В игре есть магазин, что бы узнать что продаётся - напиши Магазин(Попробуй)")
    time.sleep(0.2)
    first_ask(secret1)
    print("Вот, вы увидели что есть в магазине, теперь перейдём к самой игре!")
    time.sleep(0.2)
    print("Тут вам предстоит ходит по лабиринту, и убивать монстров, цель игры, пройти сквозь весь лабиринт и зачистить его!")
    time.sleep(0.2)
    print("Чем дольше вы будете ходить, тем сильнее будут монстры!")
    time.sleep(0.2)
    print("Что-бы ходить по лабиринту, пишите - 'н' - вниз, 'в' - вверх, 'л' - влево, 'п' - вправо'")
    time.sleep(0.2)
    print("Так-же в игре разные характеристики такие как: 'Защита', 'Усиление атаки', 'Ул.Защита', 'Скорость', 'Оглушение', 'Регенерация' и 'Вампиризм'")
    print(" ")
    print("Защита: Буду приводить примеры, У вас 1 Защита, у врага 3 урона, первым ударом он нанесёт вам 2 урона, т.к сработала 1 защита, на следующий ход он нанесёт вам 1 урон. Броня нарастает по ходу боя. Если урон врага ушёл в минус, вы будете лечиться каждый ход сверх максимального хп.")
    print(" ")
    print("Усиление атаки: работает по тому же принципу что и защита")
    print(" ")
    print("Ул. Защита: Это процент который позволяет с некоторым шансом получить лишь 10% урона")
    print(" ")
    print("Скорость: Это шанс увернутся и тем самым проигнорировать урон")
    print(" ")
    print("Оглушение: Позволяет оглушить противника, в момент оглушения он не совершит удар, а вы будете регенерировать если у вас есть регенерация")
    print(" ")
    print("Регенерация: После каждого хода, если у вас не максимальное Хп, будет увеличивать текущий запас хп на своё значение(Реген 5, будет в конце каждого хода в бою лечить на 5) (НЕ ВЛИЯЕТ НА РЕГЕНЕРАЦИЮ ПОСЛЕ ПОЛНОЙ БЛОКИРОВКИ И ПОСЛЕ ОБЫЧНОГО ХОДА)")
    print(" ")
    print("Вампиризм: Лечит вас в зависимости от вашего урона, вы нанесли 100 урона, а ваш вампиризм 10%, вы полечитесь на 10% - СВЕРХ ВАШЕГО ХП!")
    print(" ")
    print("А так же классы, их в игре 8. 3 из них вы можете выбрать 4-ый стандартный(Введите что угодно Кроме того что вам предлогают), при сборке сета для нужного класса, он улучшается, Вору - Ассасин, Убийце - Вампир, Танку - Рыцарь.")
    time.sleep(10)
def tutor_ask(secret1):
    is_tutor = input("Вы хотите пройти обучение?(Да/Нет):")
    if is_tutor == "Да" or is_tutor == "да":
        tutor(secret1)
        return()
    elif is_tutor == "Нет" or is_tutor == "нет":
        return()
    else:
        tutor_ask(secret1)



def printMaze(maze, markX=None, markY=None):
    """Displays the maze data structure in the maze argument. The
    markX and markY arguments are coordinates of the current
    '@' location of the algorithm as it generates the maze."""

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if markX == x and markY == y:
                # Display the '@' mark here:
                print(MARK, end='')
            else:
                # Display the wall or empty space:
                print(maze[(x, y)], end='')
        print() # Print a newline after printing the row.

def dead():
    time.sleep(999999999)
def visit(x, y):
    global boss
    global Knight_Vampire
    global Assassin_set
    global Vampire_set
    global Knight_set
    global Demigod_set
    global equip
    global user_class
    global StunC
    global Regen
    global Abs
    global Vampirism
    global elite_enemy
    global boss_enemy
    global exp_cap
    global critD
    global critC
    global damage
    global defence
    global udamage
    global upgrade
    global exp
    global level
    global max_health
    global kort_buy
    global coins
    global health
    global block
    global weapon
    global code_weapon
    global step
    global speed
    global bot_buy
    global inventory
    global autobattle
    global Vampirism_hp
    global hpdamage
    global enemy
    global r_coins
    global location
    global extra_dif
    """"Carve out" empty spaces in the maze at x, y and then
    recursively move to neighboring unvisited spaces. This
    function backtracks when the mark has reached a dead end."""
    
    rand = random.randint(1, 100)
    if block == 1:
        time.sleep(0.001)
    else:
        if rand >= 80:
            answ = menu(f'Вы нашли противника', ['Напасть','Убежать'], 'red')
            if answ == 0:
                fight()
                if elite_enemy == 1:
                    elite_enemy = 0
                    maze[(x, y)] = ELITE_ENEMY_DEF
                elif boss_enemy == 1:
                    maze[(x, y)] = BOSS_ENEMY_DEF
                    boss_enemy = 0
                else:
                    maze[(x, y)] = DEF_ENEMY
            elif answ == 1:
                chance = random.randint(1, 100)
                if chance >= 80:
                    print("Вам не удалось сбежать и начался бой!")
                    time.sleep(0.2)
                    fight()
                    maze[(x, y)] = DEF_ENEMY
                else:
                    print("Вы избежали столкновения")
                    maze[(x, y)] = ENEMY
            else:
                chance = random.randint(1, 100)
                if chance >= 80:
                    print("Вам не удалось сбежать и начался бой!")
                    time.sleep(0.2)
                    fight()
                    maze[(x, y)] = DEF_ENEMY
                else:
                    print("Вы избежали столкновения")
                    maze[(x, y)] = ENEMY            
        elif rand == 50:
            gift = random.randint(50, 125)
            print(f"Обнаружено сокровище! вы получили: {gift}©")
            time.sleep(1.5)
            coins = coins+gift
            maze[(x, y)] = TREASURE
        elif rand < 5:
            event()
            maze[(x, y)] = ROOM
        else:
            maze[(x, y)] = EMPTY # "Carve out" the space at x, y.
    print(f'[33m©:{coins}[0m, [31m♥:{health}[0m')
    printMaze(maze, x, y) # Display the maze as we generate it.
    print('\n\n')

    while True:
        # Check which neighboring spaces adjacent to
        # the mark have not been visited already:
        unvisitedNeighbors = []
        if y > 1 and (x, y - 2) not in hasVisited:
            unvisitedNeighbors.append(NORTH)

        if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
            unvisitedNeighbors.append(SOUTH)

        if x > 1 and (x - 2, y) not in hasVisited:
            unvisitedNeighbors.append(WEST)

        if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
            unvisitedNeighbors.append(EAST)

        if len(unvisitedNeighbors) == 0:
            # BASE CASE
            # All neighboring spaces have been visited, so this is a
            # dead end. Backtrack to an earlier space:
            return
        else:
            # RECURSIVE CASE
            # Randomly pick an unvisited neighbor to visit:
            a = len(unvisitedNeighbors)
            a -= 1
            unvisitedNeighbors.append("Меню")
            try:
                nextIntersection = menu(f'Меню \n©:{coins}, ♥:{health}', unvisitedNeighbors, 'red')
            except Exception as e:
                print(e)
                time.sleep(10)
            if nextIntersection > a:
                nextIntersection = "Меню"
            else:
                nextIntersection = unvisitedNeighbors[nextIntersection]
            if nextIntersection == "Меню":
                    if nextIntersection == "Меню" or nextIntersection == "меню":
                        nextIntersection = menu(f'Меню \n©:{coins}, ♥:{health}', ['Магазин','Прокачка','Характеристики','Инвентарь', 'Меню крафта', 'Сохранение', 'Локация', 'Автобой', 'Закончить игру'], 'red')
                        if nextIntersection == 0:
                            shope()                                     
                        elif nextIntersection == 1:
                            while True:
                                if upgrade >= 1:
                                        upg = menu(f'Улучшение - У вас {upgrade} очков улучшения', ['М.Хп - 5','Усиление атаки - 1','Скорость - 3','Защита - 3','Крит шанс - 5%','Крит урон - 20%','Урон - 3','Выйти'], 'red')
                                        if upg == 0:
                                            max_health = max_health+5
                                            upgrade = upgrade-1
                                        elif upg == 1:
                                            udamage = udamage+1
                                            upgrade = upgrade-1
                                        elif upg == 2:
                                            speed = speed+3
                                            upgrade = upgrade-1
                                        elif upg == 3:
                                            defence = defence+3
                                            upgrade = upgrade-1
                                        elif upg == 4:
                                            critC = critC+5
                                            upgrade = upgrade-1
                                        elif upg == 5:
                                            critD = critD+0.2
                                            upgrade = upgrade-1
                                        elif upg == 6:
                                            damage = damage+3
                                            upgrade = upgrade-1
                                        elif upg == 7:
                                            print("Вы отказались от улучшения")
                                            break
                                else:
                                    print("У вас нет очков улучшения")
                                    break
                        elif nextIntersection == 2:
                            critty = int(critD*100)
                            Vampirism_hp = round(Vampirism_hp, 2)
                            max_health = round(max_health, 2)
                            hpdamage = round(hpdamage, 2)
                            speed = round(speed, 2)
                            udamage = round(udamage, 2)
                            power_points = round((max_health/5)+udamage+(speed/3)+(defence/3)+(critC/5)+(critD*5)+(damage/3)+(StunC/3)+(Abs/3)+(Vampirism/2)+(Regen/2)+(hpdamage/2)+(Vampirism_hp/2), 2)
                            if power_points < 30:
                                rank = "[32m[F]"
                            elif 100 > power_points > 30:
                                rank = "[32m[E]"
                            elif 175 > power_points > 100:
                                rank = "[32m[D]"
                            elif 250 > power_points > 175:
                                rank = "[36m[C]"
                            elif 500 > power_points > 250:
                                rank = "[36m[B]"
                            elif 1000 > power_points > 500:
                                rank = "[31m[A]"
                            elif 1500 > power_points > 1000:
                                rank = "[33m[S]"
                            elif 2200 > power_points > 1500:
                                rank = "[33m[S+]"
                            elif 3000 > power_points > 2200:
                                rank = "[33m[SS]"
                            elif 5000 > power_points > 3000:
                                rank = "[35m[H]"
                            elif 10000 > power_points > 5000:
                                rank = "[33m[G]"
                            elif 50000 > power_points > 10000:
                                rank = "[33m[SSS]"
                            elif 100000 > power_points > 50000:
                                rank = "[33m[SG]"
                            elif 1000000 > power_points > 100000:
                                rank = "[33m[Godly]"
                            elif 10000000 > power_points > 1000000:
                                rank = "[31m[Sacred deity]"
                            elif 100000000 > power_points > 10000000:
                                rank = "[31m[Unknown God]"
                            elif 1000000000 > power_points > 100000000:
                                rank = "[31m[Someone from beyond]"
                            elif 10000000000 > power_points > 1000000000:
                                rank = "[31m[What?]"
                            elif 100000000000 > power_points > 10000000000:
                                rank = "[31m[What???]"
                            elif power_points > 100000000000:
                                rank = "[31m[Stop hacking bro!]"
                            print(f"[36mВаш класс: {user_class} {rank}[0m")
                            print(f"[36mВаш уровень силы: [33m{power_points}[0m")
                            print(f"[36mВаш уровень: [33m{level}[0m")
                            exp = int(exp)
                            exp_cap = int(exp_cap)
                            print(f"[36mВаш опыт: [33m{exp}/{exp_cap}[0m")
                            print(f"[36mВаши очки улучшений: [33m{upgrade}[0m")
                            print(f"[36mВаше здоровье: [33m{health}/{max_health}[0m")
                            if hpdamage != 0:
                                print(f"[36mУрон от здоровья: [33m{hpdamage}%[0m")
                            if Vampirism_hp != 0:
                                print(f"[36mВампиризм от здорвья: [33m{Vampirism_hp}%[0m")
                            print(f"[36mВаша регенерация: [33m{Regen}[0m")
                            print(f"[36mВаша атака: [33m{damage}[0m")
                            print(f"[36mВаша ловкость: [33m{speed}[0m")
                            print(f"[36mВаш шанс оглушения: [33m{StunC}%[0m")
                            print(f"[36mВаша защита: [33m{defence}")
                            print(f"[36mВаш шанс усил.защиты: [33m{Abs}%[0m")
                            print(f"[36mВаше усиление атаки: [33m{udamage}[0m")
                            print(f"[36mВаш крит.урон: [33m{critty}%[0m")
                            print(f"[36mВаш крит.шанс: [33m{critC}%[0m")
                            if Vampirism != 0:
                                print(f"[36mВампиризм: [33m{Vampirism}%[0m")
                            time.sleep(5)
                        elif nextIntersection == 3:
                            inv()
                        elif nextIntersection == 4:
                            craft_menu()
                        elif nextIntersection == 5:
                            save()
                        elif nextIntersection == 6:
                            if step <= 150:
                                locs = ["Лес"]
                            elif 150 < step < 500:
                                locs = ["Лес", "Ущелье"]
                            elif 500 <= step < 1000:
                                locs = ["Лес", "Ущелье", "Преисподня"]
                            elif 10000 > step > 1000:
                                locs = ["Лес", "Ущелье", "Преисподня", "Высшее королевство"]
                            elif step > 10000:
                                locs = ["Лес", "Ущелье", "Преисподня", "Высшее королевство", "Долина конца"]
                            choose_location = menu(f'Выберите локацию:', locs, 'green')
                            if choose_location == 0:
                                location = "Лес"
                                if 500 > step >= 150:
                                    extra_dif = 2
                                if 1000 > step >= 500:
                                    extra_dif = 3.5
                                if step >= 1000:
                                    extra_dif = 5
                            elif choose_location == 1:
                                location = "Ущелье"
                                if 500 > step >= 150:
                                    extra_dif = 1
                                if 1000 > step >= 500:
                                    extra_dif = 3
                                if step >= 1000:
                                    extra_dif = 4.5
                            elif choose_location == 2:
                                location = "Преисподня"
                                if 500 > step >= 150:
                                    extra_dif = 1
                                if 1000 > step >= 500:
                                    extra_dif = 1
                                if step >= 1000:
                                    extra_dif = 2
                            elif choose_location == 3:
                                location = "Высшее королевство"
                            elif choose_location == 4:
                                location = "Долина конца"
                        elif nextIntersection == 7:
                            di = ["Да", "Нет"]
                            choose_autobattle = menu(f'Включить автобой?:', di, 'red')
                            if choose_autobattle == 0:
                                autobattle = 1
                            else:
                                autobattle = 0
                        elif nextIntersection == 8:
                            print("Вы проиграли, попробуй начать сначала!")
                            if reward_game >= 1:
                                if reward_game == 2:
                                    reward_points = int(((step/3)/2))
                                    r_coins += reward_points
                                else:
                                    reward_points = int((step/3))
                                    r_coins += reward_points
                                print(f"Вы получили {reward_points} наградных монет")
                                with open('profile.json', 'w', encoding='utf-8') as p:
                                    p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                    p.write('}]')
                                FileEncrypt('profile.json')
                            a = input("Вы хотите начать сначала? (Д/Н): ")
                            if a == "Д" or a == "д":
                                set_stats()
                            else:
                                print("Ну нет так нет :)  ")
                                critty = int(critD*100)
                                print(f"[36mВаш класс: {user_class}[0m")
                                print(f"[36mВаш уровень: [33m{level}[0m")
                                print(f"[36mВаш опыт: [33m{exp}/{exp_cap}[0m")
                                print(f"[36mВаши очки улучшений: [33m{upgrade}[0m")
                                print(f"[36mВаше здоровье: [33m{health}/{max_health}[0m")
                                print(f"[36mВаша регенерация: [33m{Regen}[0m")
                                print(f"[36mВаша атака: [33m{damage}[0m")
                                print(f"[36mВаш шанс увернуться: [33m{speed}%[0m")
                                print(f"[36mВаш шанс оглушения: [33m{StunC}%[0m")
                                print(f"[36mВаша защита: [33m{defence}")
                                print(f"[36mВаш шанс усил.защиты: [33m{Abs}%[0m")
                                print(f"[36mВаше усиление атаки: [33m{udamage}[0m")
                                print(f"[36mВаш крит.урон: [33m{critty}%[0m")
                                print(f"[36mВаш крит.шанс: [33m{critC}%[0m")
                                if Vampirism != 0:
                                    print(f"[36mВампиризм: [33m{Vampirism}%[0m")
                                print(" ")
                                time.sleep(1000000)
                            block = 1
                            visit(x, y)

            
                    print("Вы ввели не тот символ!")
                    block = 1
                    visit(x, y)
            if health < max_health:
                health = health+1
                print("Вы полечились на 1хп")
            block = 0
            try:
                # Move the mark to an unvisited neighboring space:
                if nextIntersection == NORTH:
                    nextX = x
                    nextY = y - 2
                    maze[(x, y - 1)] = EMPTY # Connecting hallway.
                elif nextIntersection == SOUTH:
                    nextX = x
                    nextY = y + 2
                    maze[(x, y + 1)] = EMPTY # Connecting hallway.
                elif nextIntersection == WEST:
                    nextX = x - 2
                    nextY = y
                    maze[(x - 1, y)] = EMPTY # Connecting hallway.
                elif nextIntersection == EAST:
                    nextX = x + 2
                    nextY = y
                    maze[(x + 1, y)] = EMPTY # Connecting hallway.

                hasVisited.append((nextX, nextY)) # Mark as visited.
                step = step+game_speed
                print(f"Ход: {step}")
                visit(nextX, nextY) # Recursively visit this space.
            except UnboundLocalError as e:
                print(e)
def start():
    global health
    global secret1
    global speed
    global damage
    global max_health
    global user_class
    global udamage
    global defence
    global hasVisited
    global r_coins
    global hunter
    global mage
    global bers
    global dwarf
    global golem
    global goblin
    global fenix
    global demon
    global fatboy
    global elitekill
    global autobattle
    global game_speed
    secret1 = 0
    tutor_ask(secret1)
    time.sleep(1)
    diffs = [1, 2, 3, 4]
    if savee == 0:
        di = ["1 - Лёгкая", "2 - Нормальная", "3 - Сложная", "4 - Для достойных"]
        choose_dif = menu(f'Выберите сложность:', di, 'red')
        if choose_dif == 3:
            total_dif = 4
        if choose_dif == 2:
            total_dif = 3
        if choose_dif == 1:
            total_dif = 2
        if choose_dif == 0:
            total_dif = 1
        if total_dif not in diffs:
            print("Вы ввели не верно!, установлена сложность 2!")
            total_dif = 2
    SEEDa = input("Введите сид игры, если не важен, напишите с, тогда он будет случайным: ")
    SEED = SEEDa.lower()
    if SEED == "с":
        SEED = random.randint(0,99999)
        print(f"Сид игры: {SEED}")
        random.seed(SEED)
    else:
        reward_game = 0
        print("Вы не получите награду за данную игру!")
        random.seed(SEED)
        print(f"Сид игры: {SEED}")
    di = ["Да", "Нет"]
    choose_autobattle = menu(f'Включить автобой?:', di, 'red')
    if choose_autobattle == 0:
        autobattle = 1
    else:
        autobattle = 0
    di = ["1ход - 1 шаг", "1ход - 3 шага", "1ход - 5шагов", "1ход - 7шагов"]
    choose_gamespeed = menu(f'Выберите скорость игры:', di, 'red')
    if choose_gamespeed == 0:
        game_speed = 1
    elif choose_gamespeed == 1:
        game_speed = 3
    elif choose_gamespeed == 2:
        game_speed = 5
    elif choose_gamespeed == 3:
        game_speed = 7
    print("Генерация...")
    if endless_game == 0 and savee == 0:
        print(f"[33mВаши наградные монеты: {r_coins}")
        print("[36mВоин: Защита 10, Макс.ХП 5[32m [Т]")
        print("[33mОсобенность: Нету, базовый класс") 
        print("[31mУбийца: Усиление урона 1, Макс.ХП 5, Ловкость 1[32m [У]")
        print("[33mОсобенность: Нету, базовый класс") 
        print("[32mВор: Ловкость 3, Урон 3[32m [В]")
        print("[33mОсобенность: Нету, базовый класс")
        hunter_price = 4500
        if hunter == 1:
            print("[32m[Спец.Класс]Охотник: Ловкость 3, Урон 3[0m [32m[О]")
            print("[33mОсобенность: Имеет шанс нанести двойной урон.")
        else:
            print("[32m[Спец.Класс]Охотник: Ловкость 3, Урон 3[0m [31m[О]")
            print("[33mОсобенность: Имеет шанс нанести двойной урон.")
        mage_price = 5500
        if mage == 1:
            print("[36m[Спец.Класс]Маг: Магия 5, Макс.Хп 5[0m [32m[М]")
            print("[33mОсобенность: Весь урон становитсья магическим, Магический урон пробивает защиту врагов, но не нарастает по ходу боя.")
        else:
            print("[36m[Спец.Класс]Маг: Магия 5, Макс.Хп 5[0m [31m[М]")
            print("[33mОсобенность: Весь урон становитсья магическим, Магический урон пробивает защиту врагов, но не нарастает по ходу боя.")
        bers_price = 7500
        if bers == 1:
            print("[31m[Спец.Класс]Берсерк: Урон 2, Макс.Хп 25[0m [32m[Б]")
            print("[33mОсобенность: Урон увеличивается в зависимости от хп которых не хватает.")
        else:
            print("[31m[Спец.Класс]Берсерк: Урон 2, Макс.Хп 25[0m [31m[Б]")
            print("[33mОсобенность: Урон увеличивается в зависимости от хп которых не хватает.")
        dwarf_price = 5000
        if dwarf == 1:
            print("[35m[Спец.Класс]Дварф: Защита 5, Макс.Хп 10[0m [32m[Д]")
            print("[33mОсобенность: Скидка на улучшение предметов 25%, т.е вместо 10% от стоимости предмета, цена на улучшение 7.5%.")
        else:
            print("[35m[Спец.Класс]Дварф: Защита 5, Макс.Хп 10[0m [31m[Д]")
            print("[33mОсобенность: Скидка на улучшение предметов 25%, т.е вместо 10% от стоимости предмета, цена на улучшение 7.5%.")
        golem_price = 6500
        if golem == 1:
            print("[36m[Спец.Класс]Голем: Защита 25, Макс.Хп 15[0m [32m[Г]")
            print("[33mОсобенность: Получает поглащение в начале боя которое зависит от кол-ва Макс.Хп и Защиты.")
        else:
            print("[36m[Спец.Класс]Голем: Защита 25, Макс.Хп 15[0m [31m[Г]")
            print("[33mОсобенность: Получает поглащение в начале боя которое зависит от кол-ва Макс.Хп и Защиты.")
        goblin_price = 5000
        if goblin == 1:   
            print("[32m[Спец.Класс]Гоблин: Ловкость 3, Урон 2 [0m [32m[ГБ]")
            print("[33mОсобенность: Наносит дополнительный урон в зависимости от имеющегося золота.")
        else:
            print("[32m[Спец.Класс]Гоблин: Ловкость 3, Урон 2 [0m [31m[ГБ]")
            print("[33mОсобенность: Наносит дополнительный урон в зависимости от имеющегося золота.")
        fenix_price = 6000
        if fenix == 1:
            print("[35m[Спец.Класс]Феникс: Ловкость 2, Макс.Хп 10 [0m [32m[Ф]")
            print("[33mОсобенность: Имеет 2 жизни, после смерти взрывается, восстанавливая 50% здоровья и нанося 5-и кратный урон(Может быть критом).")
        else:
            print("[35m[Спец.Класс]Феникс: Ловкость 2, Макс.Хп 10 [0m [31m[Ф]")
            print("[33mОсобенность: Имеет 2 жизни, после смерти взрывается, восстанавливая 50% здоровья и нанося 5-и кратный урон(Может быть критом).")
        demon_price = 7500
        if demon == 1:
            print("[31m[Спец.Класс]Демон: Ловкость 2, Атака 2, Макс.Хп 15 [0m [32m[ДМ]")
            print("[33mОсобенность: Наносит каждый ход дополнительно 10% от своих хп(Сквозь защиту).")
        else:
            print("[31m[Спец.Класс]Демон: Ловкость 2, Атака 2, Макс.Хп 15 [0m [31m[ДМ]")
            print("[33mОсобенность: Наносит каждый ход дополнительно 10% от своих хп(Сквозь защиту).")
        fatboy_price = 6500
        if fatboy == 1:
            print("[36m[Спец.Класс]Толстяк: Макс.Хп 50 [0m [32m[ТС]")
            print("[33mОсобенность: Вся защита превращается в здоровье (1 защита - 5 здоровья)/ После убийства врага +5 здоровья навсегда.")
        else:
            print("[36m[Спец.Класс]Толстяк: Макс.Хп 50 [0m [31m[ТС]")
            print("[33mОсобенность: Вся защита превращается в здоровье (1 защита - 5 здоровья)/ После убийства врага +5 здоровья навсегда.")            
        elite_price = 7000
        if elitekill == 1:
            print("[31m[Спец.Класс]Элитный убийца: Макс.Хп 10, Ловкость 3, Атака 2, Усиление атаки 2 [0m [32m[Э]")
            print("[33mОсобенность: Ловкость усиливает атаку (Атака*(Ловкость/100), если ловкость меньше 100, усиление не действует.")
        else:
            print("[31m[Спец.Класс]Элитный убийца: Макс.Хп 10, Ловкость 3, Атака 2, Усиление атаки 2 [0m [31m[Э]")
            print("[33mОсобенность: Ловкость усиливает атаку (Атака*(Ловкость/100), если ловкость меньше 100, усиление не действует.")
        while True:
            class_pick = input("[33mВыберите класс): ")
            if class_pick == "Т" or class_pick == "т":
                defence = defence+10
                max_health = max_health+5
                health = health+5
                user_class = "[36mВоин[0m"
                break
            elif class_pick == "У" or class_pick == "у":
                udamage = udamage+1
                max_health = max_health+5
                health = max_health
                speed = speed+1
                user_class = "[31mУбийца[0m"
                break
            elif class_pick == "В" or class_pick == "в":
                speed = speed+3
                max_health = max_health+5
                damage = damage+3
                user_class = "[32mВор[0m"
                break
            elif class_pick == "О" and hunter == 1 or class_pick == "о" and hunter == 1:
                speed = speed+3
                damage = damage+3
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[32mОхотник[0m"
                break
            elif class_pick == "О" and hunter == 0 or class_pick == "о" and hunter == 0:
                an = menu(f'Меню покупки класса [{hunter_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < hunter_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Охотника")
                            r_coins -= hunter_price
                            hunter = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
            elif class_pick == "М" and mage == 1 or class_pick == "м" and mage == 1:
                max_health = max_health+5
                health = max_health
                damage = damage+5
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[36mМаг[0m"
                break
            elif class_pick == "М" and mage == 0 or class_pick == "м" and mage == 0:
                an = menu(f'Меню покупки класса [{mage_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < mage_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Мага")
                            r_coins -= mage_price
                            mage = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
            elif class_pick == "Б" and bers == 1 or class_pick == "б" and bers == 1:
                max_health = max_health+25
                health = max_health
                damage = damage+2
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[31mБерсерк[0m"
                break
            elif class_pick == "Б" and bers == 0 or class_pick == "б" and bers == 0:
                an = menu(f'Меню покупки класса [{bers_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < bers_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Берсерка")
                            r_coins -= bers_price
                            bers = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
            elif class_pick == "Д" and dwarf == 1 or class_pick == "д" and dwarf == 1:
                max_health = max_health+10
                health = max_health
                defence = defence+5
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[35mДварф[0m"
                break
            elif class_pick == "Д" and dwarf == 0 or class_pick == "д" and dwarf == 0:
                an = menu(f'Меню покупки класса [{dwarf_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < dwarf_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Дворфа")
                            r_coins -= dwarf_price
                            dwarf = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
            elif class_pick == "Г" and golem == 1 or class_pick == "г" and golem == 1:
                max_health = max_health+15
                health = max_health
                defence = defence+25
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[35mГолем[0m"
                break
            elif class_pick == "Г" and golem == 0 or class_pick == "г" and golem == 0:
                an = menu(f'Меню покупки класса [{golem_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < golem_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Голема")
                            r_coins -= golem_price
                            golem = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
            elif class_pick == "ГБ" and goblin == 1 or class_pick == "гб" and goblin == 1:
                speed = speed+3
                damage = damage+2
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[32mГоблин[0m"
                break
            elif class_pick == "ГБ" and goblin == 0 or class_pick == "гб" and goblin == 0:
                an = menu(f'Меню покупки класса [{goblin_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < goblin_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Гоблина")
                            r_coins -= goblin_price
                            goblin = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
            elif class_pick == "Ф" and fenix == 1 or class_pick == "ф" and fenix == 1:
                speed = speed+2
                max_health = max_health+10
                health = max_health
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[35mФеникс[0m"
                break
            elif class_pick == "Ф" and fenix == 0 or class_pick == "ф" and fenix == 0:
                an = menu(f'Меню покупки класса [{fenix_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < fenix_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Феникса")
                            r_coins -= fenix_price
                            fenix = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
            elif class_pick == "ДМ" and demon == 1 or class_pick == "дм" and demon == 1:
                speed = speed+2
                damage = damage+2
                max_health = max_health+15
                health = max_health
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[31mДемон[0m"
                break
            elif class_pick == "ДМ" and demon == 0 or class_pick == "дм" and demon == 0:
                an = menu(f'Меню покупки класса [{demon_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < demon_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Демона")
                            r_coins -= demon_price
                            demon = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
            elif class_pick == "ТС" and fatboy == 1 or class_pick == "тс" and fatboy == 1:
                max_health = max_health+50
                health = max_health
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[36mТолстяк[0m"
                break
            elif class_pick == "ТС" and fatboy == 0 or class_pick == "тс" and fatboy == 0:
                an = menu(f'Меню покупки класса [{fatboy_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < fatboy_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Толстяка")
                            r_coins -= fatboy_price
                            fatboy = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
            elif class_pick == "Э" and elitekill == 1 or class_pick == "э" and elitekill == 1:
                max_health = max_health+10
                health = max_health
                damage = damage+2
                speed = speed+3
                udamage = udamage+2
                reward_game = 2
                print("Вы получите вдвое меньше наградных монет за эту игру")
                user_class = "[31mЭлитный Убийца[0m"
                break
            elif class_pick == "Э" and elitekill == 0 or class_pick == "э" and elitekill == 0:
                an = menu('Меню покупки класса [{elite_price}]', ['Купить','Отменить'], 'red')
                while True:
                    if an == 0:
                        if r_coins < elite_price:
                            print("У вас не достаточно денег")
                            break
                        else:
                            print("Вы успешно купили класс Элитного Убийцы")
                            r_coins -= elite_price
                            elitekill = 1
                            with open('profile.json', 'w', encoding='utf-8') as p:
                                p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(r_coins, hunter, mage, bers, dwarf, golem, goblin, fenix, demon, fatboy, elitekill, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
                                p.write('}]')
                            FileEncrypt('profile.json')
                            break
                    elif an == 1:
                        break
    # Carve out the paths in the maze data structure:
    hasVisited = [(1, 1)] # Start by visiting the top-left corner.
    visit(1, 1)
global r_coins
global key
try:
    with open('profile.json', encoding='utf-8') as p:
        fas = 21
    data = FileDecrypt('profile.json')
    r_coins = data[0]['User'][0]['coins']
    hunter = data[0]['User'][0]['hunter']
    mage = data[0]['User'][0]['mage']
    bers = data[0]['User'][0]['bers']
    dwarf = data[0]['User'][0]['dwarf']
    golem = data[0]['User'][0]['golem']
    goblin = data[0]['User'][0]['goblin']
    fenix = data[0]['User'][0]['fenix']
    demon = data[0]['User'][0]['demon']
    fatboy = data[0]['User'][0]['fatboy']
    elitekill = data[0]['User'][0]['elitekill']
    versy = data[0]['User'][0]['version']
    if versy != version:
        print("version dismatch!")
        print(f"current version: {version}")
        print(f"profile version: {versy}")
except FileNotFoundError:    
    with open('profile.json', 'w', encoding='utf-8') as p:
        print(version)
        p.write('[{"User": [{"coins": %d, "hunter": %d, "mage": %d, "bers": %d, "dwarf": %d, "golem": %d, "goblin": %d, "fenix": %d, "demon": %d, "fatboy": %d, "elitekill": %d, "version": "%s"}]'%(10000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, version)) # добавим кусок в массив ("Меня зовут %s. Мне %d лет." % (name, age))
        p.write('}]')
        hunter = 0
        mage = 0
        bers = 0
        dwarf = 0
        golem = 0
        goblin = 0
        fenix = 0
        demon = 0
        fatboy = 0
        elitekill = 0
        r_coins = 0
    key = Fernet.generate_key()
    try:
        if os.path.getsize("key.key") > 0:
            print("exist")
            with open('key.key','rb') as file:
                key = file.read()
        else:
            with open('key.key','wb') as file:
                file.write(key)
    except Exception:
        with open('key.key','wb') as file:
                file.write(key)
    FileEncrypt('profile.json')
    data = FileDecrypt('profile.json')
    r_coins = data[0]['User'][0]['coins']
    hunter = data[0]['User'][0]['hunter']
    mage = data[0]['User'][0]['mage']
    bers = data[0]['User'][0]['bers']
    dwarf = data[0]['User'][0]['dwarf']
    golem = data[0]['User'][0]['golem']
    goblin = data[0]['User'][0]['goblin']
    fenix = data[0]['User'][0]['fenix']
    demon = data[0]['User'][0]['demon']
    fatboy = data[0]['User'][0]['fatboy']
    elitekill = data[0]['User'][0]['elitekill']
    versy = data[0]['User'][0]['version']
    if versy != version:
        print("version dismatch!")
        print(f"current version: {version}")
        print(f"save version: {versy}")
set_stats()

# Display the final resulting maze data structure:
printMaze(maze)
critty = int(critD*100)
print(f"[36mВаш класс: {user_class}[0m")
print(f"[36mВаш уровень: [33m{level}[0m")
print(f"[36mВаш опыт: [33m{exp}/{exp_cap}[0m")
print(f"[36mВаши очки улучшений: [33m{upgrade}[0m")
print(f"[36mВаше здоровье: [33m{health}/{max_health}[0m")
print(f"[36mВаша регенерация: [33m{Regen}[0m")
print(f"[36mВаша атака: [33m{damage}[0m")
print(f"[36mВаш шанс увернуться: [33m{speed}%[0m")
print(f"[36mВаш шанс оглушения: [33m{StunC}%[0m")
print(f"[36mВаша защита: [33m{defence}")
print(f"[36mВаш шанс усил.защиты: [33m{Abs}%[0m")
print(f"[36mВаше усиление атаки: [33m{udamage}[0m")
print(f"[36mВаш крит.урон: [33m{critty}%[0m")
print(f"[36mВаш крит.шанс: [33m{critC}%[0m")
if Vampirism != 0:
    print(f"[36mВампиризм: [33m{Vampirism}%[0m")
print(" ")
print("Поздравляем, вы прошли уровень! Хотите ли вы продолжить игру с этим же персонажем?(Д/Н)")
a = input("Ответ введите сюда: ")
if a == "Д" or a == "д":
    endless_game = 1
    create_maze()
else:
    print("Спасибо за игру")
time.sleep(100)

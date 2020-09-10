import random

def rnd():
    return random.randint(5, 30)


def  generate_monster():
    monster = {
        "health": rnd(),
        "strength": rnd(),
    }
    print(f"Вы встретили чудовище с {monster.get('health')} жизнями и с силой удара {monster.get('strength')}")
    return monster


def apple():
    hp = rnd()
    print(f"Вы нашли яблоко увелчивающее здоровье на {hp}")
    knight['health'] = knight['health'] + hp
    status_knight(knight)
    return hp


def sword():
    sword = rnd()
    print(f"Вы нашли меч с cилой атаки {sword}")
    return sword


def pick_sword(strength):
    knight['strength'] = strength
    return status_knight(knight)


def status_knight(knight: dict):
    if knight['health'] <= 0:
        print('Вы мертвы')
        return 1
    else:
        print(f"Моя жизнь: {knight['health']}\nМоя сила: {knight['strength']}\n")
        return 0


def status_mob(monster: dict):
    if monster.get('health') <= 0:
        print('Монстер убит\n')
        return 0
    else:
        print(f"У чудовища осталось:\n Жизни: {monster['health']}\n Сила: {monster['strength']}\n")


def fight(knight: dict, monster: dict):
    monster['health'] =  monster.get('health') - knight.get('strength')
    knight['health'] = knight.get('health') - monster.get('strength')
    if knight['health'] <= 0:
        status_mob(monster)
        return status_knight(knight)
    elif monster['health'] <= 0:
        status_knight(knight)
        return status_mob(monster)
    else:
        return fight(knight,monster)


knight = {
   "health": 10,
   "strength": 10,
}

def check_key(key):
    if key == "1" or key == "2":
        return key
    else:
        key = input("Введите 1 или 2: ")
        return check_key(key)


def check_value(value):
    if value == apple:
        value()
        pass
    elif value == sword:
        strength_sw = value()
        pick = input("Введите 1-взять меч, 2-пойти дальше?: ")
        key = check_key(pick)
        if key == '1':
            pick_sword(strength_sw)
        else:
            return key
    elif value == generate_monster:
        mob = value()
        action = input("Введите 1-атаковать чудовище, 2-убежать?: ")
        key = check_key(action)
        if key == '1':
            return fight(knight, mob)
        else:
            return key


list = [generate_monster,apple,sword]
index = 0
while index < 10:
    rnd_gen = random.choice(list)
    enter = check_value(rnd_gen)
    if enter == "2":
        continue
    elif enter == 1:
        print("Игра окончена")
        break
    elif enter == 0:
        index += 1
        print(f"Число побед: {index}\n")
        continue
    else:
        continue
else:
    print("Вы победили!\nИгра закончена!")

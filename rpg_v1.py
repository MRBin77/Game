""" Игра герой и чудовище

Name
    rpg_v1
Description
    Игра герой и чудовище. Пошаговая игра, ввод осуществляется с помощью 1 либо 2
    Игра написана в качестве выполнения домашнего задания
Contents
    Packages
        random
    Variables
        knight (dict): Переменная хранит характеристики рыцаря (strength, health)
    Functions
        rnd()
        generate_monster()
        apple()
        sword()
        pick_sword(strength: int)
        status_knight(knight:dict)
        status_monster(monster:dict)
        fight(knight: dict, monster:dict)
        check_key(key: str)
        check_func_address(func_address)

"""

import random


knight = {
    'health': 10,
    'strength': 10,
}


def rnd():
    """
    Функция генерирования случайных значений
    Returns:
        int: Возвращает случаное значение в диапазоне от 5 до 30
    """
    return random.randint(5, 30)


def  generate_monster():
    """
    Функция генерирует монстров и выводит их значение

    Returns:
        dict: Возвращает словарь с монстром, с случаныйми значениями в health и strength
    Examples:

    """
    monster = {
        'health': rnd(),
        'strength': rnd(),
    }
    print(f"Вы встретили чудовище с {monster.get('health')} жизнями и с силой удара {monster.get('strength')}")
    return monster


def apple():
    """
    Функция генерирует яблоко, увеличивающее здоровье (health) рыцарю
    Returns:
         int: Возвращает значение увеличенного здоровье (health) рыцаря
    Examples:
        >>> apple()
        Вы нашли яблоко увеличивающее здоровье на 5
        Моя жизнь: 15
        Моя сила: 10
    """
    hp = rnd()
    print(f"Вы нашли яблоко увеличивающее здоровье на {hp}")
    knight['health'] = knight['health'] + hp
    status_knight(knight)
    return hp


def sword():
    """
    Функция генерирует меч с случайным значением
    Return:
         int: Возвращает случайное значение
    Examples:
        >>> sword()
        Вы нашли меч с cилой атаки 23
        23
    """
    sword = rnd()
    print(f"Вы нашли меч с cилой атаки {sword}")
    return sword


def pick_sword(strength: int):
    """
    Функция взятия меча. При взятии заменят strength рыцаря, на новое значение
    Parameters:
        strength (int): Принимается новое значение силы(strength) меча
    Return:
        none: Возвращает статус рыцаря из ф-ции status_knight()
    Examples:
        >>> pick_sword(sword())
        Вы нашли меч с cилой атаки 27
        Моя жизнь: 10
        Моя сила: 27
    """
    knight['strength'] = strength
    return status_knight(knight)


def status_knight(knight: dict):
    """
    Функция выводит статус рыцаря. Если рыцарь жив то выводит health и strength рыцаря,
    если рыцарь мертв то выведет сообщение о смерте
    Parameter:
         knight (dict): Принимает на вход словарь из ключей strength и health  рыцаря.
    Returns:
         return 1 (int): Возвращает 1 если рыцарь мёртв
         return 0 (int): Возвращает 0 если рыцарь жив
    Examples:
        Если рыцарь жив то:

            >>> status_knight(knight)
                Моя жизнь: 10
                Моя сила: 10

                0

        Ecли рыцарь мертв то:
            >>> status_knight(knight)
                Вы мертвы

                1
    """
    if knight['health'] <= 0:
        print('Вы мертвы\n')
        return 1

    else:
        print(f"Моя жизнь: {knight['health']}\nМоя сила: {knight['strength']}\n")
        return 0


def status_mob(monster: dict):
    """
    Функция выводит статус монстра(чудовища). Если монстр жив то выводит health и strength монстра,
    если монстр мертв то выведет сообщение о смерте
    Parameter:
        monster (dict):  Принимает на вход словарь из ключей strength и health  монстра.
    Return:
         return 0 (int): Возвращает 0 если монстр мёртв
    Examples:
        Если монстр жив то:
            >>> status_monster(generate_monster())
                У чудовища осталось:
                Жизни: 5
                Силa: 10
    """
    if monster.get('health') <= 0:
        print('Монстер убит\n')
        return 0
    else:
        print(f"У чудовища осталось:\n Жизни: {monster['health']}\n Сила: {monster['strength']}\n")


def fight(knight: dict, monster: dict):
    """
    Функция реализует бой между рыцарем и монстром. Сначала атакует рыцарь и отнимае health у монстра,
    потом монстр атакует в ответ и отнимает health у рыцаря, после идёт проверка условий,
    если ни одно условие не выполняется происходит рекурсия
    Parameters:
        knight (dict): Принимает на вход словарь с характеристиками(health, strength) рыцаря
        monster (dict): Принимает на вход словарь с характеристиками(health, strength) монстра
    Returns:
        return status_knight(knight) (int): Возвращает 1 если рыцарь метртв
        return status_mob(monster) (int): Возвращает 0 если монстр мертв
        return fight(knight,monster) (dict): Возвращает рекурсивное значение, если одно из  условий выше не выполнены
    """
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


def check_key(key: str):
    """
    Функция проверяет правильность ввода играком. Если  введено не 1 или 2,
    то  выводит приглашение ввести 1 или 2
    Parameter:
        key (str): Принимает на вход cтроку, введеную игроком
    Returns:
        return key (str): Возвращает значение key, если условие выполнено
        return check_key(key) (str): Возвращает значение рекурсии
    """
    if key in ['1','2']:
        return key
    else:
        key = input("Введите 1 или 2: ")
        return check_key(key)


def check_func_address(func_address):
    """
    Функция, проверят адрес функции с адресами ф-ций apple, sword, generate_monster.
    Если адрес ф-ции совпадает с apple, sword или  generate_monster, то функция в func_address вызывается.
    Parameter:
        func_address (function): Принимает на вход функцию
    Returns:
        return key (str): Возвращает значение введенное игроком
        return fight(knight,monster) (int): Возвращает значение функции fight,  0 или 1
    """
    if func_address == apple:
        func_address()
    elif func_address == sword:
        strength_sw = func_address()
        pick = input('Введите 1-взять меч, 2-пойти дальше?: ')
        key = check_key(pick)
        if key == '1':
            pick_sword(strength_sw)
        else:
            return key
    elif func_address == generate_monster:
        monster = func_address()
        action = input('Введите 1-атаковать чудовище, 2-убежать?: ')
        key = check_key(action)
        if key == '1':
            return fight(knight, monster)
        else:
            return key


if __name__=='__main__':
    box = [generate_monster, apple, sword]
    index = 0

    while index < 10:

        rnd_gen = random.choice(box)
        enter = check_func_address(rnd_gen)
        if enter == '2':
            continue

        if enter == 1:
            print('Игра окончена')
            break

        if enter == 0:
            index += 1
            print(f"Число побед: {index}\n")
            continue

    else:
        print('Вы победили!\nИгра закончена!')

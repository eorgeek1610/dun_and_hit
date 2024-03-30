import random
from colorama import Fore, Style
import time


def get_random_item(inventory, player):
    items_with_weights_and_damage = [
        ('Поломанный меч', 90, 0.5),
        (f'{Fore.GREEN}Ржавый меч{Style.RESET_ALL}', 5, 0),
        (f'{Fore.BLUE}Меч война{Style.RESET_ALL}', 2, 0),
        (f'{Fore.BLUE}Меч героя{Style.RESET_ALL}', 2, 0),
        (f'{Fore.RED}АСТРО-МЕЧ{Style.RESET_ALL}', 0.5, 0)
    ]
    items, weights, damages = zip(*items_with_weights_and_damage)
    total_weight = sum(weights)
    weights = [w / total_weight for w in weights]

    if len(inventory) < player.backpack:
        chosen_index = random.choices(range(len(items)), weights)[0]
        item = items[chosen_index]
        damage_add = damages[chosen_index]
        player.sword_damage_add += damage_add
        inventory.append(item)
        print(f"\nВы получили: {item}")
        print(f"Его можно надеть в инветаре!")
    else:
        print("\nВаш инвентарь полон!")
    return inventory


def get_random_item_rar(inventory, player):
    items_with_weights_and_damage = [
        (f'{Fore.BLUE}Меч Тото{Style.RESET_ALL}', 40, 0),
        (f'{Fore.MAGENTA}Меч Лолога{Style.RESET_ALL}', 5, 0),
        (f'{Fore.MAGENTA}Меч Грека{Style.RESET_ALL}', 5, 0),
        (f'{Fore.MAGENTA}Меч Тутта{Style.RESET_ALL}', 10, 0),
        (f'{Fore.YELLOW}ТОМЛИБ-МЕЧ{Style.RESET_ALL}', 0.5, 0)
    ]
    items, weights, damages = zip(*items_with_weights_and_damage)
    total_weight = sum(weights)
    weights = [w / total_weight for w in weights]

    if len(inventory) < player.backpack:
        chosen_index = random.choices(range(len(items)), weights)[0]
        item = items[chosen_index]
        damage_add = damages[chosen_index]
        player.sword_damage_add += damage_add
        inventory.append(item)
        print(f"\nВы получили: {item}")
        print(f"Его можно надеть в инветаре!")
    else:
        print("\nВаш инвентарь полон!")
    return inventory


def manage_inventory(inventory, player):
    qqqw = True
    qqqww = True
    # Словарь для хранения урона каждого меча
    item_stats = {
        'Поломанный меч': (0.5, 0),
        f'{Fore.GREEN}Ржавый меч{Style.RESET_ALL}': (1, 0),
        f'{Fore.BLUE}Меч война{Style.RESET_ALL}': (1.5, 0),
        f'{Fore.BLUE}Меч героя{Style.RESET_ALL}': (1, 1),
        f'{Fore.BLUE}Меч Тото{Style.RESET_ALL}': (0, 4),
        f'{Fore.MAGENTA}Меч Лолога{Style.RESET_ALL}': (1.5, 1),
        f'{Fore.MAGENTA}Меч Грека{Style.RESET_ALL}': (0.5, 2),
        f'{Fore.MAGENTA}Меч Тутта{Style.RESET_ALL}': (2, 0),
        f'{Fore.RED}АСТРО-МЕЧ{Style.RESET_ALL}': (3, 5),
        f'{Fore.YELLOW}ТОМЛИБ-МЕЧ{Style.RESET_ALL}': (2, 6)
    }

    while True:

        print("\nВаш инвентарь:")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item}")

        print("\nВыберите действие:")
        print("1. Экипировать меч")
        print("2. Удалить предмет")
        print("3. Переплавить предмет")
        print("4. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            item_number = int(input(f"Введите номер меча для экипировки (1-{player.backpack}): "))
            if 1 <= item_number <= len(inventory):
                selected_item = inventory[item_number - 1]
                if selected_item in item_stats:
                    if selected_item == f'{Fore.MAGENTA}Меч Лолога{Style.RESET_ALL}' and qqqw:
                        player.boost_money += 5
                        qqqw = False
                    elif selected_item == f'{Fore.MAGENTA}Меч Тутта{Style.RESET_ALL}' and qqqww:
                        player.backpack += 2
                        qqqww = False
                    player.sword_damage_add = item_stats[selected_item][0]
                    player.sword_health_add += item_stats[selected_item][1]
                    player.equip_weapon(selected_item, item_stats[selected_item][0])
                else:
                    print("Это не меч!")
            else:
                print("\nНеверный номер предмета!")
        elif choice == '2':
            item_number = int(input(f"Введите номер предмета для удаления (1-{player.backpack}): "))
            if 1 <= item_number <= len(inventory):
                removed_item = inventory.pop(item_number - 1)
                if player.current_weapon == removed_item:
                    player.unequip_weapon()
                print(f"Предмет {removed_item} удален из инвентаря.")
            else:
                print("\nНеверный номер предмета!")
        elif choice == '3':
            item_number = int(input(f"Введите номер предмета для переплавки (1-{player.backpack}): "))
            if 1 <= item_number <= len(inventory):
                if random.randint(1, 100) <= 50:
                    removed_item = inventory.pop(item_number - 1)
                    if player.current_weapon == removed_item:
                        player.unequip_weapon()
                    print(f"\nПредмет успешно переплавлен.")
                    if random.randint(1, 100) <= 5:
                        get_random_item_rar(inventory, player)
                    else:
                        get_random_item(inventory, player)
                else:
                    removed_item = inventory.pop(item_number - 1)
                    if player.current_weapon == removed_item:
                        player.unequip_weapon()
                    print("\nПереплавка не удалась.")
            else:
                print("\nНеверный номер предмета!")
        elif choice == '4':
            print("\nПереходим...")
            time.sleep(0.5)
            break
        else:
            print("Неверный ввод, попробуйте снова.")

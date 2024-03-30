import random
from colorama import Fore, Style

class Item:
    def __init__(self, name, damage, health_bonus=0, special_function=None):
        self.name = name
        self.damage = damage
        self.health_bonus = health_bonus
        self.special_function = special_function

    def apply_buffs(self, player):
        player.sword_damage_add = self.damage
        player.dop_health += self.health_bonus
        if self.special_function:
            self.special_function(player)

    def remove_buffs(self, player):
        if player.sword_damage_add == self.damage:
            player.sword_damage_add = 0
        player.dop_health -= self.health_bonus

def get_random_item(inventory, player):
    items_with_weights = [
        (Item('Поломанный меч', 0.5, health_bonus=2), 90),
        (Item(f'{Fore.GREEN}Ржавый меч{Style.RESET_ALL}', 1, health_bonus=2), 5),
        (Item(f'{Fore.BLUE}Меч война{Style.RESET_ALL}', 1.5, special_function=war_sword_function), 2.5),
        (Item(f'{Fore.BLUE}Меч героя{Style.RESET_ALL}', 1, health_bonus=1), 2.5)
    ]
    items, weights = zip(*items_with_weights)
    total_weight = sum(weights)
    weights = [w / total_weight for w in weights]

    if len(inventory) < player.backpack:
        chosen_index = random.choices(range(len(items)), weights)[0]
        item = items[chosen_index]
        player.sword_damage_add += item.damage
        inventory.append(item)
        print(f"\nВы получили: {item.name}")
        print(f"Его можно надеть в инветаре!")
    else:
        print("\nВаш инвентарь полон!")
    return inventory

def war_sword_function(player):
    # Определите здесь любые специальные эффекты для Меча Война
    pass

def manage_inventory(inventory, player):
    while True:
        print("\nВаш инвентарь:")
        for index, item in enumerate(inventory, start=1):
            print(f"{index}. {item.name}")

        print("\nВыберите действие:")
        print("1. Экипировать меч")
        print("2. Удалить предмет")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            item_number = int(input("Введите номер меча для экипировки (1-5): "))
            if 1 <= item_number <= len(inventory):
                selected_item = inventory[item_number - 1]
                if player.current_weapon:
                    player.current_weapon.remove_buffs(player)
                selected_item.apply_buffs(player)
                player.current_weapon = selected_item
                print(f"Вы экипировали {selected_item.name}")
            else:
                print("\nНеверный номер предмета!")
        elif choice == '2':
            item_number = int(input("Введите номер предмета для удаления (1-5): "))
            if 1 <= item_number <= len(inventory):
                removed_item = inventory.pop(item_number - 1)
                if player.current_weapon == removed_item:
                    player.current_weapon.remove_buffs(player)
                    player.current_weapon = None
                print(f"Предмет {removed_item.name} удален из инвентаря.")
            else:
                print("\nНеверный номер предмета!")
        elif choice == '3':
            break
        else:
            print("Неверный ввод, попробуйте снова.")
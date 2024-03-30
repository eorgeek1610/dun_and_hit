import time

from colorama import Fore, Style
import random

from dun_and_hit.my_libs.cases import manage_inventory
from dun_and_hit.my_libs.cases import get_random_item
from dun_and_hit.my_libs.show_info import show_info
from dun_and_hit.my_libs.start_game import start_game
from dun_and_hit.my_libs.cases import get_random_item_rar
from dun_and_hit.my_libs.spravka import spravka

inventory = []


class Player:
    def __init__(self, health, damage, money, dop_health, miss_chacnce):
        self.health = health
        self.damage = damage
        self.money = money
        self.extra_health_given = False
        self.initial_health = health
        self.magaz_health = dop_health
        self.extra_health_given_two = True
        self.miss_chacnce = miss_chacnce
        self.backpack = 2
        self.current_weapon = None
        self.boost_money = 10
        self.sword_damage_add = 0
        self.dop_damage = 0
        self.fix = health
        self.initial_damage = damage
        self.sword_health_add = 0

    def extra_health(self):
        if self.health < 4 and not self.extra_health_given:
            self.health += 10
            self.extra_health_given = True
            print(f"{Fore.GREEN}Игрок получил доп. здоровье!{Style.RESET_ALL}")

        elif self.health < 4 and not self.extra_health_given_two:
            self.health += 14
            self.extra_health_given_two = True
            print(f"{Fore.GREEN}Игрок получил буст доп. здоровья!!{Style.RESET_ALL}")

    def attack(self, enemy):
        print("\nВыберите место для атаки:")
        print("1. Голова")
        print("2. Тело")
        print("3. Ноги")
        print("4. Захилить")
        choice = input("Выберите: ")

        if choice == "1":  # Голова
            if random.random() < self.miss_chacnce + 0.3:  # 50% шанс промаха
                print("\nВы промахнулись!")
            else:
                enemy.health -= self.damage * 2.5  # Урон в голову удваивается
                print(
                    f"\n{Fore.GREEN}Вы нанесли двойной с половиной урон в голову с уроном {player.damage * 2.5}! Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
        elif choice == "2":  # Тело
            if random.random() < self.miss_chacnce + 0.1:  # 30% шанс промаха
                print("\nВы промахнулись!")
            else:
                enemy.health -= self.damage
                print(
                    f"\n{Fore.GREEN}Вы атакуете в тело с уроном {player.damage}! Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
        elif choice == "3":  # Ноги
            if random.random() < self.miss_chacnce + 0.2:  # 40% шанс промаха
                print("\nВы промахнулись!")
            else:
                enemy.health -= self.damage * 2  # Урон в ноги увеличен
                print(
                    f"\n{Fore.GREEN}Вы нанесли урон в ноги с уроном {player.damage * 1.5}! Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
        elif choice == "4":  # Хил
            if player.health < player.initial_health:
                if random.random() < self.miss_chacnce + 0.2:  # 40% шанс промаха
                    print(f"\nВам не повезло! Ваше здоровье: {player.health}")
                else:
                    player.health += 4
                    print(f"\nВам повезло больше, вы захилили 4 здоровья! Ваше здоровье: {player.health}")
            else:
                print("У вас максимальное количество здровья!")
        else:
            print("\nНекорректный выбор.")

    def reset_health(self):
        self.health = self.initial_health + self.magaz_health  # Восстанавливаем здоровье до изначального значения

    def sword_damage_add_def(self):
        self.damage += self.sword_damage_add

    def equip_weapon(self, weapon, sword_damage_add):
        if self.current_weapon:
            self.unequip_weapon()  # Снимаем текущее оружие, если оно есть
        self.current_weapon = weapon
        self.damage += self.sword_damage_add
        self.initial_health += self.sword_health_add
        print(f"\nВаш меч: {weapon}.")

    def unequip_weapon(self):
        print(f"Вы сняли {self.current_weapon}.")
        self.current_weapon = None
        self.damage = self.initial_damage
        self.initial_health -= self.sword_health_add
        self.sword_health_add = 0


class Enemy:
    def __init__(self, health, damage, dop_damage, dop_health, miss_chacnce):
        self.health = health
        self.damage = damage
        self.initial_health = health  # Сохраняем изначальное здоровье
        self.initial_damage = damage  # Сохраняем изначальный урон
        self.magaz_damage = dop_damage
        self.magaz_health = dop_health
        self.vampirizm = False
        self.miss_chacnce = miss_chacnce

    def attack(self, player):
        choice = random.random()
        if choice < 0.6:  # Дефолт
            if random.random() < self.miss_chacnce + 0.2:  # 40% шанс промаха
                player.health -= self.damage * 1.5  # Урон в голову удваивается
                print(
                    f"{Fore.RED}Враг нанес больший урон {enemy.damage + 0.5}! Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
            else:
                player.health -= self.damage
                print(
                    f"{Fore.RED}Враг нанес урон {enemy.damage}! Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
        elif choice > 0.4:  # Хил
            if random.random() < self.miss_chacnce + 0.3:  # 20% шанс промаха
                enemy.health += 1
                print(
                    f"{Fore.RED}Врагу не повезло, и он захилил 1 здоровье. Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
            else:
                enemy.health += 2
                print(
                    f"{Fore.RED}Врагу повезло, он захилил 2 здоровья! Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
        else:
            print("\nНекорректный выбор.")
        if self.damage < 10:
            self.damage += 0.5
            self.health -= 0.5
        else:
            self.damage += 1.5
            self.health -= 1
        print(
            f"{Fore.RED}У врага сработал эффект 'Возмещение', Урон врага: {self.damage}, Здоровье врага: {enemy.health}{Style.RESET_ALL}")
        if random.random() < 0.6 and self.vampirizm:
            player.health -= self.damage
            enemy.health += self.damage
            print(
                f"{Fore.RED}У врага сработал эффект 'Вампиризм'! Он забрал у вас дополнительно {enemy.damage} и захил столько же. Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
        elif random.random() < 0.5 and not self.vampirizm and enemy.health < 5:
            enemy.health += 2
            enemy.damage -= 0.5
            print(
                f"{Fore.RED}У врага стало больше здоровья на 2, но у меньшился урон на 0.5. Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}, Урон врага: {enemy.damage}{Style.RESET_ALL}")

    def reset_health(self):
        self.health = self.initial_health + self.magaz_health  # Восстанавливаем здоровье до изначального значения

    def reset_damage(self):
        self.damage = self.initial_damage + self.magaz_damage  # Восстанавливаем урон до изначального значения


player = Player(20, 2, 0, 0, 0.2)
enemy = Enemy(30, 1, 0, 0, 0.1)


def magazin(player, enemy):
    while True:
        print("\n1. Улучшения и способности")
        print("2. Кейсы и мечи")
        print("3. Выйти")
        choice = input("Выберите: ")
        if choice == "1":
            print("\n1. Улучшение статистики.")
            print("2. Дополнительные улучшения")

            choice = input("Выберите: ")

            if choice == "1":
                print("\n1. + 1 здоровье (50 монет)")
                print("2. + 1 урон (60 монет)")
                print("3. + 1.5 урона, 1 здоровье (70 монет)")

                choice = input("Выберите: ")

                if choice == "1":
                    if player.money >= 50:
                        player.magaz_health += 1
                        player.money -= 50
                        enemy.magaz_health += 3
                        enemy.magaz_damage += 0.5
                        print(f"\nВаши монеты: {player.money}")
                    else:
                        print(f"У вас недостаточно монет. Ваши монеты: {player.money}")
                elif choice == "2":
                    if player.money >= 60:
                        player.dop_damage += 1
                        player.money -= 60
                        enemy.magaz_health += 4
                        print(f"\nВаши монеты: {player.money}")
                    else:
                        print(f"У вас недостаточно монет. Ваши монеты: {player.money}")
                elif choice == "3":
                    if player.money >= 70:
                        player.dop_damage += 1.5
                        player.magaz_health += 1
                        player.money -= 70
                        enemy.magaz_health += 6
                        print(f"\nВаши монеты: {player.money}")
                    else:
                        print(f"У вас недостаточно монет. Ваши монеты: {player.money}")
                else:
                    print("\nНапиши цифру...")

            elif choice == "2":

                if player.backpack == 2:
                    print("\n1. Увеличение на вместимость инвентаря (+2 вместимости) (10 монет)")
                elif player.backpack == 4:
                    print("\n1. Увеличение на вместимость инвентаря (+2 вместимости) (20 монет)")
                else:
                    print("\n1. Улучшение на вместимость инвентаря (+1 вместимости) (30 монет)")
                print("2. Активирование способности восстоновления здоровья <= 4 здоровья (15 монет)")

                choice = input("Выберите: ")

                if choice == "1":
                    if player.backpack == 2:
                        if player.money >= 10:
                            player.money -= 10
                            player.backpack += 2
                            print(f"\nВаши монеты: {player.money}")
                        else:
                            print(f"\nУ вас недостаточно монет. Ваши монеты: {player.money}")

                    elif player.backpack == 4:
                        if player.money >= 20:
                            player.money -= 20
                            player.backpack += 2
                            print(f"\nВаши монеты: {player.money}")
                        else:
                            print(f"\nУ вас недостаточно монет. Ваши монеты: {player.money}")
                    else:
                        if player.money >= 30:
                            player.money -= 30
                            player.backpack += 1
                            print(f"\nВаши монеты: {player.money}")
                        else:
                            print(f"\nУ вас недостаточно монет. Ваши монеты: {player.money}")

                elif choice == "2":
                    if player.money >= 15:
                        player.money -= 15
                        player.extra_health_given = True
                        print(f"\nВаши монеты: {player.money}")
                    else:
                        print(f"\nУ вас недостаточно монет. Ваши монеты: {player.money}")


            else:
                print("\nНет...")

        elif choice == "2":
            print("1. Начальный кейс.")
            print("2. Продвинутый кейс")

            choice = input("Выберите: ")

            if choice == "1":
                print(f"Начальный кейс (10 монет)")
                print(f"1. Поломанный меч (80% шансов)")
                print(f"2. {Fore.GREEN}Ржавый меч (10% шансов){Style.RESET_ALL}")
                print(f"3. {Fore.BLUE}Меч война (5% шансов){Style.RESET_ALL}")
                print(f"4. {Fore.BLUE}Меч героя (5% шансов){Style.RESET_ALL}")
                print(f"5. {Fore.RED}АСТРО-МЕЧ (ОЧЕНЬ РЕДКИЙ){Style.RESET_ALL}")

                choice = input("Купить (1. Да, 2. Нет)? ").lower()

                if choice == "1":
                    if player.money >= 10:
                        get_random_item(inventory, player)
                        player.money -= 10
                    else:
                        print("\nДеняк нету :(")
                        magazin(player, enemy)
                elif choice == "2":
                    print("\nПереходим...")
                    time.sleep(0.5)
                    magazin(player, enemy)
                elif choice == "3":
                    if player.money >= 50:
                        get_random_item(inventory, player)
                        get_random_item(inventory, player)
                        get_random_item(inventory, player)
                        get_random_item(inventory, player)
                        get_random_item(inventory, player)
                        player.money -= 50
                    else:
                        print("\nДеняк нету :(")
                        magazin(player, enemy)
                else:
                    print("\nВерну тебя в магазин, так уж и быть.")
                    time.sleep(0.5)
                    magazin(player, enemy)

            elif choice == "2":
                print(f"Продвинутый кейс (20 монет)")
                print(f"1. {Fore.BLUE}Меч Тото (70%){Style.RESET_ALL}")
                print(f"2. {Fore.MAGENTA}Меч Лолога (10% шансов){Style.RESET_ALL}")
                print(f"3. {Fore.MAGENTA}Меч Грека (10% шансов){Style.RESET_ALL}")
                print(f"4. {Fore.MAGENTA}Меч Тутта (10% шансов){Style.RESET_ALL}")
                print(f"5. {Fore.YELLOW}ТОМЛИБ-МЕЧ (ОЧЕНЬ РЕДКИЙ){Style.RESET_ALL}")
                choice = input("Купить (1. Да, 2. Нет)? ").lower()

                if choice == "1":
                    if player.money >= 20:
                        get_random_item_rar(inventory, player)
                        player.money -= 20
                    else:
                        print("\nДеняк нету :(")
                        magazin(player, enemy)
                elif choice == "2":
                    print("\nПереходим...")
                    time.sleep(0.5)
                    magazin(player, enemy)
                elif choice == "3":
                    if player.money >= 250:
                        get_random_item_rar(inventory, player)
                        get_random_item_rar(inventory, player)
                        get_random_item_rar(inventory, player)
                        get_random_item_rar(inventory, player)
                        get_random_item_rar(inventory, player)
                        player.money -= 100
                    else:
                        print("\nДеняк нету :(")
                        magazin(player, enemy)
                else:
                    print("\nВерну тебя в магазин, так уж и быть.")
                    time.sleep(0.5)
                    magazin(player, enemy)

        else:
            print("\nПереходим...")
            time.sleep(0.5)
            menu_start(player, enemy)


def menu_start(player, enemy):
    while True:
        print("\nМеню:")
        print("1. Информация о героях")
        print("2. Начать игру")
        print("3. Магазин")
        print("4. Справочник")
        print("5. Инвентарь")

        choice = input("Выберите: ")

        if choice == "1":
            show_info(player, enemy)
        elif choice == "2":
            start_game(player, enemy)
        elif choice == '3':
            magazin(player, enemy)
        elif choice == '4':
            spravka(player, enemy)
        elif choice == '5':
            manage_inventory(inventory, player)
        else:
            print("\nПовторите еще раз.")


menu_start(player, enemy)

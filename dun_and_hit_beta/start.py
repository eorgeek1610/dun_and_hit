import time

from colorama import Fore, Style
import random

from dun_and_hit_beta.my_libs.cases import manage_inventory
from dun_and_hit_beta.my_libs.cases import get_random_item
from dun_and_hit_beta.my_libs.show_info import show_info
from dun_and_hit_beta.my_libs.start_game import start_game
from dun_and_hit_beta.my_libs.spravka import spravka

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
        self.sword_damage_add = 0
        self.initial_damage = damage
        self.sword_health = 0

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
        print('4. Захилить')
        choice = input("Выберите: ")

        if choice == "1":  # Голова
            if random.random() < self.miss_chacnce + 0.3:
                print("\nВы промахнулись!")
            else:
                enemy.health -= self.damage * 2.5
                print(
                    f"\n{Fore.GREEN}Вы нанесли двойной с половиной урон в голову с уроном {player.damage * 2.5}! Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
        elif choice == "2":  # Тело
            if random.random() < self.miss_chacnce + 0.1:
                print("\nВы промахнулись!")
            else:
                enemy.health -= self.damage
                print(
                    f"\n{Fore.GREEN}Вы атакуете в тело с уроном {player.damage}! Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
        elif choice == "3":  # Ноги
            if random.random() < self.miss_chacnce + 0.2:
                print("\nВы промахнулись!")
            else:
                enemy.health -= self.damage * 2
                print(
                    f"\n{Fore.GREEN}Вы нанесли урон в ноги с уроном {player.damage * 1.5}! Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
        elif choice == "4":  # Хил
            if player.health < player.initial_health:
                if random.random() < self.miss_chacnce + 0.2:
                    print(f"\nВам не повезло! Ваше здоровье: {player.health}")
                else:
                    player.health += 4
                    print(f"\nВам повезло больше, вы захилили 4 здоровья! Ваше здоровье: {player.health}")
            else:
                print("У вас максимальное количество здровья!")
        else:
            print('\nНекорректный выбор.')

    def reset_health(self):
        self.health = self.initial_health + self.magaz_health + self.sword_health

    def sword_damage_add_def(self):
        self.damage += self.sword_damage_add

    def equip_weapon(self, weapon):
        if self.current_weapon:
            self.unequip_weapon()
        self.current_weapon = weapon
        self.damage += self.sword_damage_add
        print(f"Ваш меч: {weapon}.")

    def unequip_weapon(self):
        print(f"Вы сняли {self.current_weapon}.")
        self.current_weapon = None
        self.damage = self.initial_damage

    @property
    def damage_look(self):
        return self.damage + self.sword_damage_add


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
                    f"Врагу не повезло, и он захилил 1 здоровье. Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}{Style.RESET_ALL}")
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
                f"У врага сработал эффект 'Вампиризм'! Он забрал у вас дополнительно {enemy.damage} и захил столько же. Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}")
        elif random.random() < 0.5 and not self.vampirizm and enemy.health < 5:
            enemy.health += 2
            enemy.damage -= 0.5
            print(
                f"У врага стало больше здоровья на 2, но у меньшился урон на 0.5. Ваше здоровье: {player.health}, Здоровье Врага: {enemy.health}, Урон врага: {enemy.damage}")

    def reset_health(self):
        self.health = self.initial_health + self.magaz_health  # Восстанавливаем здоровье до изначального значения

    def reset_damage(self):
        self.damage = self.initial_damage + self.magaz_damage  # Восстанавливаем урон до изначального значения


player = Player(10, 2, 700, 0, 0.2)
enemy = Enemy(15, 0.5, 0, 0, 0.1)


def magazin(player, enemy):
    while True:
        print("\n1. Улучшения и способности")
        print("2. Кейсы и мечи")
        print("3. Выйти")
        choice = input("Выберите: ")
        if choice == "1":
            print("\n1. Улучшение урона + 1, и хп + 2 (30 монет)")
            print("2. Восстоновление способности доп. здоровья (15 монет)")
            print("3. Улучшение здоровья + 3,+ 1 урон (70 монет)")
            print("4. Улучшение здровья и урона на +2 (80 монет)")
            print("5. Улучшение восстоновления способности доп. здоровья (+5 доп. здоровья) (100 монет)")
            print("6. У меньшение шанса на промах (30 монет)")
            if player.backpack == 2:
                print("7. Увеличение на вместимость инвентаря (+2 вместимости) (10 монет)")
            elif player.backpack == 4:
                print("7. Увеличение на вместимость инвентаря (+2 вместимости) (20 монет)")
            else:
                print("7. Улучшение на вместимость инвентаря (+1 вместимости) (30 монет)")
            print("8. Выйти")

            choice = input("Выберите: ")

            if choice == "1":
                if player.money >= 30:
                    player.damage += 1
                    player.magaz_health += 2
                    player.money -= 30
                    enemy.magaz_damage += 0.5
                    enemy.magaz_health += 1
                    print(f"Успешная покупка, ваши монеты: {player.money}")
                else:
                    print(f"Не достаточно монет, ваши монеты: {player.money}")
            elif choice == "2":
                if player.money >= 15:
                    player.extra_health_given = False
                    player.extra_health_given_two = True
                    enemy.magaz_health += 2
                    player.money -= 15
                    player.damage += 1
                    print(f"Успешная покупка, ваши монеты: {player.money}")
                else:
                    print(f"Не достаточно монет, ваши монеты: {player.money}")
            elif choice == "3":
                if player.money >= 70:
                    player.health += 3
                    player.money -= 70
                    enemy.magaz_health += 2
                    print(f"Успешная покупка, ваши монеты: {player.money}")
                else:
                    print(f"Не достаточно монет, ваши монеты: {player.money}")
            elif choice == '4':
                if player.money >= 80:
                    player.magaz_health += 2
                    player.damage += 2
                    enemy.magaz_health += 2
                    enemy.magaz_damage += 0.5
                    enemy.vampirizm = True
                    player.money -= 80
                    print(f"Успешная покупка, ваши монеты: {player.money}")
                else:
                    print(f"Не достаточно монет, ваши монеты: {player.money}")
            elif choice == '5':
                if player.money >= 100:
                    player.money -= 100
                    player.extra_health_given_two = False
                    enemy.damage += 0.5
                    player.extra_health_given = True
                    print(f"Успешная покупка, ваши монеты: {player.money}")
                else:
                    print(f"Не достаточно монет, ваши монеты: {player.money}")
            elif choice == "6":
                if player.money >= 30:
                    if player.miss_chacnce < 0.2:
                        player.money -= 30
                        print(f"За скам, отберу у тебя монеты! {player.money}")
                    else:
                        player.miss_chacnce = 0.1
                        player.money -= 30
                        print(f"Успешная покупка, ваши монеты: {player.money}")
                else:
                    print(f"Не достаточно монет, ваши монеты: {player.money}")
            elif choice == "7":
                if player.backpack == 2:
                    if player.money >= 10:
                        player.backpack += 2
                        player.money -= 10
                        print(f"\nУспешная покупка, ваши монеты: {player.money}")
                elif player.backpack == 4:
                    player.backpack += 2
                    player.money -= 20
                    print(f"\nУспешная покупка, ваши монеты: {player.money}")
                else:
                    player.backpack += 1
                    player.money -= 30
                    print(f"\nУспешная покупка, ваши монеты: {player.money}")
            elif choice == "8":
                print("\nПереходим...")
                magazin(player, enemy)
            else:
                print("Повторите еще раз.")
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
        else:
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

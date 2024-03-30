def show_info(player, enemy):
    player.reset_health()
    enemy.reset_health()
    enemy.reset_damage()
    print("\nИнформация о вас:")
    print(f"Здоровье: {player.health}")
    print(f"Монет: {player.money}")
    print(f"Урон: {player.damage}")
    print(f"Размер инвентаря: {player.backpack}")
    if not player.extra_health_given or not player.extra_health_given_two:
        print(f"Способность активна: если у вас < 4 здоровья, вы захилите 10")
    else:
        print(f"Способность не активна: если у вас < 4 здоровья, вы захилите 10 (купить ее можно в магазине)")
    print("\nИнформация о враге:")
    print(f"Здоровье: {enemy.health}")
    print(f"Урон: {enemy.damage}")
    print(f"Способность: Возмещение")
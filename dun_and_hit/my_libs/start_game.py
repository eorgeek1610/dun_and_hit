def start_game(player,enemy):
    # Восстановление здоровья и урона после игры
    player.reset_health()
    enemy.reset_health()
    enemy.reset_damage()
    # Игровой цикл
    while player.health > 0 and enemy.health > 0:
        enemy.attack(player)
        player.attack(enemy)
        player.extra_health()
        from dun_and_hit.my_libs.close_game import close_game
        close_game(player, enemy)

        # Восстановление здоровья и урона после игры
    player.reset_health()
    enemy.reset_health()
    enemy.reset_damage()

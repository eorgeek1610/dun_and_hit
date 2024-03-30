def close_game(player, enemy):
    if player.health <= 0:
        print("\nВы были поверженны...")
        if player.money <= 0:
            print("Увы, вы нечего не заработали.")
        elif player.money >= 10:
            print("У вас забрали 5 монет.")
            player.money -= 5
        else:
            print("Увы, вы нечего не заработали.")
    elif enemy.health <= 0:
        print("\nВЫ ПОБЕДИЛИ!")
        print("Вы получили + 10 монет!")
        player.money += 10
        enemy.magaz_health += 1

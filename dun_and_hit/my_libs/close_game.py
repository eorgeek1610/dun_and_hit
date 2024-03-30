def close_game(player, enemy):
    if player.health <= 0:
        print("\nВы были поверженны...")
        if player.money <= 0:
            print("Увы, вы нечего не заработали.")
        elif player.money >= 10:
            print("У вас забрали 10 монет.")
            player.money -= 10
        else:
            print("Увы, вы нечего не заработали.")
    elif enemy.health <= 0:
        print("\nВЫ ПОБЕДИЛИ!")
        if player.money <= 15:
            print(f"Вы получили + {player.boost_money} монет!")
            player.money += player.boost_money
        elif player.money <= 70:
            print(f"Вы получили {player.boost_money - 5} монет")
            player.money += player.boost_money - 5
        else:
            print(f"Вы получили {player.boost_money - 10} монет")
            player.money += player.boost_money - 10

        player.money += 10
        if enemy.magaz_health <= 15:
            enemy.magaz_health += 2
            enemy.magaz_damage += 0.5
        else:
            enemy.magaz_health += 1

import hw7_classes as cls


def game():
    num_rooms = int(input('Input num rooms: '))
    hero = cls.Hero()
    monster = cls.Monster()
    builder = cls.Builder(num_rooms)
    rooms = builder.build_maze()
    for room in rooms:
        if room.monster:
            while hero.life_points > 0 or monster.life_points > 0:
                hero.life_points = hero.life_points - monster.life_points
                monster.life_points = monster.life_points - hero.life_points
        if hero.life_points > monster.life_points:
            return print('Hero win!')
        else:
            return print('Monster win!')


if __name__ == '__main__':
    game()

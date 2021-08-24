from random import randint


class Wall:

    def __init__(self, wall1, wall2, wall3, wall4):
        self.wall1 = wall1
        self.wall2 = wall2
        self.wall3 = wall3
        self.wall4 = wall4


class Room(Wall):

    def __init__(self, wall1, wall2, wall3, wall4, door_pos, hero=False, monster=False):
        super().__init__(wall1, wall2, wall3, wall4)
        self.door_pos = door_pos
        self.hero = hero
        self.monster = monster

    @staticmethod
    def door_pos():
        d_p = ["top", "right", "bottom", "left"]
        door_pos = d_p[randint(0, 3)]
        return door_pos

    def get_monster(self):
        return self.monster

    def get_hero(self):
        return self.hero


class NPC:

    def __init__(self, life_points, damage):
        self.life_points = life_points
        self.damage = damage


class Hero(NPC):
    def __init__(self):
        NPC.__init__(self, randint(1000, 2000), randint(20, 40))


class Monster(NPC):
    def __init__(self):
        NPC.__init__(self, randint(1000, 2000), randint(20, 40))


class Builder:
    def __init__(self, num_rooms):
        self.num_rooms = num_rooms
        self.rooms_count = 0
        self.rooms = []
        self.room = Room(None, None, None, None, Room.door_pos())
        self.first_room = Room(None, None, None, None, Room.door_pos(), hero=True)
        self.last_room = Room(None, None, None, None, Room.door_pos(), monster=True)

    def build_maze(self):
        while self.num_rooms > 0:
            if self.rooms_count == 0:
                self.rooms.append(self.first_room)
                self.num_rooms -= 1
            elif self.num_rooms == 1:
                self.rooms.append(self.last_room)
                self.num_rooms -= 1
            else:
                self.rooms.append(self.room)
                self.num_rooms -= 1
        return self.rooms

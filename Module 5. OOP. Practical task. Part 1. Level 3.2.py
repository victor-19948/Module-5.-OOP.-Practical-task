import random

class Warrior:

    def __init__(self, name, health, armor, endurance, min_damage, max_damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.endurance = endurance
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.endurance_over = 0
        self.armor_damage = 0
        self.health_damage = 0

    def attack(self):
        if self.endurance <= 0:
            if not self.endurance_over:
                self.min_damage //= 2
                self.max_damage //= 2
                self.endurance_over = 1
        else:
            self.endurance -= 10

    def damage_taken(self, damage):
        if self.armor > 0:
            damage_remain = damage - (self.armor * 2)
            if damage_remain < 0:
                self.armor_damage = damage // 2
                self.armor -= self.armor_damage
            else:
                self.armor_damage = self.armor
                self.armor = 0
                self.health_damage = damage_remain
                self.health -= self.health_damage
        else:
            self.armor_damage = 0
            self.health_damage = damage
            self.health -= self.health_damage



    def health_damage(self, damage):
        self.health -= damage

    def armor_damage(self, damage):
        self.armor -= damage // 2

    def health_rage_damage(self, damage):
        self.health -= int(damage * 1.5)

    def armor_rage_damage(self, damage):
        self.health -= int(damage / 2 * 1.5)


a = Warrior('Арагорн сын Араторна', 200, 100, 50, 20, 40)
b = Warrior('Гендельф Белобородый', 100, 50, 50, 40, 80)

def Duel(warrior_a, warrior_b):
    step = 1
    fight = True
    while fight:
        warriors_action = [random.randrange(0, 2), random.randrange(0, 2)]
        print(f'Ход {step}')
        if warriors_action == [1, 0]:
            warrior_a.attack()
            damage_now = random.randrange(warrior_a.min_damage, warrior_a.max_damage)
            warrior_b.damage_taken(damage_now)
            print(f'Воин {warrior_a.name} атаковал воина {warrior_b.name} и нанес {damage_now} единиц урона')
            print(f'Воин {warrior_b.name} потерял {warrior_b.armor_damage} брони и {warrior_b.health_damage} здоровья '
                  f'и теперь имеет {warrior_b.health} здоровья и {warrior_b.armor} брони')
        elif warriors_action == [0, 1]:
            warrior_b.attack()
            damage_now = random.randrange(warrior_b.min_damage, warrior_b.max_damage)
            warrior_a.damage_taken(damage_now)
            print(f'Воин {warrior_b.name} атаковал воина {warrior_a.name} и нанес {damage_now} единиц урона')
            print(f'Воин {warrior_a.name} потерял {warrior_a.armor_damage} брони и {warrior_a.health_damage} здоровья '
                  f'и теперь имеет {warrior_a.health} здоровья и {warrior_a.armor} брони')
        elif warriors_action == [1, 1]:
            print('Воины одновременно атаковали друг друга')
            warrior_a.attack()
            damage_now = int((random.randrange(warrior_a.min_damage, warrior_a.max_damage)) * 1.5)
            warrior_b.damage_taken(damage_now)
            print(f'Воин {warrior_a.name} нанес воину {warrior_b.name} {damage_now} единиц урона')
            warrior_b.attack()
            damage_now = int((random.randrange(warrior_b.min_damage, warrior_b.max_damage)) * 1.5)
            warrior_a.damage_taken(damage_now)
            print(f'А воин {warrior_b.name} нанес воину {warrior_a.name} {damage_now} единиц урона')
            print(f'Воин {warrior_a.name} потерял {warrior_a.armor_damage} брони и {warrior_a.health_damage} здоровья '
                  f'и теперь имеет {warrior_a.health} здоровья и {warrior_a.armor} брони')
            print(f'А Воин {warrior_b.name} потерял {warrior_b.armor_damage} брони и {warrior_b.health_damage} здоровья'
                  f' и теперь имеет {warrior_b.health} здоровья и {warrior_b.armor} брони')
        else:
            print('Ни один из воинов не атаковал другого')
            print('Каждый в угрожающей боевой стойке выжидает подходящего момента')
        step += 1
        if warrior_a.health <= 0 and warrior_b.health <= 0:
            print('Оба бойца охваченные яростью битвы в своей последней атаке убили друг друга')
            print('Битва окончена')
            fight = False
        elif warrior_a.health <= 0:
            print(f'{warrior_b.name} одержал победу!')
            print('Битва окончена')
            fight = False
        elif warrior_b.health <= 0:
            print(f'{warrior_a.name} одержал победу!')
            print('Битва окончена')
            fight = False
        else:
            print()


Duel(a, b)

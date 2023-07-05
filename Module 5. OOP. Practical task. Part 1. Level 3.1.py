import random

class Warrior:

    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def damage_taken(self, damage):
        self.health -= damage


a = Warrior('Арагорн сын Араторна', 100, 20)
b = Warrior('Гендельф Белобородый', 100, 20)

def Duel(warrior_a, warrior_b):
    step = 1
    fight = True
    while fight:
        turn = random.randrange(0, 2)
        print(f'Ход {step}')
        if turn:
            warrior_a.damage_taken(warrior_b.damage)
            print(f'Юнит {warrior_b.name} атаковал юнита {warrior_a.name} и нанес {warrior_b.damage} единиц урона')
            print(f'Здоровье {warrior_a.name} теперь {warrior_a.health} ед.')
            print(f'Здоровье {warrior_b.name} теперь {warrior_b.health} ед.')
        else:
            warrior_b.damage_taken(warrior_a.damage)
            print(f'Юнит {warrior_a.name} атаковал юнита {warrior_b.name} и нанес {warrior_a.damage} единиц урона')
            print(f'Здоровье {warrior_a.name} теперь {warrior_a.health} ед.')
            print(f'Здоровье {warrior_b.name} теперь {warrior_b.health} ед.')
        step += 1
        if warrior_a.health <= 0:
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

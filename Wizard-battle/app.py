import random
import time

from characters import Wizard, Creature, SmallAnimal, Dragon
def main():
    print_header()
    game_loop()


def print_header():
    print("----------------------------")
    print("       WIZARD BATTLE")
    print("----------------------------")
    print()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 57, True),
        Wizard('Evil Wizard', 1000),

    ]

    name = input("Welcome, my friend. How should I call you?")
    hero = Wizard(name, 75)

    while True:

        active_creature = random.choice (creatures)
        print('A {} of level {} appeared from the darkness of the dungeon.'.format (active_creature.name,
                                                                                     active_creature.level))
        cmd = input('Do you [a]ttack, [r]un away,[l]ook around or e[x]it?')

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard was defeated and tries to hide')
                time.sleep(5)
                print('The wizard returnsv revitalized!!!')

        elif cmd == 'r':
            print('Run!')
        elif cmd == 'l':
            print('The wizard {} looks around and find:'.format(hero.name))
            for c in creatures:
                print('* A {} of level {}.'.format(c.name, c.level))
        elif cmd == 'x':
            print('Ok. Bye')
            break

        else:
            print('Think again. What do you want to do?')

        if not creatures:
            print('You defeated all the creatures. Leaving the dungeon ...')
            break

if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program runs a game of Pig.
"""


import random


class Die(object):
    """
    This is a constructor for the Die class.
    """

    random.seed(0)

    def __init__(self):
        self.rolled = 0

    def roll(self):
        self.rolled = random.randint(1, 7)
        return self.rolled


class Player(object):
    """
    This is a constructor for the Player class.
    """
    def __init__(self):
        self.name = ''
        self.turn_status = 0
        self.turn_score = 0
        self.total_score = 0

class Game(object):
    """
    This is a constructor for the GAme class.
    """
    def __init__(self, p1, p2):
        self.p1 = Player(p1)
        self.p2 = Player(p2)
        self.die = Die()
        self.turn(self.p1)

    def player_turn(self, player):
        while player.turn_status == 1 and player.total_score < 100:
            roll = self.die.roll()
            if roll == 1:
                print '*' * 40
                print 'You rolled a 1. Points are forfeit.'
                print '*' * 40
                self.turn_score = 0
                print '{} your score is {}.'.format(player.name, player.total_score)
                continue


def doSomething():
    """
    Args:
        num_seconds (int): Value for actual time of simulation.
        time_req (int): Value for time required to process task.
    Returns:
        None
    Example:
        >> simulateOneServer(11, 2)
    """

if __name__ == '__main__':
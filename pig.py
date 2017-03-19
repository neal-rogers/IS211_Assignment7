#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program DOES SOME STUFF.
"""


import


class Die:
    """
    This is a constructor for the Die class.
    """
    def __init__(self):

class Player:
    """
    This is a constructor for the Player class.
    """
    def __init__(self):

class Game:
    """
    This is a constructor for the GAme class.
    """
    def __init__(self):


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


def main():
    """
    Args:

    Returns:
        None
    Example:
        >>
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--file', help='Enter the data url.')
    parser.add_argument('--server', help='Enter number of servers.')

    args = parser.parse_args()

    if args.url:
        #url = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'
        csvdata = urllib2.urlopen(args.url)
        reader = csv.reader(csvdata)
        for row in reader:
            simulateOneServer(int(row[0], int(row[2])))
    else:
        print 'error'

if __name__ == '__main__':
    main()
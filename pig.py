#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program DOES SOME STUFF.
"""


import csv
import argparse
import urllib2


class Queue:
    """
    This is a constructor for the Queue class.
    """
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Request:
    """
    This is a constructor for the Request class.
    """
    def __init__(self, time, req_time):
        self.timestamp = time
        self.req_time = req_time

    def get_stamp(self):
        return self.timestamp

    def wait_time(self, current_time):
        return current_time - self.timestamp

class Server:
    """
    This is a constructor for the Server class.
    """
    def __init__(self):
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.process_time()


# This function needs to accept the input_file?
def simulateOneServer(num_seconds, req_time):
    """
    Args:
        num_seconds (int): Value for actual time of simulation.
        time_req (int): Value for time required to process task.
    Returns:
        None
    Example:
        >> simulateOneServer(11, 2)
    """
    lab_printer = Server()
    print_queue = Queue()
    waiting_times = []
    request = Request(num_seconds, req_time)
    print_queue.enqueue(request)

    for current_second in range(num_seconds):

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

        average_wait = sum(waiting_times) / len(waiting_times)
        print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))

#def simulateManyServers():
    #I don't understand how to implement a round robin function.


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
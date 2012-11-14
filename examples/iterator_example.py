#!/usr/bin/env python


class Unicoder(object):

    def __init__(self):
        self.start = 50
        self.stop = 1000
        self.current = None
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def next(self):
        if self.current <= self.stop:
            ret = unichr(self.current)
            self.current += 1
            return ret
        else:
            raise StopIteration()


def main():
    u = Unicoder()
    for char in u:
        print char


if __name__ == '__main__':
    main()
#!/usr/bin/env python

def abc():
    yield "a"
    yield "b"
    yield "c"

def make_unicode():
    for i in range(50,1000):
        yield unichr(i)


def main():
    for char in make_unicode():
        print char

if __name__ == '__main__':
    main()
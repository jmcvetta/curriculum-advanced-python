#!/usr/bin/env python

'''
<!-- comments here -->
'''

def makebold(fn):
    def wrapped():
        return '<b>' + fn() + '</b>'
    return wrapped

def makebold2(fn):
    return '<b>' + fn() + '</b>'

def makeitalic(fn):
    def wrapped():
        return '<i>' + fn() + '</i>'
    return wrapped

def makecomment(fn):
    def wrapped():
        return '<!--' + fn() + '-->'
    return wrapped



@makebold2
def hello():
    return "Hello world!"

def euros(fn):
    factor = .65
    def wrapped():
        return [price * factor for price in fn() ]
    return wrapped
        
def discount(fn):
    '''
    @param fn: Fetches a list of prices
    @type fn:  Function that returns an interable
    '''
    discount = 1.00
    def wrapped():
        return [price - discount for price in fn() ]
    return wrapped

@euros
@discount
def get_prices():
    "Returns prices in USD"
    return [1.99, 250, 9.95]

@discount
def get_a_price():
    return 9.99

def get_euro_prices():
    return get_prices()

def main():
    #print hello()
    #print get_prices()
    print get_a_price()

if __name__ == '__main__':
    main()
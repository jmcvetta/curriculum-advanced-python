#!/usr/bin/env python



class Employee(object):
    '''
    An employee of a company
    '''
    
    __company_motto = "Make Mo' Money!"
    
    # Getter
    @property
    def company_motto(self):
        return Employee.__company_motto
    
    # Setter
    @company_motto.setter
    def company_motto(self, other):
        Employee.__company_motto = other
        
    def __init__(self, name):
        self.name = name
    
#    def __str__(self):
#        return 'Employee %s' % self.name
    

    

class Boss(Employee):
    '''
    A boss a company
    '''
    
    def __init__(self, name, title):
        super(Boss, self).__init__(name)
        self.title = title

def main():
    e1 = Employee('Joe Worker')
    e2 = Employee('Sarah Smith')
    b1 = Boss('Samar Bossman', 'Deputy Chief Assistant Paper Pusher')
    print e1
    
    

if __name__ == '__main__':
    main()
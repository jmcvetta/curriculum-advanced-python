#!/usr/bin/env python


class LoadBalancerException(BaseException):
    '''
    Something is wrong with the load balancer
    '''
    

class LoadBalancerWrongStateException(LoadBalancerException):
    '''
    Load balancer is in the wrong state for the requested action.
    '''


def reboot_load_balancer():
    # blah blah blah code....
    raise LoadBalancerWrongStateException('Load balancer must be in STANDBY state to reboot')

def main():
    try:
        #x = 1 / 0
        reboot_load_balancer()
    except LoadBalancerException as err:
        print 'ERROR: %s' % err
        # or maybe send a command to change the LB state then try again, etc
        


if __name__ == '__main__':
    main()
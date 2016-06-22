# -*- coding: utf-8 -*-  
'''
Created on 2014-8-26

@author: Kemin Yu
'''
import sys
import optparse
from scenario import Scenario
from params import Param
from webparams import WebParam

def commandui(args=sys.argv[1:]):
    parser = optparse.OptionParser(usage="%prog [options]", version="%prog 1.0")

    parser.add_option("-s", "--scenario",
                      dest="scenario",
                      action="store_true",
                      default=False,
                      help='run scenario request - login first, then run multi-requests')
    parser.add_option("-a", "--app",
                      dest="app",
                      action="store_true",
                      default=False,
                      help='run application if. parameter checking request - login first, then run multi-requests')
    parser.add_option("-w", "--web",
                      dest="web",
                      action="store_true",
                      default=False,
                      help='run web if. parameter checking request - login first, then run multi-requests')
    
    (options, args) = parser.parse_args(args)
    
    if options.scenario: # update tools
        s = Scenario()
        s.run()
    elif options.app:
        p = Param()
        p.run()
        p.print_result()
    elif options.web:
        p = WebParam()
        p.run()
        p.print_result()

if __name__ == '__main__':
    commandui()
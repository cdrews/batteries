#!/usr/bin/python -tt
import sys
import os
import logging
import argparse 
import matplotlib.pyplot as plot
import yaml


def prop_vector(arr,p):
    return [int(e[p]) for e in arr]

def main(args):
    logger = logging.getLogger("CHANGEME")
    logger.debug(args)
    #'description'
    #'Weight (g)' 
    #'Discharge (c)' 
    #'Capacity(mAh)' 
    #'Max Charge Rate (C)' 
    #'Config (s)' 
    #'Length-A(mm)' 
    #'Height-B(mm)'
    #'Width-C(mm)'
    batts = yaml.load(open("results.yaml"))
    batts = filter(lambda b:int(b["Capacity(mAh)"])>900 and int(b["Capacity(mAh)"])<1500,batts)
    batts = filter(lambda b:int(b["Config (s)"])==3,batts)
    x=prop_vector(batts,"Weight (g)")
    y=prop_vector(batts,"Capacity(mAh)")
    c=prop_vector(batts,"Config (s)")
    plot.scatter(x,y,c=c)
    plot.show()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Do somthing amazing")

    parser.add_argument('filename', metavar='filename', type=str, help='a filename to process') 
    parser.add_argument('-d','--debug', 
        choices=['critical','error','warn', 'info', 'debug'],
        default='critical',
        help="debug level")

    args = parser.parse_args()
    level={'critical':logging.CRITICAL,'error':logging.ERROR,'warn':logging.WARNING, 'info':logging.INFO, 'debug':logging.DEBUG}[args.debug]
    logging.basicConfig(format="%(asctime)-15s %(message)s")
    logger = logging.getLogger("CHANGEME")
    logger.setLevel(level)

    main(args)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

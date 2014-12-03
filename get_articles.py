#!/usr/bin/python -tt
import sys
import os
import logging
import argparse 
import urllib
import time

from bs4 import BeautifulSoup

def get_links(file_):
    soup=BeautifulSoup(open(file_))
    for tr in soup.find_all("tr",class_="zeroLineHeight"):
        yield(tr.find_all("a")[0].get("href"))

def download_article(link):
    url="http://hobbyking.com/hobbyking/store/%s"%link
    urllib.urlretrieve(url,"data/%s"%link)
    print "got %s, sleeping 10 seconds"%link

def main(args):
    for file_ in args.filename:
        for link in get_links(file_):
            download_article(link)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Do somthing amazing")

    parser.add_argument('filename', metavar='filename', type=str, help='a filename to process',nargs="+") 
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

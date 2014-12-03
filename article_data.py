#!/usr/bin/python -tt
import sys
import os
import logging
import argparse 
import urllib
import time
import json
from bs4 import BeautifulSoup
import yaml
import csv

def get_attributes(file_):
    soup=BeautifulSoup(open(file_))
    description = soup.find(id="productDescription").text
    attributes = {}
    attributes["description"] = description
    div = soup.find_all("div",class_="data_tbl")[0]
    table = div.find_all("table",class_="defaultLineHeight")[0]
    for tr in table.find_all("tr"):
        attributes[tr.find_all("td")[0].text]=float(tr.find_all("td")[1].text)
    return attributes

def json2csv(data):
    writer = csv.writer(open("results.csv","w"))

    writer.writerow(sorted(data[0].keys()))
    for d in data:
        row = []
        for k in sorted(data[0].keys()):
            row.append(d[k])
        writer.writerow(row)

def main(args):
    results = [] 
    for file_ in args.filename:
        try:
            attr = get_attributes(file_)
            results.append(attr)
        except:
            logging.exception("that did not work")
        f=open("results.yaml","w")
        f.write(yaml.dump(results,encoding=('utf-8')))
        f.close()
        f=open("results.json","w")
        f.write(json.dumps(results))
        f.close()
        json2csv(results)

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

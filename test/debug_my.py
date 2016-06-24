#!/usr/bin/env python
# encoding: utf-8
_author_ = 'jialiang'
_email_ = 'jialiang.liu@nexusguard.com'


'''
Debug function file
'''
import os, sys
lib_path = os.path.abspath(os.path.join("."))
sys.path.append(lib_path)

from pymongo.mongo_client import MongoClient

def debug(mongo_addr):
    connection = MongoClient(mongo_addr)
    print connection

if __name__ == '__main__':
    mongo_addr = "mongodb://127.0.0.1:27017,127.0.0.2:27018"
    print debug(mongo_addr)



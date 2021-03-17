#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
from connections import Mongo 
from utils import CSV
import time

if __name__ == '__main__':
    
    mongoClient = Mongo("bigdata", "csv_data")

    # mongoClient.showListDatabaseNames()
    # mongoClient.showListCollectionNames()

    utilCsv = CSV()

    utilCsv.loadCsvByName("covid.csv")

    start_time = time.time()

    utilCsv.resetIndexCsv()

    dataToInsert = utilCsv.fitDataToInsert()

    mongoClient.insertMany(dataToInsert)

    print("Execution time: {} segundos".format(time.time() - start_time))
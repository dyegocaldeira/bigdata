#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
import csv

class CSV:
    
    def __init__(self):
        pass

    def loadCsvByName(self, csvName):
        self.loadedCsv = pd.read_csv(csvName)
    
    def getCsvLoaded(self):
        return self.loadedCsv

    def resetIndexCsv(self):
        self.loadedCsv.reset_index(inplace=True)

    def fitDataToInsert(self):
        return self.loadedCsv.to_dict("records")

    def openCsvByName(self, csvName):
        return csv.reader(open(csvName))
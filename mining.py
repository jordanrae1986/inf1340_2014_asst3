#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime

class StockMiner:
    def __init__(self, stock_name, stock_file_name):
        self.stock_name = stock_name
        self.monthly_averages = []
        self.stock_data = self.read_json_from_file(stock_file_name)
        self.init_monthly_averages_list()

    def monthly_averages_list(self):
        for daily_stock_results in self.stock_data:
            



def read_stock_data(stock_name, stock_file_name):
    return


def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)


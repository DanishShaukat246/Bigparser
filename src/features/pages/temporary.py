from selenium.webdriver.common.by import By
import json, os
from src.features.pages.header import Header
from selenium.webdriver.support.ui import Select
from src.features.utilities import driver
from array import *

class temporary():
    def __init__(self):
        self.arrayKeyword = []
        self.arrayData = []
        self.random = 0
        self.arrayGroupStats = []
        self.action = 0
        self.programSeats = 0
        self.departmentsCount = 0

temp = temporary()

def set_keywordArray(arr2):
    temp.arrayKeyword = arr2

def set_random(rand):
    temp.random = rand

def set_arrayData(arr):
    temp.arrayData = arr

def set_groupStatArray(arr):
    temp.arrayGroupStats = arr

def set_actions(val):
    temp.action = val

def set_programSeats(seats):
    temp.programSeats = seats

def set_departmentsCount(count):
    temp.departmentsCount = count
import pygame, sys, random, json


class Top_records:
    def __init__(self):
        self.win_weigh = 500
        self.win_heigh = 600
        self.table = json.load('Top_records.json')

    def render(self):
        pass
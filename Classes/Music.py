import pygame
import sys
import os
import json
import settings
from utilities import *


class Music():
    """
    Занимается загрузкой музыки и воспроизведением
    """
    def __init__(self, music):
        self.done = True
        self.music = music

    def play(self):
        play_music(self.music)


if __name__ == '__main__':
    music = Music('JT_Machinima.mp3').play()
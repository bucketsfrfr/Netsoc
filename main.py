### IMPORTS ###
import datetime
import yaml
import logging
import traceback
import os
import time
import json
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get

def main():
    try:

        with open(f"{os.path.dirname(__file__)}/config.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

        channels = {
            "netsoc_verified":620996002316288041
            }

        emote_list = {
'list':
'''Current Options Are
monkaS
ayaya
xqcL
suprised_pikachu
big_chungus
KEKW
PogChamp
bio-hazard
D:''',
'monkaS':
'''
⠟⠛⣉⣡⣴⣶⣶⣶⣶⣶⣶⣤⣉⡛⢿⣿⣿⠿⠟⠛⣋⣉⣩⣭⣭⣭⣉⣙⠛⠈
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠡⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠆⠄⠈⢻⣿⣿⣿⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠰⠄⠙⣿
⣿⣿⣿⣿⣿⣿⣿⣔⡗⠠⢀⣼⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠘⠠⢀⣼
⡉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣋⣡⡈⠛⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿
⠿⠷⠶⣦⣭⣉⣉⣉⣉⣭⡥⣴⡿⠿⢟⣠⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶
⣿⣷⣶⣶⣤⣬⣭⣽⣿⣿⠖⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁
⣿⣿⣿⣿⡿⠿⠛⣫⣥⣴⣾⣿⣿⣿⣿⣿⣷⣤⣝⠛⢛⣫⣭⣭⣭⣭⣅⠄⠄⠄
⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣷⡀⠄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣶⣶⣶⣮⣭⣉⣙⡛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⢛⣉⣭
⣛⣛⣛⡛⠻⠿⢿⣿⣿⣶⣶⣶⣶⣦⣤⣬⣭⣭⣭⣭⣭⣭⣭⣭⣴⣾⣿⣿⣿⡿
⢿⣿⣿⣿⣿⣷⣶⣦⣭⣭⣭⣭⣍⣉⣉⣉⣛⣛⠛⠛⠛⠛⠛⠛⠛⢛⣋⣭⣄⠄
⣶⣦⣬⣍⣙⣛⠛⠛⠛⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄
''',
'ayaya':
'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⡻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⠿⣿⣿⣿⣿⡿⠿⣷⣌⠛⣿⣿⣿
⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣧⡘⢿⡿⢋⣼⣿⣿⣿⣿⣷⣄⠢⣭⣓⠌⠻⣿
⣿⣿⠿⣿⣿⡃⠻⣿⣿⣿⣿⣿⣿⣷⠌⢡⣾⡧⠭⠍⣛⠿⢿⣿⣷⣜⠻⣷⣆⠙
⣿⣿⡇⢻⣿⡇⢰⣮⣝⡻⢿⣿⣿⠋⣴⣆⠩⣶⣶⣶⣶⣭⣶⣦⣭⣍⣓⠈⢿⣌
⣿⣿⢣⣎⢻⣿⡜⣿⣿⣿⣶⣬⣁⣘⠻⠿⠦⠙⠿⠿⠟⣛⣛⣛⣛⣩⡍⢩⣤⣌
⣿⡏⡼⣛⣬⠩⣽⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿
⣿⢠⣴⣿⣿⣷⣌⡳⢌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢻⡷⢸⣿⣿
⡇⣾⣿⣿⣿⣿⣿⣿⣶⣤⣽⣿⣿⣿⣿⣿⣿⣿⣟⠕⢋⣤⣴⣾⣿⣿⣷⢸⣿⣿
⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⡟⡿⡿⣿⢸⣿⣿
⣿⡌⢿⣿⣿⠿⠟⠛⠒⣀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣵⣧⣿⢸⣿⣿
⡰⣭⣌⠻⣧⢴⡶⣿⡿⣿⣿⣿⣿⣿⣿⠿⠟⣛⣋⣍⡻⣿⣿⣿⣿⣿⡿⠆⣿⣿
⣧⠻⣿⣧⡹⣾⣧⣿⣱⣿⣿⣿⣿⡏⢁⣶⣿⣿⣿⣿⣧⢻⣿⣿⡿⠋⠁⠄⢹⣿
⣿⣧⡹⣿⣇⢿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣿⣿⣿⡿⢟⣼⡿⠋⢀⣀⠄⠄⠈⣿
⣿⣿⣧⠻⣿⣦⣙⠿⠿⢿⣿⣿⣿⣿⣷⣮⠭⠭⠍⣒⣫⡵⢞⣨⡼⠁⠄⠄⠄⡸
''',
'xqcL':
'''
⠀⠀⠀⣠⣴⣾⣿⣿⣿⣶⣄⣀⣀⣤⣶⣶⣦⣤⠀⠀⠀⠀⠀
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀
⢀⣼⣿⡟⠉⠉⠉⠉⠉⠛⠻⣿⣿⣿⣿⣿⠿⠟⠛⠳⠂⠀⠀
⣿⣿⣿⠟⠉⠉⠛⠛⠓⠀⠉⠻⣿⣿⣿⡿⢀⡄⠲⠶⢶⣶⠀
⣿⣿⣷⣤⣤⣄⣀⣀⡘⠁⠀⣠⣿⣿⣯⡀⢹⡀⢀⣀⣠⡽⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
⣿⣿⣿⣍⡉⠉⠉⠉⠙⠛⠛⠾⠿⠿⠿⠿⠿⠿⣿⣿⣿⠀⠀
⠛⠉⠉⠉⠛⠓⠲⢶⣶⣶⣶⣶⣦⣤⣤⣤⣤⣤⣤⡶⠁⠀⠀
⣴⣾⣿⣿⣿⣷⣦⣄⡈⠙⢿⠿⠛⠋⠉⠉⠉⠙⠁⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀⠀⣴⣾⣿⣿⣿⣶⣦⡀⠀⠀⠀
⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣧⣀⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀
⣀⣴⣶⣦⡄⠉⣿⣿⣿⣿⣿⡟⠉⣉⡉⠙⢻⣿⣿⡟⠀⠀⠀
⣿⣿⡿⠛⢁⣤⣿⣿⣿⣿⣿⡇⠈⣿⣿⣧⠀⠙⣿⠁
''',
'big_chungus':
'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣧⠀⠀⠀⢰⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡆⠀⠀⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⠀⢰⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⠀⢸⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⢸⡄⠸⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⢸⡅⠀⣿⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣥⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⡿⣿⣿⡿⡅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠀⠉⡙⢔⠛⣟⢋⠦⢵⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣄⠀⠀⠁⣿⣯⡥⠃⠀⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡇⠀⠀⠀⠐⠠⠊⢀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀
⠀⠀⠀⡜⣭⠤⢍⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢛⢭⣗⠀
⠀⠀⠀⠁⠈⠀⠀⣀⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠀⠰⡅
⠀⠀⠀⢀⠀⠀⡀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠔⠠⡕⠀
⠀⠀⠀⠀⣿⣷⣶⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠉⢆⠀⠀⠀⠀
⠀⢀⠤⠀⠀⢤⣤⣽⣿⣿⣦⣀⢀⡠⢤⡤⠄⠀⠒⠀⠁⠀⠀⠀⢘⠔⠀⠀⠀⠀
⠀⠀⠀⡐⠈⠁⠈⠛⣛⠿⠟⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠑⠒⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''',
'suprised_pikachu':
'''
⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
''',
'KEKW':
'''
⢰⣶⠶⢶⣶⣶⡶⢶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡶⠶⢶⣶⣶⣶⣶
⠘⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⠿⠄⠄⠄⠈⠉⠄⠄⣹⣶⣿⣿⣿⣿⢿
⠄⠤⣾⣿⣿⣿⣿⣷⣤⡈⠙⠛⣿⣿⣿⣧⣀⠠⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶
⢠⠄⠄⣀⣀⣀⣭⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣤⣿⣿⠉⠉⠉⢉⣉⡉⠉⠉⠙⠛⠛
⢸⣿⡀⠄⠈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣷⣾⣿
⢸⣿⣿⣿⣿⣿⣿⣿⣿⠛⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢸⣿⣿⣿⣿⣿⡿⣿⣿⣴⣿⣿⣿⣿⣄⣠⣴⣿⣷⣭⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠸⠿⣿⣿⣿⠋⣴⡟⠋⠈⠻⠿⠿⠛⠛⠛⠛⠛⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢸⣿⣿⣿⡁⠈⠉⠄⠄⠄⠄⠄⣤⡄⠄⠄⠄⠄⠄⠈⠄⠈⠻⠿⠛⢿⣿⣿⣿⣿⣿
⢸⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⣠⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣿⣿⣿⣿
⢸⣿⣿⣿⡀⠄⠄⠄⠄⠄⠄⠄⠉⠉⠁⠄⠄⠄⠄⠐⠒⠒⠄⠄⠄⠄⠉⢸⣿⣿⣿
⢸⣿⣿⣿⢿⣦⣄⣠⣄⠛⠟⠃⣀⣀⡀⠄⠄⣀⣀⣀⣀⣀⣀⡀⢀⣰⣦⣼⣿⣿⡿
⢸⣿⣿⣿⣿⣿⣿⣻⣿⠄⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣥⣾⣟⣿⣿⣿⣿⣿
⢸⣿⣿⣿⣿⣿⣿⣿⣿⡆⠈⠿⠿⠿⠿⠿⠿⠿⠿⠿⣧⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
''',
'PogChamp':
'''
⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠉⠉⠙⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠀⠀
⣿⣿⣯⣥⣤⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣏⣀⣀⣀⡀⠀
⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠻⠿⠟⠉⠉⠉⢻⣿⣿⣿⡿⠟⠋⣡⣼⣿⣿⣿⡄
⣿⣿⣿⣟⣭⣤⣶⣶⣿⣿⠃⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⡅⡀⢀⣩⣤⣤⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣛⡛⠛⠛⠛⢋⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⠛⠛⠓⠠⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣦⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⢿⡿⢿⣿⣿⣿⠃
⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣄⣀⣀⠀⠀⠀⠀⠀⢰⣾⣿⣿⠏⠀
⠀⠀⠀⠀⠀⠀⠉⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣜⡻⠋⠀⠀⠀
⣰⣾⣷⣶⣿⣾⣖⣻⣿⣿⡿⣿⣿⣿⣿⠿⠿⠟⠛⠛⠛⠋⠉⠉⢉⡽⠃⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡉⠉⠉⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⡤⠚⠉⠀⠀⠀⠀⠀
⠛⠛⣿⣿⣿⣿⣿⣿⣿⠉⠛⢶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠠⣾⣿⣿⣿⣿⣿⠿⠟⠃⠀⠀⠀⠈⠲⣴⣦⣤⣤⣤⣶⡾⠁⠀⠀⠀⠀⠀⠀⠀
⠄⠈⠉⠻⢿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
''',
'D:':
'''
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢛⣉⣩⣤⣬⣉⣉⣉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠋⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣈⠻⢿⣿⣿⣿⣿⣿
⣿⣿⣿⠟⢁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡙⠿⣿⣿⣿
⣿⣿⠏⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠙⢻⣷⡆⠹⣿⣿
⣿⡇⢠⣿⣿⣿⣿⣿⣿⡟⠋⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣀⣴⣿⣿⡄⢹⣿
⡟⢀⣿⣿⣿⣿⣿⣿⣿⣧⣀⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢻
⠁⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⢛⣋⣉⣉⣉⠙⢿⣿⣿⣿⣿⣿⡇⢸
⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣡⣴⣶⣿⣿⣿⣿⣿⣿⣧⠄⢿⣿⣿⣿⣿⡇⢸
⣇⠈⣿⣿⣿⣿⣿⣿⣿⡟⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢸⣿⣿⣿⣿⠃⣼
⣿⣆⠘⣿⣿⣿⣿⣿⣿⡇⣴⣤⣤⣬⣉⡛⠻⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠃⢸⣿
⣿⣿⣆⠘⢿⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿⠿⠷⠌⠛⢛⣋⣉⣁⣸⣿⡿⠋⣠⣿⣿
⣿⣿⣿⣶⡈⠙⢿⣿⣟⣈⣉⣩⣥⣤⣶⣶⣶⣾⣿⣿⣿⣿⣿⡿⠟⢁⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣶⣄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⣉⣤⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣈⡉⠉⠛⣋⣉⣉⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
''',
'bio-hazard':
'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡖⠁⠀⠀⠀⠀⠀⠀⠈⢲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⢀⣀⣤⣤⣤⣤⣀⡀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣔⢿⡿⠟⠛⠛⠻⢿⡿⣢⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣷⣤⣀⡀⢀⣀⣤⣾⣿⣿⣿⣷⣶⣤⡀⠀⠀⠀⠀
⠀⠀⢠⣾⣿⡿⠿⠿⠿⣿⣿⣿⣿⡿⠏⠻⢿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣷⡀⠀⠀
⠀⢠⡿⠋⠁⠀⠀⢸⣿⡇⠉⠻⣿⠇⠀⠀⠸⣿⡿⠋⢰⣿⡇⠀⠀⠈⠙⢿⡄⠀
⠀⡿⠁⠀⠀⠀⠀⠘⣿⣷⡀⠀⠰⣿⣶⣶⣿⡎⠀⢀⣾⣿⠇⠀⠀⠀⠀⠈⢿⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠹⣿⣷⣄⠀⣿⣿⣿⣿⠀⣠⣾⣿⠏⠀⠀⠀⠀⠀⠀⢸⠀
⠀⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⢇⣿⣿⣿⣿⡸⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠈⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠐⢤⣀⣀⢀⣀⣠⣴⣿⣿⠿⠋⠙⠿⣿⣿⣦⣄⣀⠀⠀⣀⡠⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀
'''
        }
        grad_list = ['2018', '2019', '2020', '2021']
        token = cfg["token"]
        build = "2021.06.16"

        bot = commands.Bot(
            command_prefix="$",
            intents=discord.Intents().all(),
            activity=discord.Game(name=f"with your firewalls - [Build]{build}")
            )

        @bot.event
        async def on_ready():
            try:
                print(f"[START UP] Logged in to bot: {bot.user}\n[START UP] Running discord.py version: {discord.__version__}")
                await check_users()
            except Exception as e:
                print(e)

        @bot.event
        async def on_raw_reaction_add(payload):
            try:
                if payload.member.bot:
                    pass
                else:
                    with open(f"{os.path.dirname(__file__)}/reactrole.json") as json_file:
                        data = json.load(json_file)
                        for x in data:
                            if x["emoji"] == payload.emoji.name and x["message_id"] == payload.message_id:
                                role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x["role_id"])
                                await payload.member.add_roles(role)
            except Exception as e:
                print(f"[EXCEPTION] {e}")

        @bot.event
        async def on_raw_reaction_remove(payload):
            try:
                with open(f"{os.path.dirname(__file__)}/reactrole.json") as json_file:
                    data = json.load(json_file)
                    for x in data:
                        if x["emoji"] == payload.emoji.name and x["message_id"] == payload.message_id:
                            role = discord.utils.get(bot.get_guild(payload.guild_id).roles, id=x["role_id"])
                            await bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)
            except Exception as e:
                print(f"[EXCEPTION] {e}")

        @bot.event
        async def on_member_join(user):
            try:
                guild = bot.get_guild(364524308091109377)
                await user.add_roles(guild.get_role(839335125993127937))
            except Exception as e:
                print(f"[EXCEPTION] {e}")

        async def check_users():
            try:
                guild = bot.get_guild(364524308091109377)
                for member in guild.members:
                    if len(member.roles) == 1:
                        await member.add_roles(guild.get_role(839335125993127937))
            except Exception as e:
                print(f"[EXCEPTION] {e}")

        async def deletemsg(ctx):
            try:
                await ctx.message.delete()
                print(f"[INFO]\nApplicant {ctx.message.author.name}\nSuccesfully deleted message: {ctx.message.content}")
            except Exception as e:
                await ctx.message.author.send(f"{ctx.author.mention}, Please DM an Executive ASAP!")
                print(f"[ERROR]\nApplicant {ctx.message.author.name} caused\n[EXCEPTION] - {e}")

        @bot.command()
        @commands.has_any_role("Non-Verified")
        async def apply(ctx, first: str=None, last: str=None, year: str=None, accept: str=None):
            try:
                # Make the characters lowercase
                accept.lower()
                output = ""
                # Ensure that no fields are left empty
                if first == None or last == None or year == None or accept == None:
                    await ctx.message.author.send(f"{ctx.message.author.mention}! You have a missing field! Please DM an Executive if you believe there is an error!")
                    print(f"[INFO]\nApplication Denied\nReason: Missing field\nApplicant: {ctx.message.author.name}\nMessage content: {ctx.message.content}")
                    await deletemsg(ctx)
                    return
                # Ensure they agree to the rules
                if accept != "yes":
                    await ctx.message.author.send(f"{ctx.message.author.mention}! You must agree to the rules found in #welcome-and-rules! Please DM an Executive if you believe there is an error!")
                    print(f"[INFO]\nApplication Denied\nReason: Rules not accepted\nApplicant: {ctx.message.author.name}\nMessage content: {ctx.message.content}")
                    await deletemsg(ctx)
                    return
                # Ensure their grad year is valid
                if len(year) != 4 or (int(year) > 2030 and int(year) < 2010):
                    await ctx.message.author.send(f"{ctx.message.author.mention}! You must provide a valid grad year! Accepted years are 2019-2025. Please DM an Executive if you believe there is an error!")
                    print(f"[INFO]\nApplication Denied\nReason: Invalid Grad Year\nApplicant: {ctx.message.author.name}\nMessage content: {ctx.message.content}")
                    await deletemsg(ctx)
                    return
                # Set the members nickname
                name = f"{first.capitalize()} {last.upper()}."
                output += f"[INFO]\nApplicant {ctx.message.author.name}\nSetting nickname to {name}..."
                try:
                    await ctx.message.author.edit(nick=name)
                    output += f"\nSuccessfully set nickname to {name}"
                except Exception as e:
                    await ctx.message.author.send(f"{ctx.message.author.mention}! There was an error setting your nickname! Please DM an Executive for assistance.")
                    print(f"[ERROR]\nApplicant {ctx.message.author.name}\nCould not set nickname.\nError: {e}")
                    return
                # Add them to their year role
                output += (f"\nSetting year role and Verified roles...")
                try:
                    year = f"Class of {year}"
                    year_role = discord.utils.get(ctx.guild.roles, name=year)
                    verified_role = discord.utils.get(ctx.guild.roles, name="Verified")
                    non_verified_role = discord.utils.get(ctx.guild.roles, name="Non-Verified")
                    prospective_role = discord.utils.get(ctx.guild.roles, name="Prospective Students")
                    await ctx.message.author.add_roles(verified_role, year_role)
                    await ctx.message.author.remove_roles(non_verified_role, prospective_role)
                    output += f"\nSuccessfully added {year} role, Verified role and removed Non-Verified Role"
                except Exception as e:
                    await ctx.message.author.send(f"{ctx.message.author.mention}! There was an error adding your roles! Please DM an Executive for assistance.")
                    print(f"[ERROR]\nApplicant {ctx.message.author.name}\nCould not set roles\nError: {e}")
                    return
                # Delete their message
                output += f"\nDeleting command message..."
                await deletemsg(ctx)
                output += f"\nMessage deleted!"
                # Send the user a message to confirm they have registered
                output += f"\n[INFO]: Applicant {ctx.message.author.name} - Sending success message..."
                success_member = discord.Embed(title="A Huge Success!",
                                            description=f"""Hi!
                                                        You've successfully registered and verified yourself for the Netsoc
                                                        OT - Official Discord! Below are the details we gathered from your
                                                        application, please let us know if there are any issues!
                                                        \nYour Name: {name}\nGrad Year: {year}\nAccept Rules: {accept}
                                                        \nThank you for joining us! Make sure to see our role 
                                                        assignment channel for more roles!""",
                                            colour=discord.Colour.dark_blue())
                await ctx.message.author.send(embed=success_member)
                output += f"\nSuccessfully sent applicant success message."
                # Send the executives a message to confirm a new registration
                output += f"\nSending executive success message..."
                channel = bot.get_channel(channels["netsoc_verified"])
                success_execs = discord.Embed(title="New Member!",
                                            description=f"""Someone successfully registered and verified themself! Below are the details gathered from the application
                                            \nName: {name}\nGrad Year: {year}\nAccept Rules: {accept}""",
                                            color=discord.Colour.dark_blue())
                await channel.send(embed=success_execs)
                output += f"\nSuccessfully sent executive success message."
                print(output)
            except Exception as e:
                print(f"[EXCEPTION]\nApplicant {ctx.message.author.name}\nUnexpected Error Occured\nError: {e}\n{output}")
                await deletemsg(ctx)

        @bot.command()
        @commands.has_any_role("Server Admin", "Netsoc Executive")
        async def reactrole(ctx, emoji, role: discord.Role, *, message):
            try:
                await ctx.channel.purge(limit=1)
                emb = discord.Embed(
                    title=message.split("|")[0],
                    description=message.split("|")[1],
                    color=int(message.split("|")[2], 16)
                    )
                msg = await ctx.channel.send(embed=emb)
                await msg.add_reaction(emoji)
                with open(f"{os.path.dirname(__file__)}/reactrole.json") as json_file:
                    data = json.load(json_file)
                    new_react_role = {
                        "role_name":role.name,
                        "role_id":role.id,
                        "emoji":emoji,
                        "message_id":msg.id
                    }
                    data.append(new_react_role)
                with open(f"{os.path.dirname(__file__)}/reactrole.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)
            except Exception as e:
                print(f"[EXCEPTION] {e}")

        @bot.command()
        @commands.has_any_role("Server Admin", "Netsoc Executive")
        async def purge(ctx, x=0):
            try:
                await ctx.channel.purge(limit=int(x)+1)
            except Exception as e:
                print(f"[EXCEPTION] {e}")

        @bot.command()
        async def lmgt(ctx):
            try:
                await ctx.channel.purge(limit=1)
                message_id = await ctx.channel.history(limit=1).flatten()
                message_id = str(message_id[0])
                message_id = message_id.split(" ")[1]
                message_id = message_id.split("=")[1]
                message = await ctx.channel.fetch_message(message_id)
                output = 'https://letmegooglethat.com/?q='
                output += message.content.replace(" ", "+")
                await ctx.channel.send(output)
            except Exception as e:
                print(f"[EXCEPTION] {e}")
    
        @bot.command()
        @commands.has_any_role("Server Admin", "Netsoc Executive")
        async def alumni_check(ctx):
            try:
                await ctx.channel.purge(limit=1)
                for x in grad_list:
                    year_role = discord.utils.get(ctx.guild.roles, name=f"Class of {x}")
                    alumni_role = discord.utils.get(ctx.guild.roles, name="Alumni")
                    guild = bot.get_guild(364524308091109377)
                    for member in guild.members:
                        if year_role in member.roles:
                            await member.add_roles(alumni_role)
            except Exception as e:
                print(f"[EXCEPTION] {e}")

        @bot.command()
        @commands.has_any_role("Server Admin", "Netsoc Executive")
        async def give_role_user(ctx, role: discord.Role, target: discord.Member):
            try:
                await target.add_roles(role)
            except Exception as e:
                print(f"[EXCEPTION] {e}")

        @bot.command()
        @commands.has_any_role("Server Admin", "Netsoc Executive")
        async def give_role_role(ctx, role: discord.Role, target: discord.Role):
            try:
                guild = bot.get_guild(364524308091109377)
                for member in guild.members:
                    if target in member.roles:
                        await member.add_roles(role)
            except Exception as e:
                print(f"[EXCEPTION] {e}")
            

        @bot.command()
        async def ascii(ctx, emote):
            try:
                await ctx.channel.purge(limit=1)
                await ctx.channel.send(emote_list[emote])
            except Exception as e:
                print(f"[EXCEPTION] {e}")
        
        @bot.command()
        @commands.has_any_role("Server Admin", "Netsoc Executive")
        async def say(ctx, *, message):
            try:
                await ctx.channel.purge(limit=1)
                await ctx.channel.send(message)
            except Exception as e:
                print(f"[EXCEPTION] {e}")

        bot.run(token, bot=True, reconnect=True)

    except Exception as e:
        print(f"[EXCEPTION] {e}")
        with open(f"{os.path.dirname(__file__)}/error.txt", "r+") as f:
            f.append(f"[ERROR] - {e}")
        main()

if __name__ == "__main__":
    main()
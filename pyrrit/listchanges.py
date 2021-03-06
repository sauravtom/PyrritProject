from os import system
import requests
import sys
import constants
import json
import os

__author__ = 'arnav'

url = "http://" + constants.g_url + "/changes/?q=status:open"

col_y = '\033[93m'
col_p = '\033[95m'
col_g = '\033[92m'
col_0 = '\033[0m'


def show_all_list():
    resp_str = os.popen("curl " + url).read()
    # ugly hack because python refuses to get the full response
    resp_str = resp_str.replace(resp_str[:4], '')
    #ugly hack because gerrit's json has 4 stupid characters in the first line
    json_data = json.loads(resp_str)
    for item in json_data:
        print(col_y + str(item.get('_number')) + col_0 + "\t" + item.get('subject'))
        print("  " + col_g + item.get('project') + col_0 + "\n")

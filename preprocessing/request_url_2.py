import sys
import os
import urllib.error
import urllib.request
import os
import asyncio
import subprocess
import wget
import pandas as pd
import codecs
import csv
import os
import shutil
from itertools import islice
from urllib.error import HTTPError
from urllib.request import urlopen, Request

download_path= 'data_50k'
APIKEY = '1ef38937bf841c4a90b49d0e756bd4980b56886822cd8f20d6cf18cd449d68c9'
apps_path = 'app_msc.csv'

def list_apk_files(directory):
    apk_files = []
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否以 ".apk" 结尾
        if filename.endswith(".apk"):
            # source_file =  os.path.join(download_path,filename)
            # # new_filename = filename.replace('50kAndroidzoo', '')
            # destination_file = os.path.join(download_path, 'raw_dataset', filename)
            # shutil.move(source_file, destination_file)
            apk_files.append(filename)

    return apk_files
exist_file_list = list_apk_files(download_path)


def get_raw_webpage(url):
    """
        Download a web url as raw bytes
    """
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = response.read()
        return data

    except urllib.error.HTTPError as e:
        print('HTTPError: ', e.code , file = sys.stderr)
        return None

    except urllib.error.URLError as e:
        print('URLError: ', e.args, file = sys.stderr)
        return None

    except ValueError as e:
        print('Invalid url.', e.args, file = sys.stderr)

    return None


def get_webpage(url):
    """
    Get webpage as raw bytes and then
    convert to readable form
    """
    data = get_raw_webpage(url)
    if data == None:
        return None

    return data.decode('utf-8-sig')

downed_count = 0
with open(apps_path, encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in islice(reader, 1, None):

        # print(row)
        name = row[1]
        url = 'https://androzoo.uni.lu/api/download?apikey={}&sha256='.format(APIKEY)+name
        name_temp = name+'.apk'
        path = os.path.join(download_path,name_temp)
        
        if name_temp not in exist_file_list:
            print(row)

            get_webpage(url)
        else:
            downed_count +=1
            print("exist")
        
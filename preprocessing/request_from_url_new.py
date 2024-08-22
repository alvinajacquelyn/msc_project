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

download_path= 'apk'
APIKEY = '1ef38937bf841c4a90b49d0e756bd4980b56886822cd8f20d6cf18cd449d68c9'
apps_path = 'apps.csv'

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

#https://androzoo.uni.lu/api/download?apikey=1ef38937bf841c4a90b49d0e756bd4980b56886822cd8f20d6cf18cd449d68c9&sha256=
exist_file_list = list_apk_files(download_path)

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
            try:
                wget.download(url,path)
            except HTTPError:
                continue
        else:
            downed_count +=1
            print("exist")
        


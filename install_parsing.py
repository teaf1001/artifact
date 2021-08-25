import glob
import re
import time
import pandas as pd
import sqlite3

def install_start(arr, data):
    arr[0] =  re.compile('StartTime=[\d/ :]*').findall(data)[0].replace("StartTime=","")
    arr[0] = time_convert(arr[0])# UTC+0 -> UTC+9
    arr[1] = re.compile(r'Name=*').findall(data)[0].replace("Name=","")
    arr[2] =  re.compile(r'Path=[\w:\\]*').findall(data)[0].replace("Path=","")
    arr[3] =  re.compile('Size=\w*').findall(data)[0].replace("Size=","")
    arr[4] =  re.compile('Magic=\w*').findall(data)[0].replace("Magic=","")
    arr[5] =  re.compile('SizeOfImage=\w*').findall(data)[0].replace("SizeOfImage=","")
    arr[6] =  re.compile('PeChecksum=\w*').findall(data)[0].replace("PeChecksum=","")
    arr[7] =  re.compile('LinkDate=[\d/ :]*').findall(data)[0].replace("LinkDate=","")
    arr[8] =  re.compile('LinkerVersion=[\.\d]*').findall(data)[0].replace("LinkerVersion=","")
    arr[9] =  re.compile('BinFileVersion=[\.\d]*').findall(data)[0].replace("BinFileVersion=","")
    arr[10] = re.compile('BinProductVersion=[\.\d]*').findall(data)[0].replace("BinProductVersion=","")
    arr[11] = re.compile('BinaryType=\w*').findall(data)[0].replace("BinaryType=","")
    arr[12] = re.compile('Created=[\d/ :]*').findall(data)[0].replace("Created=","")
    arr[13] = re.compile('Modified=[\d/ :]*').findall(data)[0].replace("Modified=","")
    arr[14] = re.compile('LastAccessed=[\d/ :]*').findall(data)[0].replace("LastAccessed=","")
    arr[15] = re.compile('VerLanguage=\d*').findall(data)[0].replace("VerLanguage=","")
    arr[16] = re.compile('Id=\w*').findall(data)[0].replace("Id=","")
    arr[17] = re.compile('FileVersion=[\.\d]*').findall(data)[0].replace("FileVersion=","")
    arr[18] = re.compile('CompanyName=\w*').findall(data)[0].replace("CompanyName=","")
    arr[19] = re.compile('ProductVersion=[\.\d]*').findall(data)[0].replace("ProductVersion=","")
    arr[20] = re.compile('PeImageType=0x\w*').findall(data)[0].replace("PeImageType=v","")
    arr[21] = re.compile('PeSubsystem=\w*').findall(data)[0].replace("PeSubsystem=","")
    arr[22] = re.compile('CrcChecksum=0x\w*').findall(data)[0].replace("CrcChecksum=","")
    arr[23] = re.compile('FileSize=0x\w*').findall(data)[0].replace("FileSize=","")
    arr[24] = re.compile('StopTime=[\d/ :]*').findall(data)[0].replace("StopTime=","")

    return arr

def time_convert(timestamp):
    inpattern = '%d/%m/%Y %H:%M:%S'
    Epoch = int(time.mktime(time.strptime(timestamp, inpattern))) + 32400 #UTC+0 -> UTC+9
    outtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(Epoch))
    return outtime


def process():
    arr = ['' for i in range(25)]
    ext_data = []
    files = glob.glob('./INSTALL/*')

    for file in files:
        f = open(file, 'r', encoding='utf-16 LE')
        data = f.read()
        try:
            arr = install_start(arr, data)
            ext_data.append(arr)
        except:
            continue
    df = pd.DataFrame(ext_data)
    df.columns = ['StartTime', 'Name', 'Path', 'Size', 'Magic', 'SizeOfImage', 'PeChecksum', 'LinkDate', 'LinkerVersion', 'BinFileVersion', 'BinProductVersion', 'BinaryType', 'Created', 'Modified', 'LastAccessed', 'VerLanguage', 'Id', 'FileVersion', 'CompanyName', 'ProductVersion', 'PeImageType', 'PeSubsystem', 'CrcChecksum', 'FileSize', 'StopTime']
    df.to_csv('./install.csv', index=False)

    return df
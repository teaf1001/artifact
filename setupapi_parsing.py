import re
import glob
import time
import pandas as pd
import sqlite3

def time_convert(timestamp):
    inpattern = '%Y/%m/%d %H:%M:%S'
    Epoch = int(time.mktime(time.strptime(timestamp, inpattern)))
    outtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(Epoch))
    return outtime

def process():
    files = glob.glob('./SETUPAPI/*')

    regex_device = re.compile('>>>  \[Device Install \(Hardware initiated\).*')
    regex_time = re.compile('>>>  Section start .*')

    info = {'device': [], 'timestamp': []}

    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                device = regex_device.findall(lines[i])
                if device:
                    timestamp = regex_time.findall(lines[i+1])
                    device = device[0].replace(">>>  [Device Install (Hardware initiated) - ","")[:-1]
                    timestamp = time_convert(timestamp[0].replace(">>>  Section start ","")[:-4])

                    info['device'].append(device)
                    info['timestamp'].append(timestamp)

    df = pd.DataFrame(info)
    df.to_csv('./setupapi.csv', index=False)

    return df

import re
import os
import sys
import glob
import setupapi_parsing as setupapi
import install_parsing as install
import appcache_parsing as appcache
import db_handle


def print_guide():
    print("example: python main.py [ALL|INSTALL|AppCache|SETUPAPI]")

def parse_artifact(target):
    if target == 'INSTALL':
        WINDIR = os.environ['WINDIR']
        path = "{}\\appcompat\\Programs\\Install\\".format(WINDIR)
        regex = re.compile('INSTALL_?[\w-]*\.txt')
        savepath = r".\INSTALL"
        save(path, regex, savepath)

    elif target == 'AppCache':
        WINDIR = os.environ['LocalAppdata']
        path = "{}\\Packages\\Microsoft.Windows.Search_cw5n1h2txyewy\\LocalState\\DeviceSearchCache\\".format(WINDIR)
        regex = re.compile('AppCache[\w]*\.txt')
        savepath = r".\AppCache"
        save(path, regex, savepath)

    elif target == 'SETUPAPI':
        WINDIR = os.environ['WINDIR']
        path = "{}\\INF\\".format(WINDIR)
        regex = re.compile('setupapi\.dev\.?\w*\.log')
        savepath = r".\SETUPAPI"
        save(path, regex, savepath)

    elif target == 'ALL':
        parse_artifact('INSTALL')
        parse_artifact('AppCache')
        parse_artifact('SETUPAPI')

def save(path, regex, savepath):
    files = glob.glob(path + "*")

    logs = []
    for file in files:
        matched = regex.findall(file)
        if matched:
            logs.append(matched[0])

    if not os.path.isdir(savepath):
        os.mkdir(savepath)

    for log in logs:
        with open(path + log, 'rb') as f:
            with open(r'{}\{}'.format(savepath, log), 'wb') as w:
                w.write(f.read())

if __name__=="__main__":

    argv = sys.argv[1]
    if argv != 'ALL' and argv != 'INSTALL' and argv != 'AppCache' and argv != 'SETUPAPI':
        print_guide()

    elif argv == 'INSTALL':
        df_install = install.process()

    elif argv == 'AppCache':
        df_appcache = appcache.process()

    elif argv == 'SETUPAPI':
        df_setupapi = setupapi.process()

    elif argv == 'ALL':
        parse_artifact('ALL')

        df_setupapi = setupapi.process()
        df_install  = install.process()
        df_appcache = appcache.process()

        db_connection = db_handle.__init__()

        df_setupapi.to_sql('setupapi', db_connection)
        df_install.to_sql('install', db_connection)
        df_appcache.to_sql('appcache', db_connection)

    else:
        parse_artifact(argv)



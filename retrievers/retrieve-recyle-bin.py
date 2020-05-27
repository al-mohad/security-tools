import os
from _winreg import *
import optparse


def sid2user(sid):
    try:
        key = OpenKey = (
            HKEY_LOCAL_MACHINE, 'SOFWARE\Microsoft\Windows NT\Current\Version\ProfileList' + '\\' + sid)
        (value, type) = QueryValueEx(key, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid


def retrunDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
        return None


def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files = os.listdir(recycleDir + sid)
        user = sid2user(sid)
        print('[*] Listing files for User: ' + str(user))
        for file in files:
            print('[+] Found File: ' + str(file))


def main():
    recycledDir = recycledDir()
    findRecycled(recycledDir)
    if __name__ == '__main__':
        main()

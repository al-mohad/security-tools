# Almohad 
# This is a brute-force attack script for encrypted zip files
# This is purely for educational purposes!

import zipfile
charlist = 'abcdefghijklmnopqrstuvwxyz'
complete = []

for current in range(6):
    # create a list for each charset in charlist
    a = [i for i in charlist]
    for x in range (current):
        a = [y + i for i in charlist for y in a]
    complete = complete + a

z = zipfile.ZipFile('sales.zip')

tries = 0

for password in complete:
    try:
        tries += 1
        print(f'Trying: {tries}')
        z.setpassword(password.encode('ascii'))
        z.extract('sales.php')
        print(f'Password found after {tries} tries: {password}')
        break
    except:
        pass

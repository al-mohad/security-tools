# To do get dynamic zip file name from user
# Get keyword from user
# Save wordlist to text file
import zipfile
import itertools

keywords = ['mike', 'smith', '0802', '1995', 'ilove', 'barcelona']
combinations = itertools.combinations(keywords, 2)
final_combinations = []

for combination in combinations:
    final_combinations.append(combination[0] +combination[1])
    print(final_combinations)

z = zipfile.ZipFile('php.txt.zip')

wordlist = open('cain.txt', 'r').read()
wordlist = wordlist.splitlines()

tries = 0

for word in wordlist:
    try:
        tries += 1
        z.setpassword(word.encode('ascii'))
        z.extract('php.txt')
        print(f'Password Found! Password: {word}')
        break
    except:
        pass
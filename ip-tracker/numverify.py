import requests
import argparse
import json
apiKey = '0b85713070dc79f0e4fdab942155278e'
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', help='Phone Number to Track')
    args = parser.parse_args()
    number = args.number
    url = 'http://apilayer.net/api/validate?access_key=' + \
        apiKey+'&number='+number+'&country_code=NG&format=1'
    response = requests.get(url)
    data = json.loads(response.content)

    # print(data)
    print('\t[+] NUMBER\t\t\t', data['number'])
    print('\t[+] CARRIER\t\t\t', data['carrier'])
    print('\t[+] LINE TYPE\t\t\t', data['line_type'])
    print('\t[+] COUNTRY\t\t\t', data['country_name'])
    print('\t[+] COUNTRY CODE\t\t', data['country_code'])
    # print('\t[+] TIME\t\t', data['timezone'])
    # print('\t[+] ZIP\t\t\t', data['zip'])
    # print('\t[+] LAT\t\t\t', data['lat'])
    # print('\t[+] LON\t\t\t', data['lon'])
    # print('\t[+] AS\t\t\t', data['as'])
    # print('\t[+] ORG\t\t\t', data['org'])

import re

import requests as requests

base_url = 'https://www.bonbast.com'

currencies = {
    'try': 'Turkish Lira',
    'afn': 'Afghan Afghani',
    'bhd': 'Bahraini Dinar',
    'cny': 'Chinese Yuan',
    'cad': 'Canadian Dollar',
    'usd': 'United States Dollar',
    'thb': 'Thai Baht',
    'azn': 'Azerbaijani Manat',
    'amd': '10 Armenian Dram',
    'rub': 'Russian Ruble',
    'eur': 'Euro',
    'chf': 'Swiss Franc',
    'jpy': '10 Japanese Yen',
    'kwd': 'Kuwaiti Dinar',
    'gbp': 'British Pound',
    'sek': 'Swedish Krona',
    'myr': 'Malaysian Ringgit',
    'omr': 'Omani Rial',
    'aud': 'Australian Dollar',
    'dkk': 'Danish Krone',
    'inr': 'Indian Rupee',
    'aed': 'UAE Dirham',
    'qar': 'Qatari Rial',
    'iqd': '100 Iraqi Dinar',
    'hkd': 'Hong Kong Dollar',
    'sar': 'Saudi Riyal',
    'sgd': 'Singapore Dollar',
    'nok': 'Norwegian Krone',
}

coins = {
    'emami1': 'Emami',
    'azadi1g': 'Gerami',
    'azadi1': 'Azadi',
    'azadi1_2': '½ Azadi',
    'azadi1_4': '¼ Azadi',
}

gold = {
    'mithqal': 'Gold Mithqal',
    'gol18': 'Gold Gram',
}

buy = '1'
sell = '2'


# get the token from the main page of bonbast.com
def get_token_from_main_page():
    headers = {
        'authority': 'bonbast.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'cache-control': 'no-cache',
        'cookie': 'cookieconsent_status=true; st_bb=0',
        'pragma': 'no-cache',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
    }

    response = requests.get(base_url, headers=headers)
    search = re.search("\$\.post\('/json',{\s*data:\"(.+)\"", response.text, re.MULTILINE)
    if search is None:
        print('Error: token not found')
        return None
    return search.group(1)


# get response by using token acquired from main page
def get_response_from_api(token):
    headers = {
        'authority': 'bonbast.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'cookieconsent_status=true; st_bb=0',
        'origin': 'https://bonbast.com',
        'referer': 'https://bonbast.com/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'data': token,
        'webdriver': 'false',
    }

    response = requests.post(f'{base_url}/json', headers=headers, data=data)
    return response.json()


if __name__ == '__main__':
    token = get_token_from_main_page()
    if token is None:
        print('Error: token not found')
        exit(1)
    response = get_response_from_api(token)
    print(response)

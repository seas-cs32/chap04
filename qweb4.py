### chap04/qweb4.py
import requests

def main():
    print('Searching wikipedia: changed "<nothing>"')
    # print('Searching wikipedia: changed "path"')
    # print('Searching wikipedia: changed "hostname"')
    # print('Searching wikipedia: changed "srsearch"')

    # Concatenate the first 3 components of a URL for HTTP
    protocol = 'https'
    hostname = 'en.wikipedia.org'
    # hostname = 'en.wikipediaasdfghjasdfghj.org'
    path = '/w/api.php'
    # path = '/asdfghjasdfghj/api.php'
    url = protocol + '://' + hostname + path

    # Describe the query string as a Python dictionary
    query = {'action': 'query',
             'list': 'search',
             'srsearch': 'The Cat in the Hat',
             # 'srsearch': 'asdfghjasdfghj',
             'srlimit': 1,
             'format': 'json'
    }

    response = requests.get(url, params=query)

    print("response.status_code =", response.status_code)

if __name__ == '__main__':
    main()